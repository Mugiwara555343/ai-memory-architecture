
# Memory Parsers

This folder includes all the memory parsing scripts — the heart of your AI system’s internal understanding. Each parser version handles different models or formats, and they convert raw log entries into structured `.json` and `.md` files for long-term use.

### ✨ Included Scripts

- `memory_parser.py`  
  Core parser — stable version currently in use for general processing.

- `memory_parser_07_05_25.py`  
  Time-stamped experimental version with tweaks for n8n compatibility.

- `memory_parser_LM_STUDIO.py`, `memory_parser_all_3_models.py`  
  Variants that route memory parsing logic across multiple models using LM Studio's endpoints.

- `memory_parser_capy_working.py`, `zephyr_parser.py`  
  Specialized parsers designed for specific local models (Capybara, Zephyr).

- `memory_parser_v1_full.py`, `memory_parser_2_models.py`  
  Older but more comprehensive versions — useful for fallback or full-system chaining.

---

### 🧠 Purpose

Parsers are responsible for transforming memory inputs into structured, meaningful context — tagging emotions, generating summaries, and storing logs for retrieval.

Each version serves as a snapshot of your project’s evolution, allowing flexible experimentation with new models or formats without breaking the core system.

---

### 🔧 Future Additions

- Parser auto-selector based on active model
- Markdown-to-JSON and JSON-to-Markdown reconversion
- Topic tagging and summary condensation
