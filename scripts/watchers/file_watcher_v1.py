# file_watcher_v1.py

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# === CONFIGURATION ===
WATCH_DIRECTORIES = [
    "./logs",
    "./memory"
]

class MemoryWatcherHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[MODIFIED] {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"[CREATED] {event.src_path}")

if __name__ == "__main__":
    print("🧠 Starting file watcher...")
    observers = []

    for folder in WATCH_DIRECTORIES:
        path = Path(folder)
        path.mkdir(exist_ok=True)
        event_handler = MemoryWatcherHandler()
        observer = Observer()
        observer.schedule(event_handler, str(path), recursive=False)
        observer.start()
        observers.append(observer)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("👋 Stopping file watcher...")
        for observer in observers:
            observer.stop()
        for observer in observers:
            observer.join()
