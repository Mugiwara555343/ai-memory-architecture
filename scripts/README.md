# 🧠 Script Modules – Core Memory Automation

This folder contains the core Python automation scripts powering the persistent AI memory system. Each script is modular, testable, and structured for local execution — ensuring privacy, reliability, and full system control.

These scripts handle real-time file watching, parsing, and memory log generation, forming the backend of a local LLM-powered architecture.

---

## 📜 Included Scripts

| Script | Description |
|--------|-------------|
| `memory_parser.py` | Core parser for raw `.md` logs → structured `.json` and cleaned `.md` memory entries. |
| `memory_parser_v1_full.py` | Experimental full-version parser with expanded tagging and metadata handling. |
| `memory_watcher.py` | Original file watcher script using Watchdog to detect file changes and trigger parsing. |
| `memory_watcher_fixed.py` | A more stable watcher variant with improved error handling and directory targeting. |
| `memory_watcher_updated.py` | Current iteration of the watcher — actively maintained and integrated with the latest parser. |
| `file_watcher_v1.py` | Legacy version; simple one-directory listener for quick prototyping. |

---

## 🔧 Dependencies

Make sure to install these required libraries before running any scripts:

```bash
pip install watchdog
