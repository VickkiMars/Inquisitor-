import unittest
from src.extractors.document_extractor import extract_text_from_file

class TestDocumentExtractor(unittest.TestCase):
    
    def test_extract_pdf(self):
        text = extract_text_from_file("test_files/sample.pdf")
        self.assertTrue(len(text) > 0)

    def test_extract_docx(self):
        text = extract_text_from_file("test_files/sample.docx")
        self.assertTrue(len(text) > 0)

    def test_extract_txt(self):
        text = extract_text_from_file("test_files/sample.txt")
        self.assertTrue(len(text) > 0)

    def test_extract_epub(self):
        text = extract_text_from_file("test_files/sample.epub")
        self.assertTrue(len(text) > 0)

    def test_extract_pptx(self):
        text = extract_text_from_file("test_files/sample.pptx")
        self.assertTrue(len(text) > 0)

    def test_invalid_file_type(self):
        # Invalid file extension
        text = extract_text_from_file("test_files/sample.jpg")
        self.assertIsNone(text)

    def test_file_not_found(self):
        # File does not exist
        text = extract_text_from_file("test_files/non_existent_file.txt")
        self.assertIsNone(text)

if __name__ == "__main__":
    unittest.main()
