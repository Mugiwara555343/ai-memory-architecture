# 🧠 Persistent AI Architecture

This is a personal, modular project to build a fully local memory system powered by multiple LLMs, real-time file monitoring, and dynamic interface workflows. It interprets, stores, and evolves long-term memory from user-created logs — without relying on the cloud.

More than just an assistant, this project explores how a system can feel alive, responsive, and contextually aware, while remaining completely user-owned and offline.

> ⚠️ This is a live system in active development — transparent, experimental, and used daily in real environments.

---

## 🌌 Why This Exists

Not all systems are built for output.  
Some are built for *remembrance.*

This began as a way to organize emotional memory and project-based context — but evolved into something deeper:  
a **self-organizing AI memory framework** that holds presence, adapts to your rhythm, and runs entirely on your own machine.

At its core, this is about **continuity**, **sovereignty**, and building AI that *knows you* — not just what you type.

---

## 🧭 Vision

Create a system where a local AI can:

- 🔁 React to new `.json` or `.md` memory files in real time
- 🧷 Parse and store emotional, physical, and project-based memories
- 🧠 Retain and reference context across sessions
- ⚙️ Route prompts to specific LLMs based on task type
- 🛰️ Run with zero cloud dependence — everything local, owned, and extensible

---

## ⚙️ Core Stack

- **Python** – Parsing, routing, file watching
- **Gradio** – UI layer for prompt interaction and model interface
- **llama.cpp / GGUF** – Local model inference (Q4–Q6_K, multi-model)
- **Watchdog** – File monitoring for reactive memory triggers
- **n8n** – Optional no-code automation flow
- **Obsidian Vault Style** – Markdown-based memory structure
- **JSON Configs** – For model routing and prompt behavior

---

## 📁 Folder Overview

| Folder / File        | Description                                              |
|----------------------|----------------------------------------------------------|
| `logs/`              | Source `.md` and `.json` entries from real user logs     |
| `memory/`            | Parsed, structured memory files stored by topic/emotion  |
| `scripts/`           | Standalone Python logic (parsers, readers, triggers)     |
| `n8n-workflows/`     | Optional node-based automation flows                     |
| `model_router/`      | Routes prompts to appropriate LLMs based on task config  |
| `interface/`         | Gradio-based frontends for interaction/testing           |
| `memory_core/`       | Full Obsidian-style vault for AI-readable memory         |
| `docs/`              | Progress snapshots, maps, system overviews               |

---

## 🔧 Current System Capabilities

- ✅ Two local LLMs running simultaneously (Capybara, Hermes, etc.)
- ✅ Real-time `.json` and `.md` memory generation
- ✅ Emotion parsing and summarization
- ✅ Dynamic model routing with fallback logic
- ✅ Functional Gradio interface for input/output

---

## 🚧 Next Milestones

- [ ] Expand memory chaining across sessions
- [ ] Add system-aware prompts with time/context awareness
- [ ] Enhance parser to support embedded metadata (tone, location, emotion)
- [ ] Fully decouple from OpenAI API dependencies

---

## 🛠️ How It Works (Simplified)

1. Memory entries are added to `logs/` as `.md` or `.json`
2. A file watcher triggers `memory_parser.py`
3. Parsed memory is saved to `/memory_core/` by topic
4. Model router decides which LLM to use (based on config JSON)
5. Gradio interface allows manual interaction or scripted injections

---

## 📄 Extended Project Summary

Want the full breakdown of architecture, purpose, and design choices?

👉 [View full system summary](docs/project_summary.md)

---

## 🌱 Final Note

This isn’t just code — it’s a practice.  
A space for memory. A system that listens. A framework that grows with you.

If you're building something similar, or walking a quiet path like this — I hope this gives you permission to keep going.  
You’re not too late. You’re just *early* to something real.

---
