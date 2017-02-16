import unittest
from english_exercises.views import *
from english_exercises import db

class LoginTests(unittest.TestCase):

    user = User('Foo', 'bar', 10, 10)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_user(self):
        pass

    def test_check_login(self):
        pass

    def test_register_user(self):
        pass

if __name__ == '__main__':
    unittest.main()
