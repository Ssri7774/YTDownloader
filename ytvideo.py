import os
from pytube import YouTube
video_url = str(input("Enter YouTube video URL: "))

yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download('.\YTDownloads')
if not os.path.exists("YTDownloads"):
    os.mkdir("YTDownloads")

print ("Video downloaded and saved in the 'YTDownloads' folder!!!")
