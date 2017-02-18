from english_exercises import db
from english_exercises.models import User, OpenQuestion


def update_user_results(user_name, correct, incorrect):
    user = User.query.filter_by(username=user_name).first()
    user.amountCorrect = user.amountCorrect + correct
    user.amountIncorrect = user.amountIncorrect + incorrect
    db.session.commit()


def process_answers(request, level, session_username):
    questions = OpenQuestion.query.filter_by(level=level).all()
    correct_answers = len(list(filter(lambda q: request.form[str(q.id)] == q.answer, questions)))
    incorrect_answers = len(list(filter(lambda q: request.form[str(q.id)] != q.answer, questions)))
    update_user_results(session_username, correct_answers, incorrect_answers)

