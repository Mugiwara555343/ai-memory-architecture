# 🔄 n8n Workflows

This folder contains visual automation flows built with [n8n](https://n8n.io), designed to support the AI memory system by capturing user input, processing memory entries, and triggering LLM tasks in response.

These flows help extend the system’s reach — enabling real-time, mobile, or external memory updates.

---

## 📂 Included Workflows

### 🟢 `telegram_memory_logger.json`
A Telegram-to-file workflow that listens for user input via a Telegram bot and logs messages as `.txt` memory entries.

**Nodes:**
- `Telegram Trigger` – Listens for messages from Telegram
- `Function` – Formats the message with timestamp and optional tag
- `Write to File` – Saves the result to a local memory folder

**Usage:**
- Capture emotional or contextual updates from mobile
- Log ideas, observations, or thoughts instantly
- Automatically feed entries into `file_watcher.py` for downstream parsing

---

### 🧠 `llm_memory_responder.json` *(in development)*
Placeholder for an LLM-triggered response workflow. Will eventually support:
- Auto-summarizing memory updates
- Emotional tone detection
- Telegram-based AI journaling responses

---

## 🌱 Planned Additions

- Remote entry validation (e.g., filters or tag requirements)  
- Feedback loop: receive model-generated reflections via Telegram  
- Multi-step automation for voice-to-text or multi-modal logging

---

Even with only two JSONs, this folder tells a story: you’re not just working with local code — you’re thinking about **how real people will interface with it.**

Would you like to add an `.md` in this folder summarizing “How to Import an n8n Workflow,” or is this enough for now?
