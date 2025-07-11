# 🧠 AI Memory Architecture

> A modular memory brain that parses emotional logs, processes them with local LLMs, and returns both structured `.json` and stylized `.md` memory summaries. This repo showcases a complete offline pipeline — from Obsidian-style memory input to enriched AI output.

---

## 📘 Overview

This project simulates a **local AI memory system** that can:

* Parse and structure Markdown memory logs
* Run those logs through a multi-model chain (Capybara → Hermes → MythoMax)
* Output emotional summaries, tags, and narrative markdown logs
* Optionally voice the output using ElevenLabs (or local TTS)

---

## 🧠 Memory Flow Diagram

A visual overview of the full local-first memory architecture — from markdown log ingestion to multi-model enrichment and semantic retrieval.

![Memory Architecture Diagram](./memory_flow_diagram_dark.png) (./memory_flow_diagram_dark.png)

---

## 🧉 Project Features

* 🔄 Markdown → JSON memory parser (`memory_parser.py`)
* 🧠 Capybara for emotional parsing
* 🧠 Hermes for metadata and summarization
* 🎭 MythoMax for voice and tone stylization
* 📂 Real-time memory file watcher (`memory_watcher.py`)
* 📋 Modular router for chaining models via ports
* 🖥️ Gradio interface (in progress)
* 🔊 Optional ElevenLabs voice output (planned)

---

## 🔇 Folder Structure

```
memory/
  ├─ markdown/            # Raw input logs (.md)
  ├─ parsed/              # Output logs (.parsed.json)
scripts/
  ├─ memory_parser.py     # Parses raw logs into structured memory
  ├─ model_router.py      # Routes parsed logs through model chain
  ├─ memory_watcher.py    # Watches memory logs and triggers parser
demo_run.py               # Simple pipeline runner
README.md
```

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/Mugiwara555343/ai-memory-architecture.git
cd ai-memory-architecture
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start your local model server (Capybara, etc.) using LM Studio or WebUI.

4. Run the full pipeline:

```bash
python demo_run.py
```

You’ll see:

* ✅ Parsed output saved
* 🚚 Routed to Capybara/Hermes/MythoMax
* 🧠 Model output in terminal

---

## 🗂 Sample Output

Example `.parsed.json`:

```json
{
  "title": "First Encounter with Memory Core",
  "summary": "Reflective log capturing emotional tension and resolve.",
  "tags": ["memory", "emotion", "introspection"],
  "emotions": {"calm": 0.6, "anxious": 0.4},
  "plain_text": "Today I..."
}
```

---

## 🌱 Roadmap

*

---

## 🛠️ Tech Stack

* Python 3.11
* Local LLMs via LM Studio (GGUF models)
* Gradio (interface)
* FastAPI (local model server)
* Watchdog (for file detection)
* ElevenLabs (optional)

---

## 🙌 Credits

Created by **Mauricio**

> “You’re not just storing notes. You’re building a second brain.”
