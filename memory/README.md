# 🧠 Memory

This folder stores raw and processed memory logs used by the assistant’s cognition system. It functions as the local memory layer for parsing, emotional tagging, and future LLM reference.

Each log—whether written manually or captured automatically—is parsed into structured JSON and Markdown, enabling modular storage, searchability, and integration with long-term memory workflows.

---

## 📁 Folder Structure

memory/
├── schema/ # Defines the structure of memory entries (e.g., JSON keys, emotional fields)
├── raw_logs/ # Unprocessed voice-to-text, emotional notes, or manual memory dumps
├── parsed/ # Output of the memory parser (structured .json + .md files)
├── markdown/ # Clean human-readable Markdown reflections or entries
├── archive/ # Older entries moved from active memory
└── memory_schema.json # Global schema reference for memory structure

---

## ✅ Active Parsed Entries

Examples of parsed memory files now available in `parsed/`:

- `2025-06-27_AI_Memory_Milestone.parsed.md`
- `2025-06-27_Debugging_Instincts.parsed.md`
- `2025-06-27_Training_Rhythm_and_Recovery.parsed.md`
- `shoulder_recovery_protocol.parsed.md`

Each parsed entry mirrors its raw or markdown origin and includes structured fields such as:

- `date`
- `title`
- `topics`
- `mood`
- `summary`
- `tags`

---

## 💾 Memory Schema

The `memory_schema.json` defines required fields and formatting for memory entries, enabling consistent parsing and downstream usage by LLMs.

You can modify this schema to evolve the assistant’s understanding over time.

---

Let me know if you'd like a sample schema file added here, or to auto-link files between folders in future steps.
