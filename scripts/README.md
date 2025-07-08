# 🧩 Interface Scripts

This folder contains the components responsible for the local user interface and model routing logic. These scripts allow real-time interaction with the memory system via a Gradio UI, managing how user inputs are processed and routed to different local LLMs.

These tools enable dynamic prompt workflows — adapting to the user’s intent, memory context, and model capabilities.

---

## ✨ Included Scripts

- **`interface.py`**  
  Primary frontend controller — integrates Gradio with the memory parser and model router. Handles user interaction, input preprocessing, and feedback display.

- **`gradio_router.py`**  
  Modular router for switching between LLMs based on task type (e.g., summarization, emotional tone parsing, memory analysis). Built for flexible task delegation.

- **`clean_json_wrappers.py`**  
  Preprocessing utility that sanitizes `.json` memory logs before reinjection. Strips extra formatting or corrupted tokens.

- **`model_config.json`**  
  Schema defining available LLMs, prompt types, system roles, and execution paths. Used to coordinate task assignment and runtime flow between components.

---

## 🧠 Why This Matters

The interface layer bridges human input with model cognition.  
It creates a foundation for prompt chaining, context-aware memory recall, and local execution — without cloud dependency.

This setup is foundational to building a *personalized cognitive assistant* that evolves through interaction.

---

