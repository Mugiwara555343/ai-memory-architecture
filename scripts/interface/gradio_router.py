import gradio as gr
import json
import sys
from pathlib import Path

# Add project root so model_router becomes importable
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

# Import router function
from model_router.model_router import query_model

# ===== CONFIG =====
MEMORY_DIR = Path(__file__).parents[1] / "memory_core" / "99_System_Settings" / "parsed_memory" / "vault_json"
SEQUENCE_FILE = Path(__file__).parents[1] / "model_router" / "router_sequence.json"


# ===== HELPERS =====
def list_memory_files(extensions=(".json", ".md")):
    files = []
    for ext in extensions:
        files.extend(MEMORY_DIR.glob(f"*{ext}"))
    return sorted([f.name for f in files])


def load_memory_text(file_path: str) -> str:
    path = Path(file_path)
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("```json"):
        lines = text.splitlines()
        text = "\n".join(lines[1:-1]).strip()
    return text


def load_sequence():
    with open(SEQUENCE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["sequence"]


# ===== MAIN FUNCTION =====
def run_model_chain(memory_file, user_prompt):
    memory_path = MEMORY_DIR / memory_file
    memory_text = load_memory_text(memory_path)

    # Load routing config and grab capybara (first model for now)
    sequence = load_sequence()
    first = sequence[0]
    model_name = first["model"]
    port = first["port"]

    full_prompt = f"[Memory Context]\n{memory_text}\n\n[User Input]\n{user_prompt}"
    result = query_model(full_prompt, model_name, port)
    return result


# ===== GRADIO UI =====
def launch_ui():
    with gr.Blocks(title="AI Memory Router") as demo:
        gr.Markdown("🧠 **AI Memory Router – Gradio Interface**")

        with gr.Row():
            file_dropdown = gr.Dropdown(choices=list_memory_files(), label="Memory File")
            user_input = gr.Textbox(label="Instruction", placeholder="What do you want the assistant to do?")

        output_box = gr.Textbox(label="Full Output", lines=15)

        run_button = gr.Button("Run Model Chain")

        run_button.click(fn=run_model_chain, inputs=[file_dropdown, user_input], outputs=output_box)

    demo.launch()


# ===== RUN =====
if __name__ == "__main__":
    launch_ui()
