from . import db
from models import User


def get_correct_answers(userName):
    return db.session.query(User).filter(username=userName)

def get_incorrect_answers(username):
    pass

def calculate_score(correct, incorrect):
    pass

def allowed_in(level, score):
    if level == ('A1' or 'A2'):
        if level < 10:
            return False
        else:
            True
    elif level == ('B1' or 'B2'):
        if level < 20:
            return False
        else:
            True
    elif level == 'C1' and level > 20:
        return True
    else:
        raise ValueError('Negative score? Really?')
