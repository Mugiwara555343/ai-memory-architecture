# local_llm_api_mythomax.py

from fastapi import FastAPI, Request, JSONResponse
from llama_cpp import Llama
import uvicorn, logging, traceback

# ─── CONFIG ────────────────────────────────────────────────────
MODEL_PATH = (
    "C:/Users/Mugi/Desktop/text-generation-webui-main/"
    "user_data/models/mythomax-l2-13b.Q6_K.gguf"
)
PORT = 5002

# ─── APP & MODEL ───────────────────────────────────────────────
app = FastAPI()
logging.basicConfig(level=logging.INFO)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=8192,        # match your other endpoints
    n_threads=10,
    n_gpu_layers=20,
)

# ─── ENDPOINT ─────────────────────────────────────────────────
@app.post("/v1/chat/completions")
async def chat(request: Request):
    try:
        data = await request.json()
        messages = data.get("messages", [])
        prompt = "".join(f"{m['role']}: {m['content']}\n" for m in messages) + "assistant:"
        result = llm(
            prompt,
            max_tokens=data.get("max_tokens", 512),
            temperature=data.get("temperature", 0.5),
        )
        reply = result["choices"][0]["text"].strip()
        return {
            "id": "chatcmpl-local-mythomax",
            "object": "chat.completion",
            "created": 0,
            "model": "local-mythomax",
            "choices": [{"index": 0, "message": {"role": "assistant", "content": reply}, "finish_reason": "stop"}]
        }
    except Exception as e:
        logging.error("❌ MythoMax API error", exc_info=True)
        return JSONResponse(status_code=500, content={"error": str(e), "trace": traceback.format_exc()})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT)
