import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import hashlib

WATCH_FOLDERS = [
    "01_Emotional_Logs",
    "02_Training_&_Discipline",
    "03_AI_Workflows",
    "04_Companion_Archives",
    "05_Creative_Worlds",
    "06_Voice_&_Tone",
]

BASE = Path(__file__).parents[2]
CHECKSUM_CACHE = {}
PENDING_TASKS = {}
DELAY = 1.5  # Delay before parsing after last modification


def get_hash(file_path):
    try:
        return hashlib.md5(file_path.read_bytes()).hexdigest()
    except:
        return None


def run_parser(src):
    key = str(src.resolve())
    new_hash = get_hash(src)

    if CHECKSUM_CACHE.get(key) == new_hash:
        return  # No meaningful change

    CHECKSUM_CACHE[key] = new_hash

    print(f"🔍 Parsing: {src.name}")
    result = subprocess.run(
        ["python", str(BASE / "99_System_Settings" / "parsed_memory" / "memory_parser.py"), str(src)],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print(f"❌ Parser error for {src.name}:\n{result.stderr.strip()}")


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        src = Path(event.src_path)

        if not src.is_file() or src.suffix not in {'.md', '.txt'}:
            return
        if '.parsed.' in src.name or src.name.endswith('~'):
            return

        key = str(src.resolve())

        # Cancel existing timer
        if key in PENDING_TASKS:
            PENDING_TASKS[key].cancel()

        # Set new delayed parse
        timer = threading.Timer(DELAY, run_parser, args=(src,))
        PENDING_TASKS[key] = timer
        timer.start()


if __name__ == "__main__":
    observer = Observer()
    for folder in WATCH_FOLDERS:
        path = BASE / folder
        observer.schedule(Handler(), str(path), recursive=True)

    print("🧠 Memory Watcher with Fingerprinting & Delay is running…\n")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
