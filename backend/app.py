from flask import Flask, render_template, request, send_file, send_from_directory
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    video_title = None

    # Set up yt-dlp options
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'quiet': False,  # Set to False for debug output
        'noplaylist': True,
    }

    try:
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = ydl.prepare_filename(info_dict)

        # Check if the video file was created
        if os.path.exists(video_title):
            return send_file(video_title, as_attachment=True)
        else:
            return "Video was not downloaded. Please check the URL and try again."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Serve static files (CSS and JS)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
