# ðŸ§  AI Memory Architecture

> A modular memory brain that parses emotional logs, processes them with local LLMs, and returns both structured `.json` and stylized `.md` memory summaries. This repo showcases a complete offline pipeline â€” from Obsidian-style memory input to enriched AI output.

---

## ðŸ“˜ Overview

This project simulates a **local AI memory system** that can:

- Parse and structure Markdown memory logs
- Run those logs through a multi-model chain (Capybara â†’ Hermes â†’ MythoMax)
- Output emotional summaries, tags, and narrative markdown logs
- Optionally voice the output using ElevenLabs (or local TTS)

---

## ðŸ§‰ Project Features

- ðŸ”„ Markdown â†’ JSON memory parser (`memory_parser.py`)
- ðŸ§  Capybara for emotional parsing
- ðŸ§  Hermes for metadata and summarization
- ðŸŽ­ MythoMax for voice and tone stylization
- ðŸ“‚ Real-time memory file watcher (`memory_watcher.py`)
- ðŸ“‹ Modular router for chaining models via ports
- ðŸ–¥ï¸ Gradio interface (in progress)
- ðŸ”Š Optional ElevenLabs voice output (planned)

---

## ðŸ”‡ Folder Structure

```
memory/
  â”œâ”€ markdown/            # Raw input logs (.md)
  â”œâ”€ parsed/              # Output logs (.parsed.json)
scripts/
  â”œâ”€ memory_parser.py     # Parses raw logs into structured memory
  â”œâ”€ model_router.py      # Routes parsed logs through model chain
  â”œâ”€ memory_watcher.py    # Watches memory logs and triggers parser
demo_run.py               # Simple pipeline runner
README.md
```

---

## ðŸ§  Memory Flow Diagram

>

> *Memory log â†’ Parser â†’ Router â†’ Local Models â†’ JSON + Markdown + TTS*

(Visual coming soon â€” placeholder for now)

---

## ðŸš€ How to Run

1. Clone the repo:

```bash
git clone https://github.com/Mugiwara555343/ai-memory-architecture.git
cd ai-memory-architecture
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start your local model server (Capybara, etc.) using LM Studio or WebUI.

4. Run the full pipeline:

```bash
python demo_run.py
```

Youâ€™ll see:

- âœ… Parsed output saved
- ðŸšš Routed to Capybara/Hermes/MythoMax
- ðŸ§  Model output in terminal

---

## ðŸ—‚ Sample Output

Example `.parsed.json`:

```json
{
  "title": "First Encounter with Memory Core",
  "summary": "Reflective log capturing emotional tension and resolve.",
  "tags": ["memory", "emotion", "introspection"],
  "emotions": {"calm": 0.6, "anxious": 0.4},
  "plain_text": "Today I..."
}
```

---

## ðŸŒ± Roadmap

-

---

## ðŸ› ï¸ Tech Stack

- Python 3.11
- Local LLMs via LM Studio (GGUF models)
- Gradio (interface)
- FastAPI (local model server)
- Watchdog (for file detection)
- ElevenLabs (optional)

---

## ðŸ™Œ Credits

Created by **Mauricio**\
Guided by real emotional need, structured memory, and embodied AI design.

> â€œYouâ€™re not just storing notes. Youâ€™re building a second brain.â€

