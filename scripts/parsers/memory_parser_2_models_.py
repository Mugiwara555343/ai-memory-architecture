import os
import sys
import json
import requests

# Constants
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PARSED_DIR = os.path.join(ROOT_DIR, "99_System_Settings", "parsed_memory")
VAULT_JSON_DIR = os.path.join(PARSED_DIR, "vault_json")
ORCA_JSON_DIR = os.path.join(PARSED_DIR, "hermes_metadata")

CAPYBARA_MODEL = "nous-capybara-7b"
ORCA_MODEL = "mistral-7b-openorca"
SERVER_URL = "http://127.0.0.1:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}

# Ensure output directories exist
os.makedirs(VAULT_JSON_DIR, exist_ok=True)
os.makedirs(ORCA_JSON_DIR, exist_ok=True)

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def write_json(data, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def clean_and_parse_json(raw_content, model_name):
    try:
        if "```json" in raw_content:
            raw_content = raw_content.split("```json")[1].split("```")[0].strip()
        return json.loads(raw_content)
    except Exception as e:
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

# Main
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

    # Prompts
    capy_prompt = f"""You're a memory extraction assistant. Return ONLY valid compact JSON with the following schema:

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

    orca_prompt = f"""Extract structured metadata as valid JSON ONLY using this schema:

{{
  "topics": ["<short topic labels>"],
  "keywords": ["<important concepts>"],
  "mood": "<mood keyword>",
  "importance": "<Low | Medium | High>"
}}

Input:
\"\"\"
{raw_text}
\"\"\"
"""

    # Run Capybara
    capy_out = query_model(CAPYBARA_MODEL, capy_prompt)
    capy_path = os.path.join(VAULT_JSON_DIR, f"{filename}.parsed.json")
    if capy_out:
        write_json(capy_out, capy_path)
        print(f"[Capybara Parsed] → {capy_path}")
    else:
        print(f"[Capybara ERROR] No valid output written for {filename}")

    # Run OpenOrca
    orca_out = query_model(ORCA_MODEL, orca_prompt)
    orca_path = os.path.join(ORCA_JSON_DIR, f"{filename}.orca.json")
    if orca_out:
        write_json(orca_out, orca_path)
        print(f"[OpenOrca Metadata] → {orca_path}")
    else:
        print(f"[OpenOrca ERROR] No valid output written for {filename}")
