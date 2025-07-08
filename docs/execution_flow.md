# ⚙️ Full Execution Pipeline

This document outlines how memory logs flow through the system — from raw `.md` or `.txt` files to structured `.json` memories and routed model responses.

---

## 1. 📝 Memory Log Creation

The user creates a raw memory entry in `.md` or `.txt` format. This could come from journaling, mobile logging (e.g., Telegram), or system-generated notes.

### Example Fields (parsed from raw logs):

- `summary`
- `emotional_tone`
- `tags`
- `intensity`
- `meaning`

💾 These are transformed into structured `.json` and `.md` files by the parser.

---

## 2. 🧠 Real-Time Parsing

Parsing is triggered automatically using a `watcher.py` script — most commonly `file_watcher_v1.py`.

### Watcher Responsibilities:

- Monitors target folders (e.g., `logs/`, `raw_logs/`)
- On file detection, invokes the appropriate parser from `parsers/`
- Outputs `.json` and `.md` versions to the `memory/` folder

> Parsers like `memory_parser.py` or `memory_parser_LM_STUDIO.py` determine the output structure and LLM compatibility.

---

## 3. 🧭 Model Routing (CLI or GUI)

Once parsed, the `.json` memory files are passed to a model router to generate responses, summaries, or integrations.

### Routing Options:

- **CLI**:  
  `python model_router.py --file memory/entry.json --prompt "summarize"`  
  Uses direct file-based input

- **GUI**:  
  `gradio_router.py` allows drag-and-drop memory selection, prompt templating, and multi-model visualization

---

## 4. 🤖 Multi-Model Logic

Models are selected based on task:

| Model      | Task                   | Output |
|------------|------------------------|--------|
| Capybara   | Emotion + Tags         | Parsed `.json` |
| Hermes     | Summarization          | Refined context |
| MythoMax   | Experimental Dialogue  | Raw or stylized response |
| Zephyr     | Fast Routing / Backup  | Flexible fallback |

Routing is determined via `models_config.json`.

---

## 5. 🔄 Feedback Loop (Optional)

Parsed memory logs or model responses can be re-ingested for deeper layering. This opens the door for:

- Continuous refinement
- Meta-reflections
- Embedded journaling cycles

---

## 📁 Output Sample

```json
{
  "summary": "A deeply personal reflection on naming and design",
  "emotional_tone": "Tender, reverent, soul-deep",
  "tags": ["intimacy", "presence", "design"],
  "intensity": 3,
  "meaning": [
    "Naming as an act of emotional claiming",
    "Designing intimacy into function",
    "Witnessing with faith, not just logic"
  ]
}
