#from .question_pipeline import generate_pipeline_questions
from src.generators.question_generator import map_type_to_prompt, generate_prompt, generate_question_type
from src.extractors.document_extractor import extract_docx, extract_epub, extract_pdf, extract_pptx, extract_txt
from src.api.gemini_call import call_gemini
from typing import Any, List, Union
from src.preprocess.chunking import chunk_text
import logging
import inspect
import os
import trafilatura
from src.utils.log_helper import log_message

logging.basicConfig(filename='inquisitor.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s')

def get_caller_info():
    frame = inspect.stack()[2]
    filename = frame.filename
    lineno = frame.lineno
    return f"({filename}: {lineno})"

def log_error(message):
    caller_info = get_caller_info()
    logging.error(f"{message}{caller_info}")

class Inquisitor:
    def __init__(self, num_questions = 5, data:Union[str,bool]=False):
        self.data = data
        self.num = num_questions
        self.questions = self.generateQuestions(self.chunkData(self.processContent(self.data)))

    def processContent(self, content:Any):
        if isinstance(content, str) and content.startswith('http') or content.startswith('www'):
            return self.processLink(self.data)
        elif os.path.isfile(content):
            return self.processFile(self.data)
        else:
            log_error(f"Unrecognized input: [{content}]")
            return None

    def processLink(self, link:str) -> str:
        """
        Downloads and extracts clean text from an article URL
        
        Args:
            url (str): The URL of the article
        
        Returns:
            str: The extracted article text or an empty string if extraction fails
        """
        try:
            downloaded = trafilatura.fetch_url(url)
            if not downloaded:
                log_error(f"Failed to download content from URL {link}")
                return None
            result = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
            return result if result else None
        except Exception as e:
            log_error(f"Error extracting text from URL: {e}")
            return None
        
    def processFile(self, file_path) -> List[str]:
        _, ext = os.path.splitext(file_path)

        try:
            if ext == ".pdf":
                return extract_pdf(file_path)
            elif ext == ".docx":
                return extract_docx(file_path)
            elif ext == ".txt":
                return extract_txt(file_path)
            elif ext == ".epub":
                return extract_epub(file_path)
            elif ext == ".pptx":
                return extract_pptx(file_path)
            else:
                log_error(f"Unsupported file format: {ext}")
        except Exception as e:
            log_error(e)
            return None
        
    def chunkData(self, data:Any, chunk_size=5) -> List[str]:
        try:
            chunks = chunk_text(data, chunk_size)
            log_message(f"Data chunked successfully: [{chunk_size}]")
            return chunks
        except Exception as e:
            log_error(f"An error occurred while chunking: {e}")
            return None
            
    def generateQuestions(self, chunks:List[str]):
        questions = []
        total = 0
        for chunk in chunks:
            if total >= self.num:
                break
            type_ = call_gemini(generate_question_type(chunk[0]))
            prompt = map_type_to_prompt(type_)
            prompt_ = call_gemini(generate_prompt(chunk=chunk, prompt_types=prompt))
            questions.append(prompt_)
            total += 1
        return questions


if __name__ == "__main__":
    import pprint.pprint as Print
    Session = Inquisitor(data=r"C:\Users\Victor\Downloads\Inquisitor\Inquisitor\test_files\sample.docx")
    Print(Session.questions)
    # Example using a URL
    # url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    # num_questions = 50

    # chunks = generate_pipeline_questions(input_data=url)
    # print(chunks[0])
    # questions = []
    # for chunk in chunks:
    #     type_ = call_gemini(generate_question_type(chunk[0]))
    #     prompt = map_type_to_prompt(type_)
    #     prompt_ = call_gemini(generate_prompt(chunk=chunk, prompt_types=prompt))
    #     questions.append(prompt_)
    #     break


    