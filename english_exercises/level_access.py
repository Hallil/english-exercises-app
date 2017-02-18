from .models import User


def calculate_score(username):
    ratio = get_correct_answers(username) / (get_correct_answers(username) + get_incorrect_answers(username))
    score = get_correct_answers(username) * ratio
    if score < 0:
        return 0
    else:
        return round(score, 2)


def get_correct_answers(user_name):
    return User.query.filter_by(username=user_name).first().amountCorrect


def get_incorrect_answers(user_name):
    return User.query.filter_by(username=user_name).first().amountIncorrect


def allowed_in_level(level, score):
    if 'A' in level:
        return True
    if 'B' in level:
        if score > 10:
            return True
        else:
            return False
    if 'C' in level:
        if score > 20:
            return True
        else:
            return False
