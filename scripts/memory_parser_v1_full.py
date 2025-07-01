import sys
from pathlib import Path
import requests
import json
import re
from datetime import datetime

def is_model_available():
    try:
        response = requests.get("http://127.0.0.1:1234/v1/models", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Get the source file path from CLI
src = Path(sys.argv[1])
text = src.read_text(encoding='utf-8')

if not is_model_available():
    print("[ERROR] Capybara model not loaded. Skipping parsing and Hermes chain.")
    sys.exit(1)

# Step 1: Capybara Parsing
capy_payload = {
    "model": "nous-capybara-7b",
    "messages": [
        {
            "role": "system",
            "content": "You are a memory parser. Your task is to read any kind of log — emotional, physical, or companion-based — and return a clean JSON object capturing both emotional structure and contextual insight. Your output must always include the following fields: - summary: A 1–2 sentence summary of the log, written clearly and emotionally aware. - emotional_tone: One or two words describing the overall tone. - tags: 3–6 topic keywords. - intensity: A number from 1 to 5. Return only valid JSON."
        },
        {
            "role": "user",
            "content": text
        }
    ],
    "temperature": 0.3,
    "max_tokens": 512
}

capy_response = requests.post("http://127.0.0.1:1234/v1/chat/completions", json=capy_payload)
capy_output = capy_response.json()["choices"][0]["message"]["content"].strip()

if capy_output.startswith("```json"):
    capy_output = capy_output.strip("`").strip()[4:].strip()

try:
    capy_data = json.loads(capy_output)
except json.JSONDecodeError:
    capy_data = {"error": "Invalid JSON output from Capybara", "raw_output": capy_output}

capy_data["source_path"] = str(src)
capy_data["parsed_at"] = datetime.now().isoformat()

base = Path(__file__).parents[2]
capy_dir = base / "99_System_Settings" / "parsed_memory"
capy_dir.mkdir(parents=True, exist_ok=True)
stem = src.stem
(capy_dir / f"{stem}.parsed.json").write_text(json.dumps(capy_data, indent=2), encoding='utf-8')
(capy_dir / f"{stem}.parsed.md").write_text(f"```json\n{json.dumps(capy_data, indent=2)}\n```", encoding='utf-8')

# Step 2: Hermes Chain
hermes_payload = {
    "model": "openhermes-2.5-mistral-7b-medquad",
    "messages": [
        {
            "role": "system",
            "content": "You are a memory summarization agent. Your task is to read a structured emotional memory (parsed by a prior model) and return high-level metadata and archive context. You must return a valid JSON object with the following fields: title, memory_type, tags, importance, notes (optional). Return only valid JSON. No commentary or prose."
        },
        {
            "role": "user",
            "content": json.dumps(capy_data)
        }
    ],
    "temperature": 0.3,
    "max_tokens": 512
}

hermes_response = requests.post("http://127.0.0.1:1234/v1/chat/completions", json=hermes_payload)
hermes_output = hermes_response.json()["choices"][0]["message"]["content"].strip()

def extract_first_json_block(text):
    matches = re.findall(r'\{.*?\}', text, re.DOTALL)
    for block in matches:
        try:
            return json.loads(block)
        except json.JSONDecodeError:
            continue
    return {"error": "No valid JSON block found in Hermes output", "raw_output": text}

hermes_data = extract_first_json_block(hermes_output)
hermes_data["capy_source"] = str(capy_dir / f"{stem}.parsed.json")
hermes_data["generated_at"] = datetime.now().isoformat()

hermes_dir = capy_dir / "hermes_metadata"
hermes_dir.mkdir(parents=True, exist_ok=True)
(hermes_dir / f"{stem}.hermes.json").write_text(json.dumps(hermes_data, indent=2), encoding='utf-8')

print(f"[Capybara Parsed] {src.name} -> {stem}.parsed.json")
print(f"[Hermes Metadata] -> {stem}.hermes.json")

# Step 3: MythoMax Stylization
if not hermes_data.get("title") or not hermes_data.get("memory_type"):
    print("[~] Skipping stylization: Hermes metadata incomplete.")
    sys.exit(0)

mytho_input = {
    "title": hermes_data.get("title"),
    "memory_type": hermes_data.get("memory_type"),
    "tags": hermes_data.get("tags"),
    "importance": hermes_data.get("importance"),
    "notes": hermes_data.get("notes"),
    "summary": capy_data.get("summary"),
    "emotional_tone": capy_data.get("emotional_tone"),
    "intensity": capy_data.get("intensity"),
}

mytho_payload = {
    "model": "mythomax-l2-13b",
    "messages": [
        {
            "role": "user",
            "content": json.dumps(mytho_input, indent=2)
        }
    ],
    "temperature": 0.7,
    "max_tokens": 1024
}

try:
    print("[DEBUG] MythoMax input payload:")
    print(json.dumps(mytho_input, indent=2))

    mytho_response = requests.post("http://127.0.0.1:1234/v1/chat/completions", json=mytho_payload)
    response_data = mytho_response.json()
    print("[DEBUG] MythoMax raw response:")
    print(json.dumps(response_data, indent=2))

    mytho_output = response_data["choices"][0]["message"]["content"].strip()

    stylized_dir = base / "06_Voice_&_Tone" / "stylized_logs"
    stylized_dir.mkdir(parents=True, exist_ok=True)
    (stylized_dir / f"{stem}.stylized.md").write_text(mytho_output, encoding='utf-8')

    print(f"[MythoMax Stylized] -> {stem}.stylized.md")

except Exception as e:
    print("[ERROR] MythoMax failed to respond correctly.")
    print(f"Error: {e}")
    print(f"Status Code: {mytho_response.status_code}")
    print(f"Raw Text:\n{mytho_response.text}")
