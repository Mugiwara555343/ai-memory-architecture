# 🧠 System Overview

This document outlines the structure, goals, and flow of the local AI memory system built in this repository.

---

## 🌌 Purpose

The goal of this project is to create a **self-contained, emotionally aware memory system** powered by multiple locally hosted LLMs. It processes journal-style logs and transforms them into persistent memory entries stored in both `.json` and `.md` formats — with emotional context, summaries, and metadata.

Unlike typical assistant builds, this system is fully local and designed to **evolve over time** into a deeper form of interaction and presence.

---

## 🧱 Core Components

| Module | Description |
|--------|-------------|
| `parser.py` | Sends raw `.md` logs to Capybara for emotional parsing |
| `summarizer.py` | Sends logs (or Capybara output) to Hermes for summarization and context |
| `watcher.py` | Monitors `logs/` folder for new files and triggers the pipeline |
| `memory/` | Stores parsed emotional `.json` memory logs for persistent storage |
| `config/models_config.json` | Central model configuration file for flexible model/endpoint control |

---

## 🧠 LLM Roles

| Model | Role | Port | Purpose |
|-------|------|------|---------|
| Capybara | Emotion Parser | 1235 | Tags emotional tone, sentiment, and affect |
| Hermes | Summarizer | 1234 | Extracts core meaning, context, and structure |

All models run locally using [LM Studio](https://lmstudio.ai/) and are manually launched in advance.

---

## 🔄 Memory Flow

```plaintext
1. User drops a new `.md` memory log into the `logs/` folder
2. `watcher.py` detects the file change
3. Log is sent to Capybara → parsed for emotion
4. Output is sent to Hermes → summarized and tagged
5. Final `.json` is saved to `/memory/`, alongside `.md` (if enabled)
