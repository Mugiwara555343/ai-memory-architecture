import os
import sys
import json
import requests
import re

# === Constants ===
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PARSED_DIR = os.path.join(ROOT_DIR, "99_System_Settings", "parsed_memory")
ZEPHYR_JSON_DIR = os.path.join(PARSED_DIR, "zephyr_json")
ORCA_JSON_DIR = os.path.join(PARSED_DIR, "hermes_metadata")

ZEPHYR_MODEL = "zephyr-7b-beta"
ORCA_MODEL = "mistral-7b-openorca"
SERVER_URL = "http://127.0.0.1:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}

# === Ensure output dirs ===
os.makedirs(ZEPHYR_JSON_DIR, exist_ok=True)
os.makedirs(ORCA_JSON_DIR, exist_ok=True)

# === Utilities ===
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def write_json(data, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def clean_and_parse_json(raw_content, model_name):
    try:
        # Option 1: Fenced JSON block
        match = re.search(r"```json\s*(\{.*?\})\s*```", raw_content, re.DOTALL)
        if match:
            return json.loads(match.group(1).strip())

        # Option 2: Loose JSON object
        match = re.search(r"\{.*\}", raw_content, re.DOTALL)
        if match:
            return json.loads(match.group(0).strip())

        # Option 3: Label-based fallback (Zephyr-style)
        fallback = {}
        lines = raw_content.strip().splitlines()
        for line in lines:
            if ":" not in line:
                continue
            key, val = line.split(":", 1)
            key = key.strip().lower()
            val = val.strip()

            if key.startswith("summary"):
                fallback["summary"] = val
            elif key.startswith("emotional tone"):
                fallback["emotional_tone"] = val
            elif key.startswith("tags"):
                fallback["tags"] = [tag.strip() for tag in val.split(",") if tag.strip()]
            elif key.startswith("intensity"):
                try:
                    fallback["intensity"] = int(val[0])
                except:
                    fallback["intensity"] = 3

        if set(fallback) == {"summary", "emotional_tone", "tags", "intensity"}:
            return fallback
        else:
            raise ValueError("Fallback format incomplete")

    except Exception:
        print(f"[WARN] {model_name} returned unparseable JSON:\n{raw_content}\n")
        return None

def query_model(model, prompt):
    try:
        response = requests.post(
            SERVER_URL,
            headers=HEADERS,
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 40,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()
        return clean_and_parse_json(content, model)
    except Exception as e:
        print(f"[ERROR] Failed to query {model}: {e}")
        return None

def parse_filename(md_path):
    return os.path.splitext(os.path.basename(md_path))[0]

# === Main ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] Usage: python memory_parser.py <path_to_md_file>")
        sys.exit(1)

    md_path = sys.argv[1]
    filename = parse_filename(md_path)
    raw_text = read_file(md_path)

    print(f"[DEBUG] Parsing → {filename}")
    print(f"[DEBUG] Source path → {md_path}")
    print(f"[DEBUG] Project root → {ROOT_DIR}")

    # === Zephyr Prompt ===
    zephyr_prompt = f"""You're a memory extraction assistant. Return ONLY valid compact JSON with the following schema:

{{
  "summary": "<one sentence summary>",
  "emotional_tone": "<sad, angry, anxious, relieved, etc.>",
  "tags": ["<list of keywords/tags>"],
  "intensity": <1-5>
}}

Input memory:
\"\"\"
{raw_text}
\"\"\"
"""

    # === OpenOrca Prompt ===
    orca_prompt = f"""Respond ONLY with valid JSON using this schema:

{{
  "topics": ["<short topic labels>"],
  "keywords": ["<important concepts>"],
  "mood": "<mood keyword>",
  "importance": "<Low | Medium | High>"
}}

DO NOT include commentary or explanation. Only respond with a JSON object.

Input:
\"\"\"
{raw_text}
\"\"\"
"""

    # === Zephyr Run ===
    zephyr_out = query_model(ZEPHYR_MODEL, zephyr_prompt)
    zephyr_path = os.path.join(ZEPHYR_JSON_DIR, f"{filename}.parsed.json")
    if zephyr_out:
        write_json(zephyr_out, zephyr_path)
        print(f"[Zephyr Parsed] → {zephyr_path}")
    else:
        print(f"[Zephyr ERROR] No valid output written for {filename}")

    # === Orca Run ===
    orca_out = query_model(ORCA_MODEL, orca_prompt)
    orca_path = os.path.join(ORCA_JSON_DIR, f"{filename}.orca.json")
    if orca_out:
        write_json(orca_out, orca_path)
        print(f"[OpenOrca Metadata] → {orca_path}")
    else:
        print(f"[OpenOrca ERROR] No valid output written for {filename}")
