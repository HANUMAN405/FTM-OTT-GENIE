import yt_dlp

video_url = 'https://youtu.be/-X4Ri2ctj78'

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Save as video title
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
