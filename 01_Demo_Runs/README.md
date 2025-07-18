# 🧪 AMA – Demo Modules

This folder contains standalone demos and test modules pulled from the full AI Memory system.

Each module here is designed to be self-contained — you can clone, test, and explore individual components without running the full stack.

---

## ✅ Currently Available

### 📂 `demo_memory_module/`

A working demo of the **Markdown-to-JSON memory parser** and **file watcher**:
- Parse `.md` logs into `.parsed.json`
- Auto-trigger parsing on file changes
- Based on the core `memory_parser.py` and `memory_watcher.py` from the system

---

## 🛠️ Coming Soon

Planned modules for future releases:
- `llm_router_demo/`: Route prompts across local model servers
- `emotion_extractor_demo/`: Summarize memory logs into emotion-tagged JSON
- `fastapi_model_runner/`: API endpoint version of chain execution
- `gpu_selector_demo/`: GPU-aware model inference preview

---

To run any demo, open that subfolder and follow its README.

🧠 The goal: let users explore individual parts of the memory engine without full orchestration.

