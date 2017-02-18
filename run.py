from os import environ
from english_exercises import app, db
from english_exercises.models import User, OpenQuestion


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(User('Level_A', 'Level_A', 1, 0))
    db.session.add(User('Level_B', 'Level_B', 16, 7))
    db.session.add(User('Level_C', 'Level_C', 30, 4))
    db.session.commit()


def fill_adverbs():
    db.session.query(OpenQuestion).delete()
    db.session.commit()
    db.session.add(OpenQuestion("He (quick) reads a book:", "quickly", "Adverbs", "A1"))
    db.session.add(OpenQuestion("Mandy is a (pretty) girl:", "pretty", "Adverbs", "A1"))
    db.session.add(OpenQuestion("The class is (terrible) loud today:", "terribly", "Adverbs", "A1"))
    db.session.add(OpenQuestion("Max is (good) a singer:", "good", "Adverbs", "A1"))
    db.session.add(OpenQuestion("You can (easy)open this tin:", "easily", "Adverbs", "A1"))
    db.session.commit()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        init_db()
        fill_adverbs()

    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
