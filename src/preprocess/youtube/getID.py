from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    """Extract YouTube video ID from various URL formats"""
    
    if 'youtube.com' in url:
        query = urlparse(url).query
        params = parse_qs(query)
        return params.get('v', [None])[0]
    elif 'youtu.be' in url:
        return urlparse(url).path[1:]
    elif len(url) == 11:  # Direct video ID
        return url
    return None