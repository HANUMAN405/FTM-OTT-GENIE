from pytube import YouTube

video_url = 'https://youtu.be/-X4Ri2ctj78'

try:
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
    if stream:
        stream.download()
        print("Download completed!")
    else:
        print("No suitable stream found.")
except Exception as e:
    print(f"Error: {e}")
