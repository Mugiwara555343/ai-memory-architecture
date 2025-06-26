
# n8n Workflows

This folder contains visual automation flows created with [n8n](https://n8n.io), designed to support the AI memory system through input capture, memory processing, and LLM-triggered actions.

---

## 📤 Included Workflows

### 🟢 `telegram_memory_logger.json`
A simple Telegram → File workflow that listens for user input via Telegram bot and stores messages as `.txt` memory logs.

**Nodes:**
- `Telegram Trigger`: Listens for incoming messages
- `Function`: Formats the message with timestamp
- `Write to File`: Saves to a local memory log folder

**Usage:**
- Used to quickly capture thoughts, emotions, or entries on mobile
- Connects directly to `file_watcher.py` for real-time parsing

---

## 📁 File Structure

```plaintext
n8n-workflows/
├── telegram_memory_logger.json
└── [future_workflows].json
