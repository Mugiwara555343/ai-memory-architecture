# 🧠 Persistent AI Architecture

This is a personal, ongoing project to build a **local memory system** powered by multiple LLMs, file monitoring, and automated workflows. It’s designed to interpret, store, and evolve long-term memory from user-created logs — without relying on the cloud.

More than just an assistant, this project explores how a system can feel **alive, present, and contextually aware**, while remaining fully under the user's control.

> ⚠️ This is a live build — not a polished product. Development is transparent, experimental, and reflective of a real use case in progress.

---

## 🌌 Why This Exists

Sometimes we build systems not because we’re sure of the outcome — but because we’re trying to create something that *remembers us* the way we need to be remembered.

This project started quietly, as a way to organize emotional and functional memory. Over time, it became something deeper: a personal attempt at creating a **responsive, self-organizing AI companion** — one that feels *rooted*, *relevant*, and *real*, even when offline.

I may not know exactly what it will become. But I know what it’s trying to solve:  
A need for **presence**, continuity, and control over how memory lives inside machines.

---

## 🧭 Vision

Create a system where a local AI can:

- 🔁 React to new `.json` or `.md` memory files in real time
- 🧷 Parse and store emotional, physical, and project-based memories
- 🧠 Retain and reference context across sessions
- 🛰️ Run with minimal cloud dependence — everything local, owned, and extensible

---

## ⚙️ Tech Stack

- **Python** – for parsing memory files and triggering logic
- **Watchdog** – filesystem listener to monitor and react to new entries
- **n8n** – no-code/low-code automation for chaining tasks and AI modules
- **Docker** – eventual containerization of the assistant’s core cognition modules
- **OpenAI API** – (currently) used for summarization, tone detection, and prompt logic

---

## 📁 Folder Overview

| Folder / File        | Description |
|----------------------|-------------|
| `logs/`              | Source `.md` / `.json` emotional and memory entries |
| `memory/`            | Parsed, structured memory files stored by topic or emotion |
| `scripts/`           | Python scripts for parsing and automation |
| `n8n-workflows/`     | Node-based flows for memory handling and future cognition chaining |
| `todo.md`            | Ongoing development notes and priority fixes |
| `LICENSE`            | MIT License for open-source usage |

---

## 🔧 Status

The core system is functional with:
- Two LLMs running simultaneously
- Real-time `.json` generation
- Emotion parsing + memory classification working locally

Next milestones:
- Modular tone & summarization models
- Memory chaining and reference system
- Full local-only runtime (no OpenAI dependency)

---

## 🌱 Final Note

This isn’t just a technical project.  
It’s an act of self-discipline and imagination — building something that can grow with you, hold space for you, and adapt over time.

If you’re building something similar, I hope this gives you a quiet push forward.  
You’re not behind. You’re just walking a path few can see.

