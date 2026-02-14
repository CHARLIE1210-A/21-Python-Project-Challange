import unittest
from main import calculate_score

class TestGameLogic(unittest.TestCase):
    def test_score_positive_attempts(self):
        self.assertEqual(calculate_score(5, {"attempts": 10, "range": 100}), 50)
    
    def test_score_zero_attempts(self):
        self.assertEqual(calculate_score(0, {"attempts": 10, "range": 100}), 0)
        
    def test_score_negative_attempts(self):
        self.assertEqual(calculate_score(-1, {"attempts": 10, "range": 100}), 0)
        

if __name__ == '__main__':
    unittest.main()