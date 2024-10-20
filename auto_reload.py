import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the path to your project directory that you want to monitor
PROJECT_DIRECTORY = "/home/azureuser/blog2/"

# Define the command to reload Nginx server
NGINX_RELOAD_COMMAND = "sudo systemctl reload nginx"  # Replace this if needed

class ChangeHandler(FileSystemEventHandler):
    """Handles file system events like modifications, creations, and deletions."""
    def on_any_event(self, event):
        # Check if the event is a modification, creation, or deletion of a file
        if event.is_directory:
            return None

        # Reload Nginx when any file is changed
        print(f"File {event.src_path} changed. Reloading Nginx server...")
        os.system(NGINX_RELOAD_COMMAND)

def monitor_directory(path):
    """Monitors the specified directory for changes."""
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_directory(PROJECT_DIRECTORY)

