from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from llama_cpp import Llama
import uvicorn
import logging
import traceback

# ─── CONFIG ─────────────────────────────────────────────────────────────
MODEL_PATH = (
    "C:/Users/Mugi/Desktop/text-generation-webui-main/"
    "user_data/models/OpenHermes-2.5-Mistral-7B-medquad.Q6_K.gguf"
)

# ─── APP & MODEL ─────────────────────────────────────────────────────────
app = FastAPI()
logging.basicConfig(level=logging.INFO)

# Increase context to handle larger JSON input
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=8192,
    n_threads=10,
    n_gpu_layers=20,
)

# ─── ENDPOINT ────────────────────────────────────────────────────────────
@app.post("/v1/chat/completions")
async def chat(request: Request):
    try:
        data = await request.json()
        messages = data.get("messages", [])

        # Reconstruct prompt with system+user if provided
        prompt = ""
        for m in messages:
            role    = m.get("role", "user")
            content = m.get("content", "")
            prompt += f"{role}: {content}\n"
        prompt += "assistant:"

        # Run the model
        result = llm(
            prompt,
            max_tokens=data.get("max_tokens", 512),
            temperature=data.get("temperature", 0.4)
        )
        reply = result["choices"][0]["text"].strip()

        return {
            "id":       "chatcmpl-local-hermes",
            "object":   "chat.completion",
            "created":  0,
            "model":    "local-hermes",
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": reply},
                    "finish_reason": "stop"
                }
            ]
        }

    except Exception as e:
        logging.error("❌ Hermes API error", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "trace": traceback.format_exc()
            }
        )

# ─── LAUNCH ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)
