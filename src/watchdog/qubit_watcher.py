import os
import time
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from src.config.settings import get_local_directory, get_qubit_id

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File created: {event.src_path}")

    def on_modified(self, event):
        print(f"File modified: {event.src_path}")

    def on_deleted(self, event):
        print(f"File deleted: {event.src_path}")

    def on_moved(self, event):
        print(f"File moved: {event.src_path} -> {event.dest_path}")

def watch_qubit():
    observer = Observer()
    handler = Handler()

    qubit_id = get_qubit_id()
    raw = get_local_directory(qubit_id)
    
    print(f"qubit_id: {repr(qubit_id)}")
    print(f"raw path: {repr(raw)}")   # repr() reveals hidden/corrupt characters
    
    directory = Path(raw)
    print(f"resolved: {repr(directory)}")
    print(f"exists: {directory.exists()}")
    
    if not directory.exists():
        raise ValueError(f"Invalid directory configured: {directory}")

    observer.schedule(handler, path=directory)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()