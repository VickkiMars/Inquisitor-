from google import genai
from google.genai import types
from google.api_core import retry
from ast import literal_eval
from dotenv import load_dotenv
from src.utils.text_cleaner import remove_trailers
import os

load_dotenv()
api_key = os.getenv("API_KEY")

is_retriable = lambda e: (isinstance(e, genai.errors.APIError) and e.code in {429, 503})

if not hasattr(genai.models.Models.generate_content, '__wrapped__'):
    genai.models.Models.generate_content = retry.Retry(
        predicate=is_retriable,
    )(genai.models.Models.generate_content)

config = types.GenerateContentConfig(temperature=0.0)
client = genai.Client(api_key=api_key)
chat = client.chats.create(model='gemini-2.0-flash')

def call_gemini(prompt):
    print(prompt)
    try:
        response = chat.send_message(
            message = prompt
        )
        text = remove_trailers(response.text, '[]')
        print(f"\nModel  Response: {text}\n")
        if text is not None:
            return text
        else:
            raise ValueError(f"There was an error with the model response: {text}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None