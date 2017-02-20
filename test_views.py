import english_exercises
import unittest

class FlaskrTestCase(unittest.TestCase):

    client = english_exercises.app.test_client()


    def test_not_logged_in(self):
        self.assertEqual(302, self.client.get('/adverbs').status_code)
        self.assertEqual(302, self.client.get('/adverbs/A1').status_code)
        self.assertEqual(302, self.client.get('/adverbs/A2').status_code)
        self.assertEqual(302, self.client.get('/adverbs/B1').status_code)
        self.assertEqual(302, self.client.get('/adverbs/B2').status_code)
        self.assertEqual(302, self.client.get('/adverbs/C1').status_code)


if __name__ == '__main__':
    unittest.main()
