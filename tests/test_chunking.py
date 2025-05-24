import unittest
from src.preprocess.chunking import chunk_text_by_milestones, generate_questions_from_chunks

class TestChunking(unittest.TestCase):
    
    def test_chunk_text_by_milestones(self):
        sample_text = """Chapter 1: Introduction
        This is the first paragraph of in a bird's.
        This is the second paragraph of a catrina.

        Chapter 2: Background
        This is the first paragraph of gattuso"""
        
        # Test chunking by chapters
        chapters = chunk_text_by_milestones(sample_text, 20)
        print(chapters, len(chapters))
        self.assertEqual(len(chapters), 3)  # 3 chunks: introduction, background, empty last chunk

        # Test chunking by paragraphs
        paragraphs = chunk_text_by_milestones(sample_text, 90)
        self.assertEqual(len(paragraphs), 4)  # Should split into 4 paragraphs

        # Test chunking by period (sentences)
        sentences = chunk_text_by_milestones(sample_text, 100)
        self.assertGreater(len(sentences), 5)  # More than 5 sentences

    def test_generate_questions(self):
        sample_chunks = [
            "This is a chunk of text related to chapter 1.",
            "This is another chunk of text from chapter 2."
        ]
        
        questions = generate_questions_from_chunks(sample_chunks, 3)
        self.assertEqual(len(questions), 2)  # Only 2 chunks, so 2 questions
        
        # Check the format of the generated question
        self.assertTrue(questions[0].startswith("Question 1: What is the main point of the following text?"))
        self.assertTrue("chunk of text" in questions[0])  # Checking the start of the text in the question

if __name__ == "__main__":
    unittest.main()
