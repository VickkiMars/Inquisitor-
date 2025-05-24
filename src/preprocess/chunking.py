from nltk.tokenize import sent_tokenize
from utils.log_helper import log_message
import nltk

# Function to remove references from the text
def remove_references(text):
    # Define the keyword for the references section (simple 'References')
    reference_keyword = "References"

    # Find the index of the 'References' section
    start_index = text.find(reference_keyword)
    print(start_index)
    if start_index != -1:
        # Cut the text before the references section
        return text[:start_index].strip()

try: 
    nltk.data.find('punkt_tab')
    log_message(f"'punkt_tab' is already downloaded")
except nltk.downloader.DownloadError:
    try:
        log_message('Downloading`punkt_tab`')
        nltk.download('punkt_tab', quiet=True)
        log_message('`punkt_tab` downloaded successfully.')
    except Exception as e:
        log_message(f"Error downloading `punkt_tab`: {e}", "error")

# Function to chunk the text into groups of sentences
def chunk_text(text, chunk_size=5):
    # Step 1: Tokenize the text into sentences using NLTK
    text = remove_references(text)
    sentences = sent_tokenize(text)
    # Step 2: Group sentences into chunks of the given size
    chunks = [sentences[i:i + chunk_size] for i in range(0, len(sentences), chunk_size)]
    
    # Step 3: Return the chunks
    return chunks

# Sample text to simulate the input (replace with your actual text)
