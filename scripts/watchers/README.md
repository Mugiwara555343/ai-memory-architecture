# 👁️ File Watchers

This folder contains scripts that monitor file systems for real-time changes — such as new or updated memory logs — and automatically invoke the appropriate parser.

These watchers make the entire memory architecture **reactive**. Rather than requiring manual execution, the system listens and responds as new input appears.

---

## ⚙️ Included Scripts

- **`file_watcher_v1.py`**  
  Initial prototype using `watchdog`. Monitors hardcoded paths and invokes the parser on file updates.

- **`memory_watcher.py`, `memory_watcher_fixed.py`, `memory_watcher_updated.py`**  
  Evolved versions supporting improved directory structure, error handling, and flexible path configs. Versions can be swapped based on system needs or performance.

---

## 🌱 Future Additions

- Config-based watcher setup using `.env` or `config.json`  
- Debounced detection to avoid repeated triggers  
- Log display or alerts when parsing completes  
- Auto-cleaning or archiving of parsed files post-processing
