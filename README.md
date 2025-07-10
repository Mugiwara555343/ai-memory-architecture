# 🧠 AI Memory Architecture

A **local-first AI memory system** designed for modular LLM cognition, long-term context retention, and emotional continuity.

This project combines real-time file parsing, model chaining, and structured memory ingestion to simulate an evolving internal companion — one that listens, remembers, and reflects.  
Built using tools like `n8n`, `Gradio`, `LLM Studio`, and `OpenAI`, this system is part automation lab, part cognitive forge.

> **Status:** Actively evolving. This is a living build — part tool, part vision, part personal AI core.

---

## 🔍 Purpose

This isn’t just about productivity or notes.  
This is about **presence** — building an offline AI memory system that holds space for your thoughts, moods, and breakthroughs.

Originally created to track daily reflections, the project grew into a **modular architecture** for parsing, storing, and responding to memory logs — through local models, dynamic UIs, and multi-format synthesis.

---

## 🧱 Core Features

- 🕰️ **Real-time memory detection**  
  Auto-watches `.md` files across folders and logs updates with timestamps

- 🧠 **Emotion + context parsing**  
  Converts markdown entries into structured `.json` memory with tags, tone, intensity, and source

- 🧵 **Multi-model routing**  
  Routes logs to local models (Capybara, Hermes, MythoMax) based on intent — emotion, logic, or synthesis

- 🗣️ **Interface ready**  
  Integrated with Gradio UI, Whisper STT, and ElevenLabs for future voice control and memory dialogue

- 🌐 **n8n automation**  
  Handles webhook logic, model triggers, and future local agent tasking

---

## 🧩 Project Structure

```bash
ai-memory-architecture/
├── memory/               # Raw + parsed logs (.md → .json)
├── scripts/              # Core scripts (parser, watcher, router)
├── models/               # Model references, plans, and merge info
├── n8n-workflows/        # Webhook + agent workflows
├── All_Screenshots_Of_Troubleshooting/
├── docs/                 # Log samples, architecture notes
├── resumes/              # Career notes / portfolio links
├── README.md             # You're here
