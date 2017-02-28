from os import environ
from english_exercises import app, db
from english_exercises.models import User, OpenQuestion, MultiQuestion


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(User('Level_A', 'Level_A', 1, 0, 2))
    db.session.add(User('Level_B', 'Level_B', 16, 7, 3))
    db.session.add(User('Level_C', 'Level_C', 30, 4, 6))
    db.session.add(User('Halil', 'Halil', 0, 0, 0))
    db.session.commit()

def fill_nouns():
    # A-1
    db.session.add(OpenQuestion("I don't have much ..", "work", "Nouns", "A1"))
    db.session.add(OpenQuestion("There are a lot of ..", "chair", "Nouns", "A1"))
    db.session.add(OpenQuestion("The farmer loaded his cart with .. of fresh vegetables", "box", "Nouns", "A1"))
    db.session.add(OpenQuestion("There are many ..", "beaches", "Nouns", "A1"))
    db.session.add(OpenQuestion("Do you like this kind of ..", "music", "Nouns", "A1"))

def fill_adverbs():

    db.session.add(OpenQuestion("He (quick) reads a book:", "quickly", "Adverbs", "A1"))
    db.session.add(OpenQuestion("Mandy is a (pretty) girl:", "pretty", "Adverbs", "A1"))
    db.session.add(OpenQuestion("The class is (terrible) loud today:", "terribly", "Adverbs", "A1"))
    db.session.add(OpenQuestion("Max is a (good) singer:", "good", "Adverbs", "A1"))
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

