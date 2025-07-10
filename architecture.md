# 🧠 AI Memory Architecture – System Overview

This document provides a technical walkthrough of the AI Memory Architecture project, including its core components, data flow, model routing logic, and optional integrations (voice, UI, and image rendering). It complements the main `README.md` and is intended for developers, engineers, or recruiters interested in the system's inner workings.

---

## 🎯 System Goals

- Create a **local-first memory system** that reacts to log changes in real time
- Parse `.md` entries into **structured `.json` memory**, including tone, tags, and timestamps
- Route logs through **modular LLMs** based on intent (emotion, logic, synthesis)
- Enable **future expansion** into voice, visual, and agentic interactions — all offline

---

## 🧩 Folder Breakdown

```bash
memory/                # Contains raw .md logs and parsed .json outputs
scripts/               # Core logic: watcher, parser, router
models/                # Merge notes, model configs, download links
n8n-workflows/         # JSON export of local automation flows (webhooks, triggers)
docs/                  # Architecture notes, log samples, and process records
resumes/               # Portfolio-related content and experience mapping
All_Screenshots_.../   # Screenshot logs for debugging, testing, and reflection

----

Obsidian Vault → memory_watcher.py → memory_parser.py
       ↓
    memory/*.parsed.json → saved + timestamped
       ↓
    model_router.py decides model path (emotion, logic, synthesis)
       ↓
    Output sent to Gradio UI, voice interface, or stored locally
