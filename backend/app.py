from flask import Flask, request, jsonify, render_template
import youtube_dl
import os
import sys

app = Flask(__name__)

# Custom Progress Hook
def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes:
            progress = downloaded_bytes / total_bytes * 100
            sys.stdout.write(f"\rDownloading: {progress:.2f}% complete")
            sys.stdout.flush()
    elif d['status'] == 'finished':
        sys.stdout.write("\nDownload completed!\n")
        sys.stdout.flush()

# Home route to serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

# Download route to handle video download
@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    link = data.get('link')
    custom_filename = data.get('filename')

    if not link:
        return jsonify({"message": "No link provided"}), 400

    if not custom_filename:
        return jsonify({"message": "No filename provided"}), 400

    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'outtmpl': f'./downloads/{custom_filename}.%(ext)s',  # Save with the custom filename
        'progress_hooks': [progress_hook],  # Add the custom progress hook
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 after download
        }],
    }

    try:
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            video_title = info['title']
            return jsonify({"message": f"Downloaded: {video_title} as {custom_filename}.mp4"}), 200

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
