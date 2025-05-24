import unittest
from src.extractors.link_extractor import extract_text_from_url

class TestLinkExtractor(unittest.TestCase):
    def test_valid_url(self):
        url = "https://en.wikipedia.org/wiki/Natural_language_processing"
        result = extract_text_from_url(url)
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 100)

    def test_invalid_url_format(self):
        url = "invalid-url"
        result = extract_text_from_url(url)
        self.assertEqual(result, "")

    def test_nonexistent_url(self):
        url = "http://thispagedoesnotexist.ltd"
        result = extract_text_from_url(url)
        self.assertEqual(result, "")

    def test_empty_url(self):
        url = ""
        result = extract_text_from_url(url)
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()