from pathlib import Path

# Create the markdown content
md_content = """# 🧠 Execution Flow: Persistent AI Architecture

This document outlines the core logic and flow of the Persistent AI Architecture. It explains how structured memory files are processed through local models via command-line or GUI interfaces.

---

## 🔁 System Overview

The system is designed to simulate an emotionally intelligent memory interface by combining memory parsing, routing, and model execution. It uses local LLMs like Capybara to generate responses based on structured `.json` memory inputs.

---

## ⚙️ Full Execution Pipeline

### 1. Memory Creation
The user creates a raw memory log (`.md` or `.txt`). This is parsed into a structured `.json` file with fields like:
- `summary`
- `emotional_tone`
- `tags`
- `intensity`
- `meaning`

📄 **Example**: `vyne_core_reflection_2025-06-25.parsed.json`

---

### 2. Model Selection + Routing (CLI or GUI)
The user chooses between:
- **CLI mode**: Runs `model_router.py` with `--file` and `--prompt`
- **GUI mode**: Uses `gradio_router.py` to visually select memory files and input prompts

---

### 3. Router Logic
Model routing is configured via:
```json
{
  "sequence": [
    {
      "model": "capybara.Q6_K.gguf",
      "port": 5000
    }
  ]
}
