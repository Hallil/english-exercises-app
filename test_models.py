import unittest
from english_exercises import db
from english_exercises.models import OpenQuestion, MultiQuestion


class ModelTests(unittest.TestCase):
    open_question = OpenQuestion('ja', 'ne', 'Nouns', 'A1')
    multi_question = MultiQuestion('ja', 'baz', 'ne', 'Nouns', 'A1')

    @classmethod
    def setUpClass(cls):
        db.session.add(cls.open_question)
        db.session.add(cls.multi_question)

    @classmethod
    def tearDownClass(cls):
        db.session.rollback()
        db.session.query(OpenQuestion).delete()
        db.session.query(MultiQuestion).delete()
        db.session.commit()

    def test_db_length_fail(self):
        self.failUnlessRaises(IndexError, self.open_question, '')
    def test_db_none_fail(self):
        self.failUnlessRaises(IndexError, self.open_question, None)