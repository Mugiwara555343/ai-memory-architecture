# persistent-ai-architecture

A personal lab for building a persistent AI memory system using local files, n8n automations, Docker containers, and OpenAI’s GPT models. This repository tracks the ongoing structure, development, and logic behind a custom assistant designed to interpret, organize, and respond to long-term memory stored on-device.

This is an active build—not a finished product. Logs and tasks are documented transparently.

---

## 🧠 Vision

To create a system where a local assistant can:
- React to new `.json` or `.md` memory files in real time
- Parse and organize emotional, physical, and project-based memories
- Use context intelligently and persistently across sessions
- Eventually run with minimal cloud dependence

---

## 🧱 Tech Stack

- **Python** – scripts for file monitoring and memory parsing
- **Watchdog** – filesystem listener for triggering events
- **n8n** – low-code automation platform for task routing
- **Docker** – containerization of assistant memory modules
- **OpenAI API** – GPT for summarization, tone analysis, and prompt injection

---

## 📁 Folder Structure

