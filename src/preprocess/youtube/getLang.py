from youtube_transcript_api import YoutubeTranscriptApi
from .getID import extract_video_id

async def get_languages(url:str):
    video_id = extract_video_id(url)
    availableLanguages = YouTubeTranscriptApi.list_transcripts(video_id)