from os import environ
from english_exercises import app, db
from english_exercises.models import User, OpenQuestion


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(User('Level_A', 'Level_A', 1, 0, 2))
    db.session.add(User('Level_B', 'Level_B', 16, 7, 3))
    db.session.add(User('Level_C', 'Level_C', 30, 4, 6))
    db.session.commit()


def fill_adverbs():
    db.session.query(OpenQuestion).delete()
    db.session.commit()

    db.session.add(OpenQuestion("He (quick) reads a book:", "quickly", "Adverbs", "A1"))
    db.session.add(OpenQuestion("Mandy is a (pretty) girl:", "pretty", "Adverbs", "A1"))
    db.session.add(OpenQuestion("The class is (terrible) loud today:", "terribly", "Adverbs", "A1"))
    db.session.add(OpenQuestion("Max is (good) a singer:", "good", "Adverbs", "A1"))
    db.session.add(OpenQuestion("You can (easy) open this tin:", "easily", "Adverbs", "A1"))

    db.session.add(OpenQuestion("It's a (terrible) day today:", "terrible", "Adverbs", "A2"))
    db.session.add(OpenQuestion("She sings the song (good):", "well", "Adverbs", "A2"))
    db.session.add(OpenQuestion("He is a (careful) driver:", "careful", "Adverbs", "A2"))
    db.session.add(OpenQuestion("He (careful) drives the car:", "carefully", "Adverbs", "A2"))
    db.session.add(OpenQuestion("The dog barks (loud):", "loudly", "Adverbs", "A2"))

    db.session.add(OpenQuestion("He was (financial) stimulates:", "financially", "Adverbs", "B1"))
    db.session.add(OpenQuestion("The general (willfull) sabotages the group:", "willfully", "Adverbs", "B1"))
    db.session.add(OpenQuestion("The party was (abrupt) stopped:", "abrupty", "Adverbs", "B1"))
    db.session.add(OpenQuestion("She rambled on (endless):", "endlessly", "Adverbs", "B1"))
    db.session.add(OpenQuestion("He declined the offer (firm):", "firmly", "Adverbs", "B1"))

    db.session.add(OpenQuestion("The barber (quick) shaved his head:", "quickly", "Adverbs", "B2"))
    db.session.add(OpenQuestion("We should not take this (light):", "lightly", "Adverbs", "B2"))
    db.session.add(OpenQuestion("He felt (eternal) humiliated:", "eternally", "Adverbs", "B2"))
    db.session.add(OpenQuestion("The soccer team was (brutal) defeated:", "brutally", "Adverbs", "B2"))
    db.session.add(OpenQuestion("He does his work (cheerful):", "cheerfully", "Adverbs", "B2"))

    db.session.add(OpenQuestion("We should offer advice (constructive):", "constructively", "Adverbs", "C1"))
    db.session.add(OpenQuestion("The work was done (sloppy):", "sloppily", "Adverbs", "C1"))
    db.session.add(OpenQuestion("Erik was picking candy (random):", "randomly", "Adverbs", "C1"))
    db.session.add(OpenQuestion("The witch laughed (wicked):", "wickedly", "Adverbs", "C1"))
    db.session.add(OpenQuestion("The surgeon performed (professional):", "professionally", "Adverbs", "C1"))
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
