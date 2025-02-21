from pytube import YouTube
import os

video_url = 'https://youtu.be/-X4Ri2ctj78'

cookie_path = "cookies.txt"  # Save your cookies to this file

try:
    yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed!")
except Exception as e:
    print(f"Error: {e}")
