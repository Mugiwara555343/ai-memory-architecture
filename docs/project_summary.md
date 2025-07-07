# 🧠 Project Summary: Persistent AI Architecture

This is an independent, modular AI system built from the ground up — designed to run multiple local LLMs with persistent memory, dynamic model routing, and a fully self-hosted architecture.

It’s not just an assistant. It’s a system that remembers, adapts, and responds — structured to grow with long-term use and personal context.

---

## 🛠️ System Features

- **Hybrid CPU/GPU Model Routing**
   - Custom `model_router.py` selects optimal models based on task
   - Supports quantized `.gguf` models (Q4/Q6_K) with dynamic `gpu_layers` configs
   - Uses JSON files to define routing sequences across cognition layers

- **Real-Time Memory Parsing + Vault System**
   - Obsidian-style vault holds structured `.md` and `.json` logs
   - Includes a file watcher that detects changes and triggers `memory_parser.py`
   - Output flows into a memory bank used for context injection and persistent knowledge

- **Custom Gradio Interfaces**
   - Built from scratch using `interface.py` and `gradio_router.py`
   - Modular routing between tasks, memory readers, and model prompts
   - Launches on local endpoints (e.g. `127.0.0.1:7861`) for offline use

- **N8N Workflow Integration (Optional)**
   - Planned automation flows between logs, models, and external APIs
   - JSON output formatting is ready for no-code or low-code orchestration

---

## 💡 Why This Matters

Most AI projects rely on cloud APIs, ephemeral sessions, or third-party tools. This system was built differently — to be:

- **Persistent** – it retains memory over time  
- **Local-first** – it runs fully offline, with no data sent to the cloud  
- **Modular** – every part can be swapped, extended, or rerouted  
- **Emotional-aware** – memory logs include emotional, somatic, and context-rich metadata  
- **Real** – developed in the open, by one person, as a living system

---

## 🧩 Technologies Used

- Python (3.10+)
- Gradio
- llama.cpp / text-generation-webui
- Custom model quantization configs (`gpu_layers`, `ctx_size`)
- Windows 11 (primary dev), Pop!_OS (dual-boot testing)
- Obsidian vault-style memory organization
- JSON-based config routing and data pipelines

---

## 🧭 Next Milestones

- [ ] Expand `memory_reader.py` to support token injection previews
- [ ] Create `model_router_sequence_v2.json` with deeper logic chaining
- [ ] Begin testing on Linux for performance benchmarking
- [ ] Add auto-context responder with feedback loop

---

## 🔓 License

This project is open-sourced under the MIT License. Contributions, forks, and collaboration are welcome.