def fill_gerund():

    #   A1
    db.session.add(OpenQuestion("My friend is good %s playing volleyball", "at", "Gerund", "A1"))
    db.session.add(OpenQuestion("She complains %s bullying." , "about", "Gerund", "A1"))
    db.session.add(OpenQuestion("They are afraid %s losing the match.", "of", "Gerund", "A1"))
    db.session.add(OpenQuestion("She doesn't feel %s working on the computer.", "like", "Gerund", "A1"))
    db.session.add(OpenQuestion("We are looking forward %s going out at the weekend.", "to", "Gerund", "A1"))
    db.session.add(OpenQuestion("Laura dreams %s living on a small island.", "of", "Gerund", "A1"))
    db.session.add(OpenQuestion("Andrew apologized %s being late.", "for", "Gerund", "A1"))
    db.session.add(OpenQuestion("I don't agree %s what you are saying.", "with", "Gerund", "A1"))
    db.session.add(OpenQuestion("The girls insisted %s going out with Kerry.", "on", "Gerund", "A1"))
    db.session.add(OpenQuestion("Edward thinks %s climbing trees this afternoon.", "about", "Gerund", "A1"))
    #   A2
    db.session.add(MultiQuestion("I'm afraid %s %s my smartphone. (to lose)", "of", "losing", "Gerund", "A2"))
    db.session.add(MultiQuestion("She is looking forward %s %s her brother.<i>(to see)</i>", "to", "seeing", "Gerund", "A2"))
    db.session.add(MultiQuestion("He is responsible %s %s the money. <i>(to collect)</i>", "for", "collecting", "Gerund", "A2"))
    db.session.add(MultiQuestion("She is used %s %s to bed late. <i>(to go)</i>", "to", "going", "Gerund", "A2"))
    db.session.add(MultiQuestion("He apologized %s %s late. <i>(to be)</i>", "for", "being", "Gerund", "A2"))
    db.session.add(MultiQuestion("Larry never worries %s %s friends. <i>(to make)</i>", "about", "losing", "Gerund", "A2"))
    db.session.add(MultiQuestion("We are tired %s %s for the bus. <i> (to wait)</i>", "of", "waiting", "Gerund", "A2"))
    db.session.add(MultiQuestion("She insisted %s %s to her lawyer. <i>(to talk)</i>", "on", "talking", "Gerund", "A2"))
    db.session.add(MultiQuestion("You should give %s %s you sister. <i>(to bully)</i>", "up", "bullying", "Gerund", "A2"))
    db.session.add(MultiQuestion("They are thinking %s %s to Italy. <i>(to move)</i>", "about", "moving", "Gerund", "A2"))
    #   B1
    db.session.add(OpenQuestion("I can't imagine Peter %s <i>(go)</i> by bike.", "going", "Gerund", "B1"))
    db.session.add(OpenQuestion("He agreed %s <i>(buy)</i> a new car.", "to buy", "Gerund", "B1"))
    db.session.add(OpenQuestion("The question is easy %s <i>(answer)</i>", "to", "Gerund", "B1"))
    db.session.add(OpenQuestion("The man asked me how %s <i>(get)</i> to the airport.", "to get", "Gerund", "B1"))
    db.session.add(OpenQuestion("I look forward to %s <i>(see)</i> you at the weekend.", "to seeing", "Gerund", "B1"))
    db.session.add(OpenQuestion("Are you thinking of %s <i>(visit)</i> London?", "visiting", "Gerund", "B1"))
    db.session.add(OpenQuestion("We decided %s <i>(run)</i> through the forest.", "to run", "Gerund", "B1"))
    db.session.add(OpenQuestion("The teacher expected Sarah %s <i>(study)</i> hard.", "to study", "Gerund", "B1"))
    db.session.add(OpenQuestion("She doesn't mind %s <i>(work)</i> the night shift.", "working", "Gerund", "B1"))
    db.session.add(OpenQuestion("I learned %s <i>(ride)</i> the bike at the age of 5.", "to ride", "Gerund", "B1"))
    #   B2
    db.session.add(OpenQuestion("We decided %s <i>(buy)</i> a new car.", "to buy", "Gerund", "B2"))
    db.session.add(OpenQuestion("They've got some work %s <i>(do)</i>.", "to do", "Gerund", "B2"))
    db.session.add(OpenQuestion("Peter gave up %s <i>(smoke)</i>.", "smoking", "Gerund", "B2"))
    db.session.add(OpenQuestion("He'd like %s <i>(fly)</i> an aeroplane.", "to fly", "Gerund", "B2"))
    db.session.add(OpenQuestion("I enjoy %s <i>(write)</i> picture postcards.", "writing", "Gerund", "B2"))
    db.session.add(OpenQuestion("Do you know what %s <i>(do)</i> if there's a fire in the house?", "to do", "Gerund", "B2"))
    db.session.add(OpenQuestion("Avoid %s <i>(make)</i> silly mistakes.", "making", "Gerund", "B2"))
    db.session.add(OpenQuestion("My parents wanted me %s <i>(be)</i> home at 11 o'clock.", "to be", "Gerund", "B2"))
    db.session.add(OpenQuestion("I dream about %s <i>(build)</i> a big house.", "building", "Gerund", "B2"))
    db.session.add(OpenQuestion("I'm hoping %s <i>(see)</i> Lisa.", "to see", "Gerund", "B2"))
    #   C1
    db.session.add(OpenQuestion("be bad %s + Gerund", "at", "Gerund", "C1"))
    db.session.add(OpenQuestion("danger %s + Gerund", "of", "Gerund", "C1"))
    db.session.add(OpenQuestion("be crazy %s + Gerund", "about", "Gerund", "C1"))
    db.session.add(OpenQuestion("difficulty %s + Gerund", "in", "Gerund", "C1"))
    db.session.add(OpenQuestion("be ashamed &s + Gerund", "of", "Gerund", "C1"))
    db.session.add(OpenQuestion("idea %s + Gerund", "of", "Gerund", "C1"))
    db.session.add(OpenQuestion("way %s + Gerund", "of", "Gerund", "C1"))
    db.session.add(OpenQuestion("be fond %s + Gerund", "of", "Gerund", "C1"))
    db.session.add(OpenQuestion("succeed %s + Gerund", "in", "Gerund", "C1"))
    db.session.add(OpenQuestion("accused %s + Gerund", "of", "Gerund", "C1"))
    db.session.commit()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        init_db()
        fill_adverbs()
        fill_gerund()

    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
