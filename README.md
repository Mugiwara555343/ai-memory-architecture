# Legacy-AMA (v1) — AI Memory Architecture (Archived)

[![Status: Archived](https://img.shields.io/badge/status-archived-red.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?logo=github)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-00c7c7?logo=python)
[![PyPI](https://img.shields.io/pypi/v/note-to-json?logo=pypi&label=pypi)](https://ypi.org/project/note-to-json/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Mugiwara555343)

_Local-first memory pipeline: notes → structured JSON → multi-model reflections._

---

## 📌 Why this repo exists

This is the **v1 prototype** of my AI Memory Architecture — built to process raw notes into structured memories, run them through multiple LLMs, and output enriched summaries and styled Markdown.

> **What this repo _is_:**
> - v1 prototype of the full system
> - Design docs, diagrams, and screenshots
> - Historical record of architecture & workflow
>
> **What this repo _is not_:**
> - Maintained or runnable codebase (use links below for current tools)

---

## 🚀 Where to go now

- **Parser/CLI:** [note-to-json on PyPI](https://pypi.org/project/note-to-json/)  
- **Minimal maintained demo:** [note-to-json-demo on GitHub](https://github.com/Mugiwara555343/note-to-json-demo)

---

## 🧩 Architecture at a glance

![Early Sketch](docs/images/memory_flow_diagram_dark(2).png)

Alternative early sketch:  
![Memory Flow Diagram](docs/images/memory_flow_diagram_dark.png)

---

## 📖 A Workflow storyboard

---

### ⚡Entire Model/session orchestration started
![Step 1: Model Start](docs/images/Screenshot-2025-07-12-040512.png)  
_Sessions spin up; logs show pipelines ready._

---

### ⏳ A few examples of the entire workflow

- ### Parsed file & Terminal visual
![Step 3: Terminal Run](docs/images/Screenshot-2025-06-27-232647.png)  

- ### JSON error but parser still activates
![Step 4: Gradio UI](docs/images/Screenshot-2025-06-27-23202444.png)  

- ### All three models active and parsing 
![Step 5: Prompt Injection](docs/images/Screenshot-2025-07-12-202332.png)  

---

## 🛠️ Design notes

- **Local-first & offline** — no external APIs required.
- **Composable chain** — each model has a distinct role.
- **Resilient** — pipeline continues with fallbacks on model failure.

**v1 Model Chain:**  
- **Capybara** → tagging & emotional tone extraction  
- **Hermes** → summarization  
- **MythoMax** → stylistic rewrite

---

## 🗂️ Folder map

```
docs/            # diagrams & screenshots
demo/            # stubs or prototypes
archive/         # older experiments
```

---

## 📄 License & provenance

MIT License — see [LICENSE](LICENSE).  
Development period: 2025 (v1).  
~ X commits before v2 redesign.

---

_Current repo preserved as an artifact. See linked successors for maintained tools._
