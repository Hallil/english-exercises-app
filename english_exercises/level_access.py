from . import db
from .models import User


def calculate_score(username):
    return get_correct_answers(username) - get_incorrect_answers(username)

def get_correct_answers(userName):
    return User.query.filter(User.username == userName).first().amountCorrect

def get_incorrect_answers(userName):
    return User.query.filter(User.username == userName).first().amountIncorrect


def allowed_in_A(score):
    if score > 0:
        return True
    else:
        return False

def allowed_in_B(score):
    if score > 10:
        return True
    else:
        return False

def allowed_in_C(score):
    if score > 20:
        return True
    else:
        return False
