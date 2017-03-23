import unittest


from english_exercises.authentication import user_exists
from english_exercises.models import User
from english_exercises import db

class AuthenticationTests(unittest.TestCase):

    user = User('Foo', 'bar', 10, 10, 5)

    @classmethod
    def setUpClass(cls):
        db.session.add(cls.user)

    @classmethod
    def tearDownClass(cls):
        db.session.rollback()
        db.session.query(User).delete()
        db.session.commit()

    def test_check_login(self):
        self.assertTrue(user_exists('Foo', 'bar'))
        self.assertFalse(user_exists('bar', 'baz'))

    def test_login(self):
        self.browser.visit("http://localhost:5555/login")
        self.browser.fill('username', 'Foo')
        self.browser.fill('password', 'bar')
        self.browser.find_by_value("Login").click()
        from webbrowser import browser
        assert browser.is_text_present("Succesfull")
