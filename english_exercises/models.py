from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    amountCorrect = db.Column(db.Integer)
    amountIncorrect = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, username, password, amountCorrect, amountIncorrect, score):
        self.username = username
        self.password = password
        self.amountCorrect = amountCorrect
        self.amountIncorrect = amountIncorrect
        self.score = score

    def __repr__(self):
        return '<User %r>' % self.username


class OpenQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(80))
    answer = db.Column(db.String(80))
    category = db.Column(db.String(80))
    level = db.Column(db.String(80))

    def __init__(self, question, answer, category, level):
        self.question = question
        self.answer = answer
        self.category = category
        self.level = level


    def __repr__(self):
        return '<User %r>' % self.username

class OpenQuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(80))
    question = db.ForeignKey('OpenQuestion.id')
    user = db.ForeignKey('user.id')

    def __init__(self, answer, question, user):
        self.answer = answer
        self.question = question

    def __repr__(self):
        return '<User %r>' % self.username

class MultiQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))
    level = db.Column(db.String(80))
    question = db.Column(db.String(80))
    answer = db.Column(db.String(80))
    multiplechoiceAnswer = db.Column(db.String(80))

    def __init__(self, question, multiplechoiceAnswer, answer, category, level):
        self.category = category
        self.level = level
        self.question = question
        self.multiplechoiceAnswer = multiplechoiceAnswer
        self.answer = answer

    def __repr__(self):
        return '<User %r>' % self.username

class MultiQuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.ForeignKey('User.id')
    question = db.ForeignKey('MultiQuestion.id')
    givenoanswer = db.Column(db.String(80))
    givenchoiceanswer = db.Column(db.String(80), nullable=False)
#

    def __init__(self, user, answer, multiplechoiceAnswer):
        self.user = user
        self.answer = answer
        self.multiplechoiceAnswer = multiplechoiceAnswer


    def __repr__(self):
        return '<User %r>' % self.username