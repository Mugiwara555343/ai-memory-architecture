from pathlib import Path

TARGET_DIR = Path(__file__).parents[2] / "memory_core" / "99_System_Settings" / "parsed_memory" / "vault_json"
EXTENSIONS = [".json"]

def clean_json_wrapping(file_path: Path):
    try:
        text = file_path.read_text(encoding="utf-8").strip()
        lines = text.splitlines()

        # Only proceed if wrapped
        if lines and lines[0].strip() == "```json" and lines[-1].strip() == "```":
            new_text = "\n".join(lines[1:-1]).strip()
            file_path.write_text(new_text, encoding="utf-8")
            print(f"✅ Cleaned: {file_path.name}")
        else:
            print(f"✔ No wrapper: {file_path.name}")

    except Exception as e:
        print(f"❌ Error with {file_path.name}: {e}")

def run_cleanup():
    files = [f for ext in EXTENSIONS for f in TARGET_DIR.glob(f"**/*{ext}")]
    for file in files:
        clean_json_wrapping(file)

if __name__ == "__main__":
    run_cleanup()
