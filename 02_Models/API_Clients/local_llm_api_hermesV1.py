from fastapi import FastAPI, Request
from llama_cpp import Llama
import uvicorn

app = FastAPI()

# === Load OpenHermes Model ===
MODEL_PATH = "C:/Users/Mugi/Desktop/text-generation-webui-main/user_data/models/OpenHermes-2.5-Mistral-7B-medquad.Q6_K.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=10,
    n_gpu_layers=20
)

@app.post("/v1/chat/completions")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages", [])

    prompt = ""
    for msg in messages:
        prompt += f"{msg['role']}: {msg['content']}\n"
    prompt += "assistant:"

    result = llm(prompt, max_tokens=300)
    reply = result["choices"][0]["text"]

    return {
        "id": "chatcmpl-hermes",
        "object": "chat.completion",
        "created": 0,
        "model": "openhermes",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": reply.strip()
                },
                "finish_reason": "stop"
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)
