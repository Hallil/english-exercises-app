import english_exercises
import unittest

class ViewsTestCase(unittest.TestCase):

    client = english_exercises.app.test_client()


    def test_not_logged_in(self):
        self.assertEqual(302, self.client.get('/nouns').status_code)
        self.assertEqual(302, self.client.get('/nouns/A1').status_code)
        self.assertEqual(302, self.client.get('/nouns/A2').status_code)
        self.assertEqual(302, self.client.get('/nouns/B1').status_code)
        self.assertEqual(302, self.client.get('/nouns/B2').status_code)
        self.assertEqual(302, self.client.get('/nouns/C1').status_code)

if __name__ == '__main__':
    unittest.main()
