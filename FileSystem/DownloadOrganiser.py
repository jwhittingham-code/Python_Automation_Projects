import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # if (not event.is_directory) and event.src_path.endswith(".txt"):
        print(f"file {event.src_path} has been modified!")
        # return super().on_modified(event)



# for i in os.scandir(src):
#     print(i)

observer = Observer()
event_handler = MyHandler()
src = "/home/j/Downloads"
observer.schedule(event_handler,src,recursive=True)

observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()