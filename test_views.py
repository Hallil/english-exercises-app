import english_exercises
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = english_exercises.app.test_client()

    def test_not_logged_in(self):
        self.assertEqual(302, self.app.get('/adverbs').status_code)


if __name__ == '__main__':
    unittest.main()
