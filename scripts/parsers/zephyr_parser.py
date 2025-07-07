import os
import sys
import json
import requests
import re

# === Paths ===
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ZEPHYR_OUT_DIR = os.path.join(ROOT_DIR, "99_System_Settings", "parsed_memory", "zephyr_json")
os.makedirs(ZEPHYR_OUT_DIR, exist_ok=True)

# === Config ===
SERVER_URL = "http://127.0.0.1:5000/v1/chat/completions"  # Update if port changes
ZEPHYR_MODEL = "zephyr-7b-beta.Q4_K_S.gguf"
HEADERS = {"Content-Type": "application/json"}

# === Prompt Template ===
def build_prompt(text):
    return f"""Return ONLY valid JSON with this schema. DO NOT say anything else. Do not explain. Stop after the JSON:

{{
  "summary": "<brief one-sentence summary>",
  "emotional_tone": "<short mood>",
  "tags": ["<tag1>", "<tag2>"],
  "intensity": <1 to 5>
}}

Input:
\"\"\"
{text}
\"\"\"
"""

# === Utilities ===
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def write_json(data, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def parse_json_output(raw):
    try:
        # Handle fenced block or loose JSON
        match = re.search(r"```json\s*(\{.*?\})\s*```", raw, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except Exception:
        pass
    return None

# === Model Call ===
def call_zephyr(prompt):
    try:
        response = requests.post(
            SERVER_URL,
            headers=HEADERS,
            json={
                "model": ZEPHYR_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.4,
                "top_p": 0.9,
                "stream": False
            },
            timeout=180  # Increased from 60 to 180 seconds
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[ERROR] Request failed: {e}")
        return None

# === Main ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[USAGE] python zephyr_parser.py path/to/file.md")
        sys.exit(1)

    path = sys.argv[1]
    filename = os.path.splitext(os.path.basename(path))[0]
    raw_text = read_file(path)

    print(f"[INFO] Sending to Zephyr: {filename}")
    prompt = build_prompt(raw_text)
    output = call_zephyr(prompt)

    if not output:
        print("[ERROR] No output from model.")
        sys.exit(1)

    parsed = parse_json_output(output)
    if not parsed:
        print(f"[ERROR] Failed to parse model response:\n{output}")
        sys.exit(1)

    out_path = os.path.join(ZEPHYR_OUT_DIR, f"{filename}.parsed.json")
    write_json(parsed, out_path)
    print(f"[✅ Parsed] → {out_path}")
