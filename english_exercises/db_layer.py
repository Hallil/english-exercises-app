from english_exercises import db
from english_exercises.models import User, OpenQuestion
from english_exercises.level_access import calculate_score




def correct_answers_in_post(request, level):
    questions = OpenQuestion.query.filter_by(level=level).all()
    return len(list(filter(lambda q: request[str(q.id)] == q.answer, questions)))


def incorrect_answers_in_post(request, level):
    questions = OpenQuestion.query.filter_by(level=level).all()
    return len(list(filter(lambda q: request[str(q.id)] != q.answer, questions)))


def update_user_results(user_name, correct, incorrect):
    user = User.query.filter_by(username=user_name).first()
    user.amountCorrect = user.amountCorrect + correct
    user.amountIncorrect = user.amountIncorrect + incorrect
    user.score = calculate_score(user_name)
    db.session.commit()
