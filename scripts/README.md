# 🧩 Scripts – Memory Core Modules

This folder houses all core automation scripts used in the persistent AI memory system. These scripts are organized into modular subfolders by function — interface, parsing, and file watching — to keep the architecture clean and extensible.

## 🗂️ Subfolders

### 📡 [`interface/`](./interface)
Scripts that handle the user interface and model routing logic. Includes Gradio frontends, model selectors, and wrappers for streamlining I/O between models and memory modules.

### 🧠 [`parsers/`](./parsers)
All memory parser scripts — each one transforms raw logs into structured `.json` and `.md` formats. Supports multi-model parsing, emotion tagging, summarization, and custom token formatting.

### 🕊️ [`watchers/`](./watchers)
Real-time filesystem listeners that detect changes in memory or log folders. Automatically trigger the appropriate parser when new content is added or edited.

---

## 📍 How It Connects

1. **User writes a log** → saved to `logs/`
2. **Watcher** detects the file and triggers a **parser**
3. **Parser** creates structured `.json` and `.md` files in `memory/`
4. **Interface** uses these to inject context into live AI interactions

---

## 🛠️ Notes

- Each folder contains its own README with deeper details
- Multiple versions are stored to allow testing different routing setups
- Future plans incl
