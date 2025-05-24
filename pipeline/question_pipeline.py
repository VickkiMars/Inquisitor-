from typing import Union, List
from src.extractors.link_extractor import extract_text_from_url
from src.extractors.document_extractor import extract_text_from_file
from src.preprocess.chunking import chunk_text

def generate_pipeline_questions(
    input_data: Union[str, bytes],
    is_file: bool = False,
    file_type: str = ""
) -> List[str]:
    """
    Main pipeline function that extracts text, chunks it, and generates questions.

    Args:
        input_data (Union[str, bytes]): URL string or file content.
        user_requested (int): The number of questions the user wants.
        is_file (bool): Whether the input is a file (True) or a URL (False).
        file_type (str): The type of file ('pdf', 'docx', 'epub', etc.).

    Returns:
        List[str]: The list of generated questions.
    """
    if is_file:
        text = extract_text_from_file(input_data, file_type)
    else:
        text = extract_text_from_url(input_data)

    chunks = chunk_text(text)
    # Flatten all questions across chunks until user_requested is met

    return chunks

