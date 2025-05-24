from youtube_transcript_api import YoutubeTranscriptApi
from .getID import extract_video_id
import os, re
from pytube import YouTube
from makeTranscript import make_transcript

def sanitize_filename(title):
    """Remove invalid characters from filenames"""
    return re.sub(r'[\\/*?:"<>|]', "", title)

async def transcribe(url:str) -> str:
    yt = YouTube(url)
    clean_title = sanitize_filename(yt.title)
    try:
        if os.path.exists(f"{clean_title}.mp3"):
            return f"{clean_title}.txt"
        else:
            try:
                transcript = await formalTrans(url)
            except Exception as e:
                print(f"While getting the video's transcript, this error occurred: {e}")
                transcript = False
            if transcript:
                return transcript
            else:
                try:
                    transcript = await make_transcript(url)
                except Exception as e:
                    print(f"An error occurred while generating the transcript: {e}")
                return transcript
    except Exception as e:
        print(f"Could not get or generate transcript: {e}")
        
    
async def formalTrans(url:str, languages=['en']):
    """
    Extract transcript from YouTube video
    Args:
        video_url: YouTube URL or video ID
        languages: Preferred language codes (default: English)
    Returns:
        Formatted transcript text or None if unavailable
    """

    
    try:
        video_id = extract_video_id(url)
        if not video_id:
            return "Invalid YouTube URL/ID"
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        formatted = "\n".join([f"[{entry['start']:.2f}s] {entry['text']}" 
                             for entry in transcript])
        return formatted
        
    except Exception as e:
        return f"Error: {str(e)}"
