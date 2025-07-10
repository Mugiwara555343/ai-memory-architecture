# demo_run.py
import sys
from pathlib import Path
import importlib.util

# === Paths ===
ROOT_DIR = Path(__file__).resolve().parents[0]
SCRIPTS_DIR = ROOT_DIR / "scripts"
MEMORY_FILE = ROOT_DIR / "memory" / "markdown" / "sample_entry.md"
PARSED_OUTPUT = ROOT_DIR / "memory" / "parsed_json" / f"{MEMORY_FILE.stem}.parsed.json"

# === Import memory_parser dynamically ===
parser_spec = importlib.util.spec_from_file_location("memory_parser", SCRIPTS_DIR / "memory_parser.py")
parser = importlib.util.module_from_spec(parser_spec)
parser_spec.loader.exec_module(parser)

# === Import model_router dynamically ===
router_spec = importlib.util.spec_from_file_location("model_router", SCRIPTS_DIR / "model_router.py")
router = importlib.util.module_from_spec(router_spec)
router_spec.loader.exec_module(router)

def run_memory_pipeline():
    print(f"📥 Parsing: {MEMORY_FILE.name}")
    parsed = parser.parse_md_file(MEMORY_FILE)

    PARSED_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(PARSED_OUTPUT, "w", encoding="utf-8") as f:
        import json
        json.dump(parsed, f, indent=2, ensure_ascii=False)
    print(f"✅ Parsed to: {PARSED_OUTPUT}")

    print("🔁 Routing to models...")
    router.run_router(str(PARSED_OUTPUT), prompt=None)

if __name__ == "__main__":
    run_memory_pipeline()
