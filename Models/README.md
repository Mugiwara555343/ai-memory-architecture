# 🧠 Local LLM Models

This folder contains all the GGUF-format models I have downloaded, tested, and run locally as part of my AI architecture projects. These models are used across various interfaces and tasks including memory parsing, emotional tuning, summarization, and agent-style conversations. 

---

## 📸 Model Snapshot

![Model Inventory](./Screenshot-2025-07-16-173218.png)

---

## 🗂️ Current Models
(PS: Models are not currenlty within GitRepo, copy and paste names into Huggingface to find each)

| Model Name | Size / Quant | Description |
|------------|---------------|-------------|
| `c4ai-command-r-08-2024-Q8_0` | Q8_0 | Command R+ 2024 – Large instruction-tuned model optimized for general-purpose reasoning. |
| `chronos-hermes-13b.Q5_K_M` | Q5_K_M | Emotionally expressive variant of Hermes with storytelling + memory capacity. |
| `deepseek-coder-6.7b-instruct-q4_k_m` | Q4_K_M | Code-specialized LLM trained for programming tasks and code understanding. |
| `t3.1-MOE-6X8B-Dark-RS-Dantes...` | Q4_K_M | Mixture-of-Experts (MoE) model focused on dark fiction, horror, and lore. |
| `mistral-7b-openorca.Q4_K_S` | Q4_K_S | OpenOrca-tuned Mistral 7B; compact and versatile for summarization + chat. |
| `MN-Dark-Horror-The-Cliffhanger-18.5B-D-AU-Q6_k` | Q6_k | Highly specialized narrative model fine-tuned on horror + dialogue-driven fiction. |
| `mythomax-l2-13b.Q6_K` | Q6_K | Popular merged model known for rich completions, writing, and expressive memory. |
| `OpenHermes-2.5-Mistral-7B-medquad.Q6_K` | Q6_K | OpenHermes v2.5 with medquad finetune – strong general-purpose reasoning with improved alignment. |
| `zephyr-7b-beta.Q4_K_S` | Q4_K_S | Lightweight and responsive Zephyr beta model – good for chat and instruction following. |

---

## 🛠️ Notes

- All models are in `GGUF` format and compatible with [text-generation-webui](https://github.com/oobabooga/text-generation-webui) and [LM Studio](https://lmstudio.ai/).
- Switching between models is supported on-the-fly in my custom local router.

---

> _Maintained as part of the [AI Memory Architecture](https://github.com/Mugiwara555343/ai-memory-architecture) project._
