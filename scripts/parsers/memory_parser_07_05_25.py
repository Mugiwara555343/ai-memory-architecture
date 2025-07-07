import sys
import json
from pathlib import Path
import requests
import os
import time

# === CONFIGURATION ===
ROOT = Path(__file__).resolve().parents[2]  # Mauricio_Memory_Core
BASE = ROOT / "99_System_Settings"

print(f"[DEBUG] Project root: {ROOT}")

# === OUTPUT FOLDERS ===
vault_json     = BASE / "parsed_memory" / "vault_json"
hermes_meta    = BASE / "parsed_memory" / "hermes_metadata"
stylized_path  = ROOT / "06_Voice_&_Tone" / "stylized_logs"

vault_json.mkdir(parents=True, exist_ok=True)
hermes_meta.mkdir(parents=True, exist_ok=True)
stylized_path.mkdir(parents=True, exist_ok=True)

# === JSON EXTRACTOR FOR HERMES ===
def extract_json(raw: str) -> str:
    start = raw.find("{")
    if start == -1:
        return None
    for end in range(len(raw), start, -1):
        snippet = raw[start:end]
        try:
            json.loads(snippet)
            return snippet
        except json.JSONDecodeError:
            continue
    return None

# === MODEL CALL WITH RETRIES ===
def query_model(model, messages, retries=2, delay=5):
    for attempt in range(retries + 1):
        try:
            payload = {
                "model": model,
                "messages": messages,
                "temperature": 0.2
            }
            response = requests.post("http://127.0.0.1:1234/v1/chat/completions", json=payload, timeout=90)
            response.raise_for_status()
            result = response.json()["choices"][0]["message"]["content"].strip()
            print(f"[DEBUG Hermes Raw Output Preview] {result[:300]}")
            return result
        except requests.exceptions.ReadTimeout:
            print(f"[TIMEOUT] {model} timed out. Retrying in {delay}s... ({attempt+1}/{retries})")
            time.sleep(delay)
        except Exception as e:
            print(f"[ERROR] Model {model} failed:")
            raise e
    raise TimeoutError(f"{model} failed after {retries} retries.")

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

# === CLEAN OUTPUT (remove ```json + fix JSON artifacts) ===
if capy_out.startswith("```json"):
    capy_out = capy_out.strip().removeprefix("```json").removesuffix("```").strip()
elif capy_out.startswith("```"):
    capy_out = capy_out.strip().removeprefix("```").removesuffix("```").strip()

capy_out = capy_out.replace("\\", "").replace("\n", " ").strip()

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

# === HERMES METADATA (Smart Extraction) ===
summary_text = parsed.get("summary", "")[:500]

hermes_prompt = [
    {
        "role": "system",
        "content": (
            "You are a strict metadata extractor. You will receive a short summary of a personal log.\n\n"
            "Respond ONLY with a VALID JSON object in this format:\n"
            "{\n"
            "  \"topics\": [\"...\"],\n"
            "  \"keywords\": [\"...\"],\n"
            "  \"mood\": \"...\",\n"
            "  \"importance\": \"Low\" | \"Medium\" | \"High\"\n"
            "}\n\n"
            "Do not explain. Do not repeat. Do not wrap in code blocks. Your reply MUST begin with '{'."
        )
    },
    {"role": "user", "content": summary_text}
]

hermes_raw = query_model("openhermes-2.5-mistral-7b-medquad", hermes_prompt)

# Save full raw for inspection
hermes_raw_path = BASE / "parsed_memory" / f"{src.stem}.hermes_raw.txt"
hermes_raw_path.write_text(hermes_raw, encoding="utf-8")

hermes_out = extract_json(hermes_raw)

if not hermes_out:
    print("[!] Hermes: No valid JSON block extracted.")
    print("--- Raw Output ---\n", hermes_raw)
    sys.exit(1)

try:
    metadata = json.loads(hermes_out)
    hermes_path = hermes_meta / f"{src.stem}.hermes.json"
    hermes_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(f"[Hermes Metadata] → {hermes_path.relative_to(ROOT)}")
except json.JSONDecodeError as e:
    print("[!] Hermes JSON decode failed after extraction:")
    print(f"    {e}")
    print("--- Extracted ---")
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
