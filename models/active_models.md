# 🧠 Active Local Models

This system currently uses two locally-hosted language models via [LM Studio](https://lmstudio.ai/) to simulate core cognition modules: **emotional parsing** and **contextual summarization**.

These models are used in tandem — each performing a unique cognitive task that contributes to building a persistent, emotionally aware memory system.

---

## 🦊 Capybara – Emotion Parser

- **Quantized Model:** `capybara-7b.gguf`
- **Function:** Parses `.md` and `.json` logs for emotional tone, sentiment, and affective cues
- **Used in:** `parser.py`, `memory_pipeline.py`
- **Running via:** LM Studio

Capybara acts as the **emotional nervous system** — tagging entries with emotional states that help shape tone, priority, and context memory.

---

## 🔱 Hermes – Summarization & Context Enrichment

- **Model:** `hermes-2-pro-mistral-7b.gguf`
- **Function:** Performs summarization, memory tagging, and structured metadata enrichment
- **Used in:** `watcher.py`, `summarizer.py`
- **Running via:** LM Studio (`127.0.0.1:1234`)

Hermes functions as the **analytical cortex**, translating raw input into structured long-term memory suitable for search, chaining, and self-referencing.

---

## 🔭 Future Model Plans

| Model | Purpose |
|-------|---------|
| **MythoMax / Mixtral** | Large-context summarization, extended token memory |
| **Persona/Tone Modulator** | A future model for shaping assistant voice, adapting tone dynamically |
| **Embedding Model (e.g., E5, MiniLM)** | For searchability, vector tagging, and memory recall |

---

## 🌱 Notes

Models are run locally to preserve privacy, increase response control, and remove reliance on external APIs.  
All integration is modular, allowing future swaps, upgrades, or chaining logic without reworking the core memory system.
