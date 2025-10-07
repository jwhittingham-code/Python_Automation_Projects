from pytubefix import YouTube as tube 
from sys import argv

link = argv[1]
yt = tube(link)

print(yt.title)

yd = yt.streams.get_highest_resolution()
yd.download("./Video",f'{yt.title}.mp4')