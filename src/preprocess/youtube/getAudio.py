from pytube import YouTube
import os
import re

def sanitize_filename(title):
    """Remove invalid characters from filenames"""
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_youtube_audio(url, output_path="."):
    try:
        yt = YouTube(url)
        clean_title = sanitize_filename(yt.title)
        filename=f"{clean_title}.mp3"
        
        if not os.path.exists(filename):
            print(f"Downloading: {yt.title}")
            yt.streams.filter(only_audio=True).first().download(filename=filename)
        return clean_title, filename
    except Exception as e:
        print(f"Error: {e}")
        return None