import unittest
from src.generators.question_generator import generate_questions

class TestQuestionGenerator(unittest.TestCase):
    
    def test_generate_questions(self):
        chunk = "This is a sample paragraph discussing the importance of AI in healthcare."
        num_questions = 3
        questions = generate_questions(chunk, num_questions)
        
        self.assertEqual(len(questions), num_questions)
        self.assertTrue(all(f"Question {i+1}:" in question for i, question in enumerate(questions)))
    
    def test_empty_chunk(self):
        chunk = ""
        num_questions = 5
        questions = generate_questions(chunk, num_questions)
        
        self.assertEqual(len(questions), num_questions)
        self.assertTrue(all("Question" in question for question in questions))

if __name__ == "__main__":
    unittest.main()
