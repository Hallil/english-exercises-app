from flask import g
from english_exercises.models import User
from english_exercises import db
from flask_sqlalchemy import SQLAlchemy


def user_exists(userName, passWord):
    user = get_user(userName, passWord)
    if user is None:
        return False
    else:
        return True

def register_user(userName, passWord):
    if user_exists(userName, passWord) is False:
        new_user = User(userName, passWord, 0, 0, 0)
        db.session.add(new_user)
        db.session.commit()
        return 1
    else:
        return 0

def get_user(userName, passWord):
    return User.query.filter_by(username=userName).filter_by(password=passWord).first()
