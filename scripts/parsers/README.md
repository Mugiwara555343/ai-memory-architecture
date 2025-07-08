# 🧠 Memory Parsers

This folder includes all parser modules responsible for transforming raw memory logs into structured `.json` and `.md` formats. Each version is tuned for a specific model configuration, routing logic, or system architecture.

These scripts form the core of the AI’s internal understanding — organizing thoughts, tags, tone, and metadata for long-term retention.

---

## ✨ Included Scripts

- **`memory_parser.py`**  
  Primary parser — currently in use for stable, general-purpose parsing.

- **`memory_parser_07_05_25.py`**  
  Timestamped development version. Tweaked for n8n automation integration and CLI triggering.

- **`memory_parser_LM_STUDIO.py`, `memory_parser_all_3_models.py`**  
  Parsers configured for multi-model routing using LM Studio (e.g., Capybara, Hermes, Zephyr).

- **`memory_parser_capy_working.py`, `zephyr_parser.py`**  
  Dedicated parsing variants for single-model testing or isolated role tasks.

- **`memory_parser_v1_full.py`, `memory_parser_2_models.py`**  
  Older or experimental full-chain parsing variants for testing complex workflows and summarization logic.

---

## 🔍 Purpose

The parser layer translates personal memory into a machine-readable language.

It identifies emotional tone, key themes, intensity scores, and source paths — and converts them into structured cognitive records for use in downstream models or memory-aware workflows.

