"""local_llm_api_openchat.py – OpenChat‑3.5‑0106 FastAPI wrapper

Run with:
    GPU_LAYERS=-1 uvicorn orchestration_engines.local_llm_api_openchat:app --port 5001

Environment vars
----------------
MODEL_PATH   override gguf path (otherwise models/openchat-3.5-0106.Q5_K_M.gguf)
GPU_LAYERS   -1 = full GPU, 0 = CPU, N = layers on GPU (default -1)
MAX_TOKENS   default generation length (default 256)
"""
from __future__ import annotations

# ─── ENSURE PROJECT ROOT ON PYTHONPATH ───────────────────────────────
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))  # add AI_Memory_Core/

import atexit
import logging
import os
import signal
import asyncio
from pathlib import Path

# Fix Windows asyncio issues
if os.name == 'nt':  # Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from llama_cpp import Llama

from path_config import MODELS_DIR

# ─── CONFIG ──────────────────────────────────────────────────────────
DEFAULT_MODEL = MODELS_DIR / "openchat-3.5-0106.Q5_K_M.gguf"
MODEL_PATH: Path = Path(os.getenv("MODEL_PATH", DEFAULT_MODEL))
GPU_LAYERS: int = int(os.getenv("GPU_LAYERS", "-1"))
MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "256"))

# ─── GLOBAL MODEL INSTANCE ───────────────────────────────────────────
llm: Llama | None = None

# ─── LOGGING SETUP ───────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("OpenChatAPI")

# ─── GPU MEMORY MANAGEMENT ───────────────────────────────────────────

def cleanup_gpu_memory():
    """Clean up GPU memory and model instance"""
    global llm
    if llm is not None:
        try:
            logger.info("🧹 Cleaning up GPU memory...")
            del llm
            llm = None
            logger.info("✅ GPU memory cleaned up")
        except Exception as e:
            logger.error(f"❌ Error during cleanup: {e}")

def signal_handler(signum, frame):
    """Handle shutdown signals gracefully"""
    logger.info(f"📡 Received signal {signum}, shutting down gracefully...")
    cleanup_gpu_memory()
    sys.exit(0)

# Register cleanup handlers
atexit.register(cleanup_gpu_memory)
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# ─── MODEL LOADING ───────────────────────────────────────────────────

def load_model() -> Llama:
    """Load the model with proper error handling"""
    global llm
    
    if llm is not None:
        return llm
    
    try:
        logger.info(f"🗣️ Loading OpenChat model: {MODEL_PATH.name}")
        logger.info(f"🔧 GPU layers: {GPU_LAYERS}, Max tokens: {MAX_TOKENS}")
        
        llm = Llama(
            model_path=str(MODEL_PATH),
            n_ctx=2048,
            n_threads=os.cpu_count() or 8,
            n_gpu_layers=GPU_LAYERS,
            verbose=False
        )
        
        logger.info(f"✅ OpenChat model loaded successfully (gpu_layers={GPU_LAYERS})")
        return llm
        
    except Exception as exc:
        logger.exception(f"❌ Failed to load model: {exc}")
        raise

# ─── APP SETUP ───────────────────────────────────────────────────────
app = FastAPI(title="OpenChat API", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    """Initialize model on startup"""
    logger.info("🚀 OpenChat API starting...")
    # Don't load model here - load it lazily on first request
    logger.info("🚀 OpenChat API started successfully (model will load on first request)")

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up on shutdown"""
    cleanup_gpu_memory()

# ─── ENDPOINT ───────────────────────────────────────────────────────
@app.post("/v1/chat/completions")
async def chat(request: Request):  # type: ignore[valid-type]
    try:
        # Ensure model is loaded
        model = load_model()
        
        data = await request.json()
        messages = data.get("messages", [])
        prompt = messages[-1]["content"] if messages else ""
        temperature = data.get("temperature", 0.7)
        max_tokens = data.get("max_tokens", MAX_TOKENS)

        output = model(prompt=prompt, temperature=temperature, max_tokens=max_tokens)
        reply = output["choices"][0]["text"].strip()

        return {
            "id": "chatcmpl-local-openchat",
            "object": "chat.completion",
            "created": 0,
            "model": MODEL_PATH.name,
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": reply},
                    "finish_reason": "stop",
                }
            ],
        }

    except Exception as e:  # noqa: BLE001
        logger.exception("❌ OpenChat inference error")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model": MODEL_PATH.name,
        "gpu_layers": GPU_LAYERS,
        "model_loaded": llm is not None,
        "ready": llm is not None  # Server is ready when model is loaded
    }

# ─── ENTRYPOINT ─────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5001)
