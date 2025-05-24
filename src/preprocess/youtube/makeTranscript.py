import whisper
import os
from .getAudio import download_youtube_audio

async def make_transcript(url):
    """Transcribe and save with consistent naming"""
    model = whisper.load_model("tiny.en")
    title, filename = download_youtube_audio(url)
    print("Transcribing...")
    result = model.transcribe(filename)
    transcript_file = f"{title}.txt"
    with open(transcript_file, "w") as f:
        f.write(result["text"])
    return transcript_file