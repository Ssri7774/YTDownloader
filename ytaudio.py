import os
import subprocess
from pytube import YouTube

# Input
video_url = input("Enter YouTube video URL: ")

# Download video
yt = YouTube(video_url)
stream = yt.streams.filter(only_audio=True).first()
stream.download()

# Extract audio and save as MP3
video_path = stream.default_filename
mp3_filename = video_path[:-4] + ".mp3"
mp3_path = os.path.join("YTDownloads", mp3_filename)
if not os.path.exists("YTDownloads"):
    os.mkdir("YTDownloads")

command = f'ffmpeg -i "{video_path}" -vn -ar 44100 -ac 2 -b:a 192k "{mp3_path}"'
subprocess.call(command, shell=True)

# Remove original video file
os.remove(video_path)

print("Audio downloaded and saved as MP3 in the 'YTDownloads' folder.")
