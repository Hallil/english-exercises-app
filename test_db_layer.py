import requests, unittest
from english_exercises import db, app
from english_exercises.db_layer import correct_answers_in_post, incorrect_answers_in_post, update_user_results
from english_exercises.models import User


class DatabaseLayerTests(unittest.TestCase):

    user_1 = User('Test_A', 'level_A', 1, 4, 0.25)
    params =  {'1': 'work', '2': 'work', '3': 'work', '4': 'work', '5': 'work'}
    app.testing = True
    client = app.test_client()
    request = client.post('/nouns', environ_base={'HTTP_USER_AGENT': 'Chrome, etc'})
    request.params = params

    @classmethod
    def setUpClass(cls):
        db.session.add(cls.user_1)

    @classmethod
    def tearDownClass(cls):
        db.session.rollback()
        db.session.query(User).delete()
        db.session.commit()

    def test_allowed_in_level(self):
        self.assertEqual(1, correct_answers_in_post(self.params))
        self.assertEqual(4, incorrect_answers_in_post(self.params))

    def test_update_user_results(self):
        update_user_results('Test_A', 2, 3)
        self.assertEqual(6, db.session.query(User).filter_by(username='Test_A').first().amountCorrect)
        self.assertEqual(5, db.session.query(User).filter_by(username='Test_A').first().amountIncorrect)


if __name__ == '__main__':
    unittest.main()
