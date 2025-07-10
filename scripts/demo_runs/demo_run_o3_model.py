from pathlib import Path
import json
import sys

# ────────────────────────────────────────────────────────────────────────────────
# 🔧  Path configuration – point to the scripts folder so we can import modules
#     Adjust if your folder layout differs.
# ────────────────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.append(str(SCRIPTS_DIR))

# Local imports (live inside scripts/)
from memory_parser import parse_md_file  # noqa: E402
from model_router import run_router      # noqa: E402


# ────────────────────────────────────────────────────────────────────────────────
# 🧩  Pipeline helpers
# ────────────────────────────────────────────────────────────────────────────────

def parse_memory(md_path: Path) -> Path:
    """Parse a raw Markdown memory log into a `.parsed.json` file.

    Returns the path to the generated JSON file.
    """
    parsed_data = parse_md_file(md_path)
    parsed_path = md_path.with_suffix(".parsed.json")

    with parsed_path.open("w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Parsed memory saved → {parsed_path.relative_to(PROJECT_ROOT)}")
    return parsed_path


def route_memory(json_path: Path, prompt: str = "") -> None:
    """Send the parsed memory file through the model routing sequence."""
    print("\n🚚 Routing memory through models…")
    # `run_router` prints each model's output internally.
    run_router(str(json_path), prompt)


# ────────────────────────────────────────────────────────────────────────────────
# 🚀  Main entry point
# ────────────────────────────────────────────────────────────────────────────────

def main() -> None:
    raw_md = PROJECT_ROOT / "memory" / "markdown" / "sample_entry.md"

    if not raw_md.exists():
        print(f"❌ Memory log not found: {raw_md}")
        return

    # 1️⃣  Parse the raw Markdown log
    parsed_json = parse_memory(raw_md)

    # 2️⃣  Route via model chain (empty user prompt for now)
    route_memory(parsed_json)


if __name__ == "__main__":
    main()
