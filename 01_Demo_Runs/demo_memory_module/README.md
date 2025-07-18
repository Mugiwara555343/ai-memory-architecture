# 🧠 Memory Parser + Watcher Demo

This is a standalone demo of the **Markdown-to-JSON memory parser** and **file change watcher** used in the AI Memory architecture.

You can:
- 📝 Write or modify markdown memory logs
- ⚙️ Parse them into structured `.parsed.json` snapshots
- 👁️ Enable live file watching (auto-parse on edit)

---

## 📁 What's Included

| File                 | Role                                      |
|----------------------|-------------------------------------------|
| `memory_parser.py`   | Parses `.md` files → `.parsed.json`       |
| `memory_watcher.py`  | Watches folder for `.md` edits            |
| `run_demo.py`        | Manually run the parser on local files    |
| `demo_entry.md`      | Sample log you can edit or replace        |
| `watch_config.json`  | Declares the watched folder (`"."`)       |

---

## 📥 Step-by-Step: How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Mugiwara555343/ai-memory-architecture.git
cd your/path/chosen/ai-memory-architecture/01_Demo_Runs/demo_memory_module
```````

### 2. Manual Parse (Run Once)

```bash
python run_demo.py
```````
✅ This will convert `demo_entry.md` into demo_entry.parsed.json in the same folder.


### 3. Enable Live Watching (Auto Mode)

```bash
python memory_watcher.py
```````
Now edit `demo_entry.md` (or add a new `.md` file).
#### ✅ On save, the watcher re-runs the parser and updates/creates the corresponding `parsed.json`


## 🧪 Output Example

After parsing, you’ll see something like:

```bash
{
  "title": "Morning Reflection",
  "timestamp": "2025-07-17T20:18:21Z",
  "summary": "Today I spent time refining the AI memory watcher...",
  "tags": ["focus", "emotion", "ai"],
  "reflections": [
    "Resilience is built through iteration.",
    "System design is emotional memory made technical."
  ]
}
````


