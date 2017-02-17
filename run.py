from os import environ
from english_exercises import app, db, models
from english_exercises.models import User

def init_db():
    db.session.query(User).delete()
    db.session.commit()
    db.create_all()
    db.session.add(User('Level_A', 'Level_A', 5, 0))
    db.session.add(User('Level_B', 'Level_B', 15, 0))
    db.session.add(User('Level_C', 'Level_C', 25, 0))
    db.session.commit()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        init_db()

    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
