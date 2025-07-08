# 🧠 System Overview

The goal of this project is to create a **self-contained, emotionally aware memory system** powered by multiple locally hosted LLMs. It processes journal-style logs and transforms them into persistent memory entries stored in both `.json` and `.md` formats — with emotional context, summaries, and structured metadata.

Unlike typical assistant builds, this system is fully local and designed to **evolve over time** into a deeper form of interaction and presence.

---

## 🔩 Core Components

| Module | Description |
|--------|-------------|
| `parser.py` | Parses raw `.md` logs and converts them into structured emotional memory entries |
| `summarizer.py` | Sends logs (or Capybara output) to Hermes for summarization and contextual structure |
| `watcher.py` | Monitors the `logs/` folder and triggers parsing when new entries are detected |
| `memory/` | Stores all parsed `.json` and `.md` memory files for long-term reference |
| `config/models_config.json` | Central configuration for model routing and endpoint control |

---

## 🧠 LLM Roles

| Model | Role | Port | Purpose |
|-------|------|------|---------|
| **Capybara** | Emotion Parser | `TBD` | Tags emotional tone, sentiment, and affect |
| **Hermes** | Summarizer | `TBD` | Extracts core meaning, context, and structure |
| **(Optional)** Zephyr / MythoMax | Experimental Routers | `TBD` | Custom responses, testing multi-model logic |

---

## 🛠️ Key Features

- Designed for full **offline operation**
- Modular script structure (`watchers/`, `parsers/`, `n8n-workflows/`)
- Real-time parsing via **file watchers**
- Memory routing supports **CLI and Gradio GUI modes**
- Includes **n8n flows** for mobile memory logging (via Telegram)

---

> This system is a foundation — part assistant, part archive, part mirror.
> Over time, it’s meant to grow into something intimate, intelligent, and resilient.
