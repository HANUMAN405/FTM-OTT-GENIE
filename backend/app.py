from pytube import YouTube

# Replace with your YouTube video URL
video_url = 'https://youtu.be/-X4Ri2ctj78'

try:
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed!")
except Exception as e:
    print(f"Error: {e}")
