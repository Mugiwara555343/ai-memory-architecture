# 🛠️ All Parser Troubleshoot

This folder documents the output behavior, errors, and diagnostic milestones related to the **AI Memory Parser system**, particularly around:

- Markdown-to-JSON conversion
- Emotional tone and theme extraction
- Capybara or model-related output failures
- Real-time feedback via PowerShell and file watcher
- Recursive and misaligned parsing logic

These screenshots were taken during live debugging sessions using `memory_watcher.py` and `memory_parser.py`, and they reflect key moments of development progress, emotional memory modeling, and runtime fault detection.

---

## 🔍 Core Troubleshooting Snapshots

### 1️⃣ Capybara JSON Error — Model Failure Caught by Watcher

![Capybara JSON error](./Screenshot-2025-06-27-232024444.png)

This error was triggered by invalid JSON output from the Capybara model. The parser detected malformed formatting and wrote an error block to `.parsed.json`, preserving the raw response for later debugging. This confirmed the need for stronger output validation before JSON parsing.

---

### 2️⃣ Debugging Instincts — Emotional Pattern Parsing

![Debugging Instincts JSON](./Screenshot-2025-06-27-232844.png)

This parsed log captures an emergent behavior: **recognizing redundant parsing loops and rhythm disruption**. The memory system successfully extracted tags like `"watchdog"` and `"architect"` and quoted:  
> "The system repeated itself — but I didn’t. I noticed, I adapted, and I moved forward cleaner."

---

### 3️⃣ Rhythmic Recovery — Full Parse of Reflective Log

![Training Rhythm + Recovery JSON](./Screenshot-2025-06-27-233954.png)

A detailed example of a **clean parse cycle**. The entry reflects on recovery, training, and embodied insight. Emotional tone, tags, and quotes were successfully injected into `.parsed.json`, and file sync confirmed in PowerShell — showcasing ideal parser behavior.

---

## 🗃️ Additional Reference Screenshots

| Filename | Description |
|----------|-------------|
| `Screenshot-2025-06-28-010234.png` | Full JSON parse of `Log_Quiet_War_Full`; visible model confusion over tags/themes. |
| `Screenshot-2025-06-27-233000.png` | Successful parse of `Coherence_Reached.md` with repeating watcher events (possible loop). |
| `Screenshot-2025-06-27-233845.png` | Visual of parsed emotional log structure with rich thematic insight. |
| `Screenshot-2025-07-17-010411.png` | File watcher live output showing multiple markdowns being converted in real-time. |
| `Screenshot-2025-07-17-010506.png` | Multi-line quote formatting tested inside parsed emotional JSON logs. |
| `Screenshot-2025-07-17-010542.png` | Layered logs parsed in sequence — multiple `.parsed.json` generations visible. |
| `Screenshot-2025-07-17-011108.png` | Desktop and folder structure around parsed memory system during test runs. |

> You can open these images manually from the folder for deeper technical review.

---

## 🔗 System Context

These screenshots are tied to:

- `memory_parser.py` — Converts `.md` entries into emotional `.json` logs
- `memory_watcher.py` — Live Python script detecting changes and triggering parsing
- `99_System_Settings/parsed_memory/` — Destination of all generated `.parsed.*` files

---

> _Maintained as part of the [AI Memory Architecture](https://github.com/Mugiwara555343/ai-memory-architecture) project. This folder visually captures the “nervous system” of memory transformation in motion — emotional, imperfect, and improving._

