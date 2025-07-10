# 🧠 Architecture Overview – AI Memory System

This document outlines the architecture behind the **AI Memory Architecture** project — a modular, local-first system designed for cognitive reflection, emotional processing, and long-term memory simulation using multi-model LLM chaining.

The system is structured to scale across multiple interfaces, models, and sensory layers (voice, image, text), while remaining fully local, extensible, and privacy-preserving.

---

## ⚙️ System Goals

- Process human-readable `.md` logs into structured memory files (`.json`)
- Parse emotional tone, intensity, and tags from daily reflections
- Route memory logs to appropriate local models (emotion, logic, synthesis)
- Enable real-time interaction via voice (Whisper + ElevenLabs)
- Visualize logs through future scene renderers (ComfyUI)
- Maintain a fully offline, scriptable, and modular stack

---

## 📁 Folder Roles

| Folder                  | Purpose |
|------------------------|---------|
| `memory/`              | Raw and parsed logs, including structured `.json` memory files |
| `scripts/`             | Core Python tools: watcher, parser, model router |
| `models/`              | Model metadata, merge plans, config notes |
| `n8n-workflows/`       | Webhook triggers, local agent task flows, and automation |
| `docs/`                | Architecture notes, sample logs, reflections |
| `resumes/`             | Professional profile documents |
| `All_Screenshots_Of_Troubleshooting/` | Categorized debugging gallery with implementation proof |

---

## 🧩 System Pipeline (Flow)

```text
Markdown Logs (.md)
       ↓
memory_watcher.py
       ↓
memory_parser.py
→ Parses title, tags, emotion, tone, summary
→ Outputs clean .parsed.json file with timestamp + metadata
       ↓
model_router.py
→ Capybara (emotional), Hermes (logical), MythoMax (synthesis)
→ Future integration: DantesPeak-36B, Janus-MOE, Mythical-LMs
       ↓
Local Model Output
→ Gradio UI (text), ElevenLabs (voice), ComfyUI (visual)
