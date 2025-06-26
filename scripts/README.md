# Scripts

This folder contains the Python automation scripts that power the core functionality of the persistent AI memory system. Each script is modular, testable, and built to run locally for privacy and reliability.

---

## 🧠 Included Scripts

### 🔁 `file_watcher_v1.py`
Watches specified folders (like memory logs or emotional notes) for file changes (creation/modification).  
On change, it triggers the memory parser script to update structured `.json` and `.md` logs automatically.

**Key Features:**
- Real-time detection with watchdog
- Customizable target directories
- Integrates with your parser module

---

## 🔧 Dependencies

Make sure to install the required libraries:
```bash
pip install watchdog
