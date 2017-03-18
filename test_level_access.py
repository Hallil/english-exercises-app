import unittest
from english_exercises import db
from english_exercises.level_access import allowed_in_level, get_correct_answers, get_incorrect_answers, calculate_score
from english_exercises.models import User


class LevelAccessTests(unittest.TestCase):

    user_1 = User('Test_A', 'level_A', 1, 0, 0)
    user_2 = User('Test_B', 'level_A', 16, 7, 4)
    user_3 = User('Test_C', 'level_A', 22, 0, 14)

    @classmethod
    def setUpClass(cls):
        db.session.add(cls.user_1)
        db.session.add(cls.user_2)
        db.session.add(cls.user_3)

    @classmethod
    def tearDownClass(cls):
        db.session.rollback()
        db.session.query(User).delete()
        db.session.commit()

    def test_allowed_in_level(self):
        self.assertTrue(allowed_in_level('A', 0))
        self.assertTrue(allowed_in_level('A', 10))
        self.assertTrue(allowed_in_level('A', 20))
        self.assertTrue(allowed_in_level('A', 30))
        self.assertFalse(allowed_in_level('B', 0))
        self.assertTrue(allowed_in_level('B', 10))
        self.assertTrue(allowed_in_level('B', 20))
        self.assertTrue(allowed_in_level('B', 30))
        self.assertFalse(allowed_in_level('C', 0))
        self.assertFalse(allowed_in_level('C', 10))
        self.assertTrue(allowed_in_level('C', 20))
        self.assertTrue(allowed_in_level('C', 30))

    def test_get_correct_answers(self):
        self.assertEqual(get_correct_answers(self.user_2.username), 16)

    def test_get_incorrect_answers(self):
        self.assertEqual(get_incorrect_answers(self.user_2.username), 7)

    def test_calculate_score(self):
        self.assertEqual(11.13, calculate_score(self.user_2.username))

if __name__ == '__main__':
    unittest.main()
