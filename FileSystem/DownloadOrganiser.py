import os, pathlib, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"file {os.path.basename(event.src_path)} has been modified!")
            print(event.src_path)
            print(os.path.basename(event.src_path))
            file = os.path.basename(event.src_path)
            print(file)
            if file.endswith('.txt'):
                shutil.move(event.src_path,f"/home/j/Downloads/text/{file}" )
                print("file moved")
            elif file.endswith('.jpg'):
                shutil.move(event.src_path,f"/home/j/Downloads/img/{file}" )
                print("file moved")
        return super().on_modified(event)

src = pathlib.Path("/home/j/Downloads")
itemlist = list()
# for i in os.scandir(src):
#     #print(i)
#     itemlist.append(i)

print(itemlist)


observer = Observer()
event_handler = MyHandler()


    
observer.schedule(event_handler,src,recursive=True)

observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()