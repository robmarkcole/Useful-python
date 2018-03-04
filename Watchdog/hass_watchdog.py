"""
Example from http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html
modified to write to log.txt.
"""
import sys
import time
import os
import json
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.txt", "*.py", "*.md", "*.jpg", "*.png"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        data = {
            "time": time.strftime("%Y-%m-%d %H:%M"),
            "event": event.event_type,
            "full_path": event.src_path,
            "file": os.path.split(event.src_path)[-1]
        }
        print(json.dumps(data))
        with open('/Users/robincole/.homeassistant/www/data.json', 'a') as f:
            f.write('{}\n'.format(json.dumps(data)))

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    observer.schedule(MyHandler(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
