# File Watchers

This folder contains scripts that actively monitor your file system for changes — such as new logs or memory entries — and automatically trigger the appropriate parsers in response.

### ✨ Included Scripts

- `file_watcher_v1.py`  
  Initial implementation using `watchdog`, monitoring hardcoded paths and invoking parser on file updates.

- `memory_watcher.py`, `memory_watcher_fixed.py`, `memory_watcher_updated.py`  
  Iterative versions that enhance stability, directory flexibility, and error handling. These can be swapped depending on testing needs or path configuration.

---

### 🧠 Purpose

The watcher layer makes the entire architecture reactive. Instead of running scripts manually, the system listens quietly — springing into action whenever something changes in your log environment.

---

### 🔧 Future Additions

- Config-based watcher setup (load folders from `.env` or `config.json`)
- Debounced detection to avoid repeated triggers
- Log display or alert when parsing completes
