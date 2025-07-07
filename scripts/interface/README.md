# Interface Scripts

This folder contains the components responsible for the local user interface and model routing logic. These scripts allow you to interact with your AI system in real time, define how the frontend connects to the backend memory core, and manage which models respond to different tasks.

### ✨ Included Scripts

- `interface.py`  
  Main UI logic (currently powered by Gradio) that bridges the user and memory system.

- `gradio_router.py`  
  Manages model routing logic within the Gradio interface, allowing dynamic switching between local LLMs based on user needs or task type.

- `clean_json_wrappers.py`  
  Utility script for preprocessing `.json` logs and stripping unwanted formatting or inconsistencies before parsing.

- `model_config.json`  
  A structured config file listing available models, their roles (e.g., summarizer, tone parser), and paths to trigger logic across different system modules.

---

### 🧠 Purpose

This module is the surface of your AI — it defines how you engage with your assistant and which cognitive modules respond. It ensures that interaction remains intuitive, modular, and swappable across models or UI frameworks.

---

### 🔧 Future Additions

- WebSocket or voice interface support  
- More advanced UI layouts (tabs, memory explorers, log uploaders)  
- Live token usage monitoring for each model
