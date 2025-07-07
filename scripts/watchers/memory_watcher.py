import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import hashlib

# ---------------- configuration ---------------- #
WATCH_FOLDERS = [
    "01_Emotional_Logs",
    "02_Training_&_Discipline",
    "03_AI_Workflows",
    "04_Companion_Archives",
    "05_Creative_Worlds",
    "06_Voice_&_Tone",
]

BASE = Path(__file__).resolve().parents[2]          # …/Mauricio_Memory_Core
PARSER_PATH = BASE / "99_System_Settings" / "parsed_memory" / "memory_parser.py"
DELAY          = 1.5                                # seconds
WATCHED_EXTS   = {".md", ".txt"}                    # file types to parse
# ------------------------------------------------ #

CHECKSUM_CACHE = {}
PENDING_TASKS  = {}

def file_hash(path: Path):
    try:
        return hashlib.md5(path.read_bytes()).hexdigest()
    except Exception:
        return None

def run_parser(src: Path):
    """Call memory_parser.py on a single source file."""
    key      = str(src.resolve())
    new_hash = file_hash(src)
    if CHECKSUM_CACHE.get(key) == new_hash:         # unchanged
        return
    CHECKSUM_CACHE[key] = new_hash

    print(f"[+] Parsing: {src.name}")
    result = subprocess.run(
        ["python", str(PARSER_PATH), str(src)],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print(f"[!] Parser error for {src.name}:\n{result.stderr.strip()}")

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        src = Path(event.src_path)
        if (event.is_directory 
            or src.suffix not in WATCHED_EXTS
            or ".parsed."  in src.name
            or ".stylized" in src.name
            or src.name.endswith("~")):
            return

        # will land in the same folder as source file
        output_json = src.parent / f"{src.stem}.parsed.json"
        if output_json.exists():
            print(f"[~] Skipping already-parsed file: {src.name}")
            return

        key = str(src.resolve())
        if key in PENDING_TASKS:
            PENDING_TASKS[key].cancel()

        timer = threading.Timer(DELAY, run_parser, args=(src,))
        PENDING_TASKS[key] = timer
        timer.start()

if __name__ == "__main__":
    observer = Observer()
    for folder in WATCH_FOLDERS:
        path = BASE / folder
        if path.exists():
            print(f"[+] Watching: {path}")
            observer.schedule(Handler(), str(path), recursive=True)
        else:
            print(f"[!] Missing folder (skipped): {path}")

    print("\n🧠 Memory Watcher is running…\n")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
