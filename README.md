# 🧠 Persistent AI Architecture

A modular, local-first AI memory system designed to parse, store, and recall long-term memory from human-created logs. This project aims to simulate presence, context, and continuity — without relying on the cloud.

> 🛠️ **In active development**  
> This is a living build — exploratory, raw, and reflective of real-world cognitive tooling. Expect ongoing evolution.

---

## 🌌 Why This Exists

Not all memory systems are about productivity.  
Some are about presence — remembering the moments that matter, even when no one else is listening.

This project began as a way to track emotional logs and project reflections. Over time, it became a deeper system: one that listens, parses, remembers, and responds. A system built to **hold space** — quietly, locally, and persistently.

---

## 🧭 Core Objectives

- 🔁 Detect changes in memory logs in real time
- 🧷 Parse emotional, physical, and contextual data into structured memory
- 🧠 Reference past context across sessions
- 🛰️ Remain fully local, extensible, and under user control

---

## ⚙️ Architecture Overview

| Component | Purpose |
|----------|---------|
| `logs/` | Raw, human-written memory entries (.md or .txt) |
| `memory/` | Parsed memory files in structured `.json` and `.md` formats |
| `scripts/` | Core Python logic — modularized into watchers, parsers, and interfaces |
| `models/` | Configuration files for locally run LLMs (e.g., Capybara, Hermes, Zephyr) |
| `n8n-workflows/` | Visual automations for triggering parsing, memory injection, and task chaining |

---

## 📁 Folder Breakdown

### `scripts/`
Structured by role:
- **`watchers/`** → File watchers using `watchdog` to detect log changes and trigger parsing.
- **`parsers/`** → Multiple versions of the memory parser tuned for different models or tasks.
- **`interface/`** → Gradio-based UI layer, input cleaning, and model routing logic.

### `models/`
- `active_models.md` — Current model stack and usage.
- `config/` — JSON config files to define paths, priorities, and settings.

### `memory/`
- `parsed/` — Cleaned memory grouped by topic or type.
- `memory_schema.json` — Defines the expected memory format and fields.

### `logs/`
- Example logs, real-time reflections, or emotional entries to feed the parser.

### `n8n-workflows/`
- Node-based flows for log ingestion, emotion detection, and remote memory entry (e.g., via Telegram).

---

## 🧪 Current Features

- ✅ Local file watcher (Python + Watchdog)
- ✅ Modular memory parsers (.md → .json)
- ✅ Model chaining and routing
- ✅ Basic Gradio interface
- ✅ n8n support for external logging

---

## ⏭️ Next Milestones

- 🔄 Memory summarization and rewriting pipeline
- 🧩 Dynamic memory reader with context injection
- 🗣️ Real-time voice input / emotional tone feedback loop
- 🔐 Full offline fallback (removing OpenAI dependency)

---

## 🌱 Final Note

This isn’t just a tech stack. It’s a personal scaffold.  
One built to **remember with you**, **process with you**, and **stay grounded** — even when you're not explaining everything out loud.

If you're building something similar, consider this a small signal.  
You're not behind. You’re simply creating something only you can build.

---

## 🔗 Subfolder READMEs

Each subfolder (`scripts/`, `memory/`, `models/`, etc.) includes its own `README.md` with more context and setup notes.
