import unittest
from english_exercises.authentication import get_user, register_user, user_exists
from english_exercises.models import User
from english_exercises import db

class AuthenticationTests(unittest.TestCase):

    user = User('Foo', 'bar', 10, 10)

    @classmethod
    def setUpClass(cls):
        db.session.add(cls.user)

    @classmethod
    def tearDownClass(cls):
        db.session.rollback()
        db.session.query(User).delete()
        db.session.commit()

    def test_get_user(self):
        self.assertEqual(self.user.username, get_user('Foo', 'bar').username)
        self.assertEqual(self.user.password, get_user('Foo', 'bar').password)
        self.assertEqual(None, get_user('No', 'user'))

    def test_check_login(self):
        self.assertTrue(user_exists('Foo', 'bar'))
        self.assertFalse(user_exists('bar', 'baz'))

    def test_registered_user(self):
        self.assertEqual(0,register_user('Foo', 'bar'))

    def test_register_user(self):
        self.assertEqual(1,register_user('new', 'user'))
        self.assertEqual('new', db.session.query(User).filter_by(username='new').first().username)


if __name__ == '__main__':
    unittest.main()
