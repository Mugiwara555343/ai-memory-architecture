# interface.py
import os
import glob
import gradio as gr
import requests
from pathlib import Path
import json

CONFIG_PATH = Path(__file__).parent / "model_config.json"

def load_model_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# ========== CONFIG ==========
MODEL_API_URL = "http://127.0.0.1:5000/v1/chat/completions"  # Change port if needed

MODEL_ROLES = load_model_config()
AVAILABLE_MODELS = list(MODEL_ROLES.keys())
DEFAULT_MODEL_ROLE = "default_model"

MEMORY_DIR = str(Path(__file__).parents[1] / "memory_core" / "99_System_Settings" / "parsed_memory"/ "vault_json")

def get_latest_memory_file(extension=".md") -> str:
    """Find the latest modified memory file with given extension."""
    files = glob.glob(os.path.join(MEMORY_DIR, f"*{extension}"))
    if not files:
        return ""
    latest = max(files, key=os.path.getmtime)
    return latest

def list_memory_files(extensions=(".md", ".json")) -> list:
    """Returns a list of (display_name, full_path) tuples for memory files."""
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(MEMORY_DIR, f"*{ext}")))
    
    sorted_files = sorted(files, key=os.path.getmtime, reverse=True)
    return [(Path(f).name, f) for f in sorted_files]



# ========== CORE FUNCTIONS ==========

def load_memory_context(memory_path: str) -> str:
    """Loads memory context from .json or .md file."""
    path = Path(memory_path)
    
    if path.suffix == ".json":
        try:
            text = path.read_text(encoding="utf-8")
            # Remove Markdown wrapper if present
            
            if text.strip().startswith("```json"):
                text = text.strip()
                text = text[len("```json"):].strip()
                if text.endswith("```"):
                    text = text[:-3].strip()
            
            memory = json.loads(text)
            return json.dumps(memory, indent=2)
        except Exception as e:
            return f"[Failed to parse JSON memory: {e}]"

    
    elif path.suffix == ".md":
        return path.read_text(encoding="utf-8")
    
    return "[Unsupported memory file type.]"

def build_prompt(user_input: str, memory_path: str) -> str:
    """Combines memory context with user input for final prompt."""
    memory_context = load_memory_context(memory_path)
    return f"[Memory Context]\n{memory_context}\n\n[User Input]\n{user_input}"

def query_model(full_prompt: str, model: str) -> str:
    """Sends the prompt to Text WebUI with specified model."""
    payload = {
        "model": MODEL_ROLES.get(model, MODEL_ROLES.get("default_model")),
        "messages": [{"role": "user", "content": full_prompt}],
        "temperature": 0.5,
        "max_tokens": 1024
    }
    try:
        res = requests.post(MODEL_API_URL, json=payload, timeout=60)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[Error querying model: {e}]"

# ========== GRADIO UI ==========

def process(user_input, memory_file, model_name):
    full_prompt = build_prompt(user_input, memory_file)
    response = query_model(full_prompt, model_name)
    return full_prompt, response

with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Mauricio’s Local AI Interface — WebUI Connected")

    with gr.Row():
        user_input = gr.Textbox(label="Your Input", lines=6, placeholder="Write your instruction or message...")
        
        memory_file_choices = list_memory_files()
        memory_file_choices = list_memory_files()
        default_memory_path = memory_file_choices[0][1] if memory_file_choices else ""
        memory_file = gr.Dropdown(
            choices=memory_file_choices,
            value=default_memory_path,
            label="Memory File"
)
        model_name = gr.Dropdown(choices=AVAILABLE_MODELS, value=DEFAULT_MODEL_ROLE, label="Model Role")

    submit_btn = gr.Button("Run")

    with gr.Row():
        prompt_output = gr.Textbox(label="🧾 Full Prompt", lines=10)
        model_output = gr.Textbox(label="🤖 Response", lines=10)

    submit_btn.click(fn=process, inputs=[user_input, memory_file, model_name], outputs=[prompt_output, model_output])

if __name__ == "__main__":
    demo.launch()
