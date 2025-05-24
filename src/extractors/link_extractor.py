import trafilatura
from urllib.parse import urlparse
# Add this after extraction:
from trafilatura.meta import detect_language
import re

def is_valid_url(url):
    """Check if the URL is valid"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def sanitize_filename(title):
    """Clean the title to create a valid filename"""
    return re.sub(r'[\\/*?:"<>|]', '', title.strip())

def extract_and_save_text(url):
    """Extract text from URL and save to a file"""
    if not is_valid_url(url):
        print("Invalid URL format. Please include http:// or https://")
        return

    try:
        # Download and extract text
        downloaded = trafilatura.fetch_url(url)
        text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
        language = detect_language(text)

        if not text:
            print("No extractable text found on this page")
            return

        # Get page title for filename
        title = trafilatura.extract_metadata(downloaded).get('title', 'extracted_text')
        filename = f"{sanitize_filename(title)}.txt"

        # Save to file
        return text, language
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("🌐 Web Text Extractor (using Trafilatura)")
    url = input("Enter URL: ").strip()
    extract_and_save_text(url)