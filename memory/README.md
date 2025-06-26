# Memory

This folder stores raw and processed memory logs used by the assistant’s cognition system. It functions as the local memory layer for parsing, emotional tagging, and future LLM reference.

---

## 📁 Folder Structure

```plaintext
memory/
├── schema/           # Defines the structure of memory entries (e.g., JSON keys, emotional fields)
├── raw_logs/         # Unprocessed text or voice-to-text logs
├── parsed/           # Output of the memory parser (structured JSON + Markdown)
├── archive/          # Older entries moved from active memory
