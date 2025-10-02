from pytubefix import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print(yt.title)

yd = yt.streams.get_audio_only()
yd.download("./Music",f"{yt.title}.mp4")