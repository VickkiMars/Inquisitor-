import unittest
from src.utils.milestone_to_questions import get_questions

class TestMilestoneToQuestions(unittest.TestCase):
    """
    Test suite for generating questions based on milestones.
    """
    def test_get_questions(self):
        chunk = "This is a sample paragraph discussing the importance of AI in healthcare."
        milestone = "heading"
        user_requested = 50
        questions = get_questions(milestone, chunk, user_requested)
        
        # Assert the number of questions doesn't exceed the requested ones
        self.assertEqual(len(questions), 50)
    
    def test_optional_questions(self):
        chunk = "This is a sample paragraph discussing the importance of AI in healthcare."
        milestone = "chapter"
        user_requested = 30
        questions = get_questions(milestone, chunk, user_requested)
        
        # Assert optional questions are included
        self.assertIn("Optional Questions:", questions)
        self.assertGreater(len(questions), 30)

if __name__ == "__main__":
    unittest.main()
