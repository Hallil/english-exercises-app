import unittest
from english_exercises.dblayer import *
from english_exercises.models import *
from english_exercises import db

class LoginTests(unittest.TestCase):

    user = User('Foo', 'bar', 10, 10)

    @classmethod
    def setUpClass(cls):
        db.session.add(cls.user)

    @classmethod
    def tearDownClass(cls):
        db.session.delete(cls.user)

    def test_get_user(self):
        self.assertEqual(self.user.username, get_user('Foo', 'bar').username)
        self.assertEqual(self.user.password, get_user('Foo', 'bar').password)
        self.assertEqual(None, get_user('No', 'user'))

    def test_check_login(self):
        self.assertTrue(check_login('Foo', 'bar'))
        self.assertFalse(check_login('bar', 'baz'))

    def test_register_user(self):
        



if __name__ == '__main__':
    unittest.main()
