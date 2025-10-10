import os, pathlib, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#-------------------------------------------------------------------------

#Source path and destination folders
src = pathlib.Path(".")

imageFolder = "img"
MusicFolder = 'music'
VideoFolder = 'video'
ebookFolder = 'books'

#Creating WatchDog handler class and customised modified function.
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):

        if not event.is_directory:

            #Grabbing file name and file extention of the file that has just been downloaded (modified)         
            file = os.path.basename(event.src_path)
            fileFormat = file.split(".")[1]
            
            #setting destination folder based on file extention.
            destinationFolder = ''
            match fileFormat:
                case 'jpg':
                    destinationFolder = imageFolder
                case 'jpeg':
                    destinationFolder = imageFolder
                case 'png':
                    destinationFolder = imageFolder
                case 'mp4':
                    destinationFolder = VideoFolder
                case 'm4v':
                    destinationFolder = VideoFolder
                case 'mkv':
                    destinationFolder = VideoFolder
                case 'mp3':
                    destinationFolder = MusicFolder
                case 'wav':
                    destinationFolder = MusicFolder
                case 'pdf':
                    destinationFolder = ebookFolder
                case _:
                    pass
            
            #checking if destination folder is set
            if destinationFolder != '':
                #if folder is set we want to create it if doesnt exist.
                try:
                    os.mkdir(f"{src}/{destinationFolder}")
                except:
                    pass

                #finally move the file into the destination folder.
                shutil.move(event.src_path, f"{src}/{destinationFolder}/{file}")
                print(f"{file}, moved to {destinationFolder}")
                #note all this is within the downloads folder.
            
        return super().on_modified(event)

#Creating watchdog observer and event hander objects
# note we use our customer class for the event handler
observer = Observer()
event_handler = MyHandler()

#setting the observer schdule - we tell it how to handle the changes (see custom class above), where to do it and if we also watch child folders.    
observer.schedule(event_handler,src,recursive=True)

#start observing
observer.start()

#loop until we manually interrupt the program.
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

#helps close out the watchdog items.
observer.join()