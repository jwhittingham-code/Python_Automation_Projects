import os, pathlib, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src = pathlib.Path("/home/j/Downloads")

imageFolder = "img"
MusicFolder = 'music'
VideoFolder = 'video'
ebookFolder = 'books'


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"file {os.path.basename(event.src_path)} has been modified!")
         
            file = os.path.basename(event.src_path)
            fileFormat = file.split(".")[1]
            print(fileFormat)
            print(file)

            destinationFolder = ''

            match fileFormat:
                case 'jpg':
                    destinationFolder = imageFolder
                case 'mp4':
                    destinationFolder = VideoFolder
                case 'mp3':
                    destinationFolder = MusicFolder
                case 'pdf':
                    destinationFolder = ebookFolder


            # if file.endswith('.txt'):
            #     shutil.move(event.src_path,f"/home/j/Downloads/text/{file}" )
            #     print("file moved")
            # elif file.endswith('.jpg'):
            #     shutil.move(event.src_path,f"/home/j/Downloads/img/{file}" )
            #     print("file moved")
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