import sys
import json
from pathlib import Path
import requests
import os

# === CONFIGURATION ===
BASE = Path(__file__).resolve().parents[1]  # 99_System_Settings
ROOT = BASE.parent                          # Mauricio_Memory_Core

print(f"[DEBUG] Project root: {ROOT}")

# === OUTPUT FOLDERS ===
vault_json     = ROOT / "99_System_Settings" / "parsed_memory" / "vault_json"
hermes_meta    = ROOT / "99_System_Settings" / "parsed_memory" / "hermes_metadata"
stylized_path  = ROOT / "06_Voice_&_Tone" / "stylized_logs"

vault_json.mkdir(parents=True, exist_ok=True)
hermes_meta.mkdir(parents=True, exist_ok=True)
stylized_path.mkdir(parents=True, exist_ok=True)

# === MODEL WRAPPER ===
def query_model(model, messages):
    try:
        payload = {
            "model": model,
            "messages": messages,
            "temperature": 0.2
        }
        response = requests.post("http://127.0.0.1:1234/v1/chat/completions", json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"[ERROR] Model {model} failed:")
        raise e

# === ENTRY POINT ===
if len(sys.argv) < 2:
    print("Usage: python memory_parser.py <input_file>")
    sys.exit(1)

src = Path(sys.argv[1])
raw = src.read_text(encoding="utf-8")

# === CAPYBARA PARSING ===
capy_prompt = [
    {
        "role": "system",
        "content": (
            "You are a memory parser. Your task is to read any kind of log—emotional, physical, or companion-based—"
            "and return a valid JSON object capturing both emotional structure and contextual insight. "
            "Your response must follow this format: "
            "{\"summary\": \"...\", \"emotional_tone\": \"...\", \"tags\": [\"...\"], \"intensity\": \"1-5\"} "
            "Return only this JSON format. No explanation, no commentary."
        )
    },
    {"role": "user", "content": raw}
]

capy_out = query_model("nous-capybara-7b", capy_prompt)

# === CLEAN OUTPUT (remove markdown wrapping) ===
if capy_out.startswith("```json"):
    capy_out = capy_out.strip().removeprefix("```json").removesuffix("```").strip()
elif capy_out.startswith("```"):
    capy_out = capy_out.strip().removeprefix("```").removesuffix("```").strip()

# === DECODE JSON ===
try:
    parsed = json.loads(capy_out)
except json.JSONDecodeError as e:
    print("[ERROR] JSON Decode Error from Capybara:")
    print(f"    {e}")
    print("--- Raw Output ---")
    print(capy_out)
    sys.exit(1)
except Exception as e:
    print(f"[ERROR] Unexpected failure decoding Capybara output: {e}")
    sys.exit(1)

parsed_filename = f"{src.stem}.parsed.json"
parsed_path = vault_json / parsed_filename
parsed_path.write_text(json.dumps(parsed, indent=2), encoding="utf-8")
print(f"[Capybara Parsed] → {parsed_path.relative_to(ROOT)}")

# === HERMES METADATA ===
hermes_prompt = [
    {
        "role": "system",
        "content": (
            "You are a metadata assistant. Given a personal memory log, extract helpful metadata in JSON format. "
            "Fields: {\"topics\": [...], \"keywords\": [...], \"mood\": \"...\", \"importance\": \"Low|Medium|High\"}. "
            "Return only valid JSON. No commentary."
        )
    },
    {"role": "user", "content": raw}
]

hermes_out = query_model("openhermes-2.5-mistral-7b-medquad", hermes_prompt)
try:
    metadata = json.loads(hermes_out)
    hermes_path = hermes_meta / f"{src.stem}.hermes.json"
    hermes_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(f"[Hermes Metadata] → {hermes_path.relative_to(ROOT)}")
except json.JSONDecodeError as e:
    print("[!] Hermes JSON decode failed:")
    print(f"    {e}")
    print("--- Raw Output ---")
    print(hermes_out)
except Exception as e:
    print(f"[!] Unexpected error from Hermes: {e}")

# === MYTHOMAX STYLIZATION ===
if parsed and all(k in parsed for k in ["summary", "emotional_tone", "tags", "intensity"]):
    mytho_prompt = [
        {
            "role": "system",
            "content": (
                "You are a memory stylist. Take the provided memory data and write a vivid, emotional markdown narrative. "
                "Use first person, present tense, and match the tone. Do not summarize — *remember*. Output only markdown."
            )
        },
        {
            "role": "user",
            "content": json.dumps({
                "title": src.stem,
                "summary": parsed["summary"],
                "emotional_tone": parsed["emotional_tone"],
                "tags": parsed["tags"],
                "intensity": parsed["intensity"]
            }, indent=2)
        }
    ]

    mytho_out = query_model("mythomax-l2-13b", mytho_prompt)
    md_file = stylized_path / f"{src.stem}.stylized.md"
    md_file.write_text(mytho_out, encoding="utf-8")
    print(f"[MythoMax Stylized] → {md_file.relative_to(ROOT)}")
else:
    print("[~] Skipping stylization: Capybara data incomplete.")
