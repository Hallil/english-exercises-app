import unittest
from english_exercises import db
from english_exercises.level_access import allowed_in_A, allowed_in_B, allowed_in_C, calculate_score
from english_exercises.models import User

class AuthenticationTests(unittest.TestCase):

    level_A = User('level_A', 'level_A', 10, 2)
    level_B = User('level_B', 'level_B', 21, 7)
    level_C = User('level_C', 'level_C', 30, 2)

    @classmethod
    def setUpClass(cls):
        db.session.add(cls.level_A)
        db.session.add(cls.level_B)
        db.session.add(cls.level_C)

    @classmethod
    def tearDownClass(cls):
        db.session.rollback()
        db.session.query(User).delete()
        db.session.commit()

    def test_allowed_in_A(self):
        self.assertTrue(allowed_in_A(calculate_score('level_A')))
        self.assertTrue(allowed_in_A(calculate_score('level_B')))
        self.assertTrue(allowed_in_A(calculate_score('level_C')))

    def test_allowed_in_B(self):
        self.assertFalse(allowed_in_B(calculate_score('level_A')))
        self.assertTrue(allowed_in_B(calculate_score('level_B')))
        self.assertTrue(allowed_in_B(calculate_score('level_C')))

    def test_allowed_in_C(self):
        self.assertFalse(allowed_in_C(calculate_score('level_A')))
        self.assertFalse(allowed_in_C(calculate_score('level_B')))
        self.assertTrue(allowed_in_C(calculate_score('level_C')))

if __name__ == '__main__':
    unittest.main()
