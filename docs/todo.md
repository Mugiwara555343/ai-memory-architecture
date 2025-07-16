# TODO – persistent-ai-architecture

A living checklist of tasks, milestones, and architectural ideas for building a persistent AI memory system using n8n, Docker, and OpenAI.

---

## ✅ Completed
- [x] Initialized GitHub repository
- [x] Created folder structure: `/scripts`, `/memory`, `/logs`
- [x] Added `README.md` and project description
- [x] Wrote and committed initial file watcher using Python + watchdog
- [x] Added placeholder `memory_schema.json`
- [x] Logged initial setup progress

---

## 🔄 In Progress
- [x] Define memory schema in detail: required fields, validation rules
- [x] Begin parser module for `.json` and `.md` logs
- [x] Draft file change event → parsing → action pipeline
- [ ] Outline companion assistant’s role in memory consumption and usage

---

## 🧠 Ideas & Notes
- Memory types: emotional log, training log, project update
- Use Obsidian for local memory writing, synced via watcher
- Optional webhook to notify local LLM when new memory is added
- Memory scoring/ranking system for assistant prioritization
