from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
from datetime import datetime

TEMPLATE_PATH = os.getcwd()

def create_previews():
    print("Event at {}".format(str(datetime.now())))

class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        create_previews()

observer = Observer()
observer.schedule(EventHandler(), TEMPLATE_PATH, recursive=True)
observer.start()

# To be called on EVENT_HOMEASSISTANT_STOP:
#observer.stop()
#observer.join()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()