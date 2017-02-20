from english_exercises import db
from english_exercises.models import User, OpenQuestion
from english_exercises.level_access import calculate_score


def correct_answers_in_post(request):
    correct_answer_count = 0
    for key, value in request.items():
        correct_answer = find_answer_object(key)
        if correct_answer.answer == value:
            correct_answer_count += 1
    return correct_answer_count


def incorrect_answers_in_post(request):
    incorrect_answer_count = 0
    for key, value in request.items():
        correct_answer = find_answer_object(key)
        if correct_answer.answer != value:
            incorrect_answer_count += 1
    return incorrect_answer_count


def find_answer_object(question_id):
    return OpenQuestion.query.filter_by(id=question_id).first()


def update_user_results(user_name, correct, incorrect):
    user = User.query.filter_by(username=user_name).first()
    user.amountCorrect = user.amountCorrect + correct
    user.amountIncorrect = user.amountIncorrect + incorrect
    user.score = calculate_score(user_name)
    db.session.commit()
