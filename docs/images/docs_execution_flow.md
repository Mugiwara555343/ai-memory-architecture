# Execution Flow Overview

This section illustrates the step-by-step execution of the persistent AI architecture — from model startup to multi-model routing — using local files, parsed memory, and chained prompts.

---

## Step 1: Model Invocation via Terminal

![Step 1 - Model Start](./images/step1_model_start.png)

Terminal command executes `model_router.py`, targeting a `.parsed.json` memory file and feeding it into the selected model (Capybara).

---

## Step 2: Memory File Loaded in Gradio UI

![Step 2 - Parsed Memory JSON](./images/step2_parsed_memory_json.png)

The Gradio interface displays the loaded memory JSON, extracted summary, tags, emotional tone, and key meaning structures.

---

## Step 3: Parsed JSON Output View

![Step 3 - Terminal JSON Preview](./images/step3_terminal_run.png)

Raw `.parsed.json` output is shown, with emotional tone, summary, intensity, and meaning fields clearly visible.

---

## Step 4: Gradio Prompt Interface

![Step 4 - Gradio Prompt UI](./images/step4_gradio_ui.png)

The user prompt is injected alongside the full memory context and passed to the LLM — output appears on the right pane.

---

## Step 5: Prompt Injection Code Snippet

![Step 5 - Prompt Injection Script](./images/step5_prompt_injection.png)

`gradio_router.py` uses the `router_sequence.json` to route prompts to specific models and parse memory payloads.

---

## St
