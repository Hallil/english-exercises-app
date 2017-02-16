import english_exercises
from english_exercises import app
from functools import wraps
from flask import render_template, make_response, request, session, escape, url_for, redirect, current_app, jsonify, json, abort, flash
from english_exercises.dblayer import *

#decorator function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in') is None:
            flash("You must be logged in for this feature")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=['GET'])
def home():
    #flash("Welcome!")
    return render_template('index.html')

# Section for Rene
@app.route("/adverbs")
@app.route("/adverbs/<level>")
@login_required
def adverbs(level=None):
    if not session.get('logged_in'):
        abort(401)
        if level != None:
            if level == 'A1':
                return render_template('adverbs/A1.html')
            elif level == 'A2':
                return render_template('adverbs/A2.html')
            elif level == 'B1':
                return render_template('adverbs/B1.html')
            elif level == 'B2':
                return render_template('adverbs/B2.html')
            elif level == 'C1':
                    return render_template('adverbs/C1.html')
            else:
                return render_template('adverbs/adverbs.html')
        else:
            return render_template('adverbs/adverbs.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # db = get_db()
        # db.execute("INSERT INTO users (username, password, correct, incorrect) VALUES (?, ?, 0, 0);",
        #              [request.form['username'], request.form['password']])
        # db.commit()
        c = register_user(request.form['username'], request.form['password'])
        if c == 1: flash('You were succesfully registered.')
        else: 
            print('Register failed')
            return redirect(url_for('register'))
        
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if check_login(request.form['username'], request.form['password']):
            n = str(request.form['next'])
            print("request.form['next']="+request.form['next'])
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash("You were succesfully logged in!")
            if request.form['next'] == "": #breaks here
                return redirect(url_for('home'))
            else: 
                print("login else")
                return url_for('home')
        else:
            return "access denied"
    else:
        return render_template('login.html')

@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    del session['logged_in']    
    if session['username'] is not None:
        del session['username']
    flash("You were succesfully logged out!")
    return redirect(url_for('home'))

# Section for Eelco

@app.route("/gerund")
@app.route('/gerund/<level>')
@login_required
def gerund(level=None):
    if level == "A1":
        questions = []
        questions.append(question("My friend is good %s playing volleyball."))
        questions.append(question("She complains %s bullying." ))
        questions.append(question("They are afraid %s losing the match."))
        questions.append(question("She doesn't feel %s working on the computer."))
        questions.append(question("We are looking forward %s going out at the weekend."))
        questions.append(question("Laura dreams %s living on a small island."))
        questions.append(question("Andrew apologized %s being late."))
        questions.append(question("I don't agree %s what you are saying."))
        questions.append(question("The girls insisted %s going out with Kerry."))
        questions.append(question("Edward thinks %s climbing trees this afternoon."))
        return render_template('gerund/A1.html', questions=questions, level=level)
    elif level == "A2":
        options = ['about', 'for', 'on', 'to', 'of', 'up']
        questions = []
        questions.append(question("I'm afraid %s %s my smartphone. (to lose)", options))
        questions.append(question("She is looking forward %s %s her brother.<i>(to see)</i>", options))
        questions.append(question("He is responsible %s %s the money. <i>(to collect)</i>", options))
        questions.append(question("She is used %s %s to bed late. <i>(to go)</i>", options))
        questions.append(question("He apologized %s %s late. <i>(to be)</i>", options))
        questions.append(question("Larry never worries %s %s friends. <i>(to make)</i>", options))
        questions.append(question("We are tired %s %s for the bus. <i> (to wait)</i>", options))
        questions.append(question("She insisted %s %s to her lawyer. <i>(to talk)</i>", options))
        questions.append(question("You should give %s %s you sister. <i>(to bully)</i>", options))
        questions.append(question("They are thinking %s %s to Italy. <i>(to move)</i>", options))
        return render_template('gerund/A2.html', questions=questions, level=level)
    elif level == "B1":
        questions = []
        questions.append(question("I can't imagine Peter %s <i>(go)</i> by bike."))
        questions.append(question("He agreed %s <i>(buy)</i> a new car."))
        questions.append(question("The questions is easy %s <i>(answer)</i>"))
        questions.append(question("The man asked me how %s <i>(get)</i> to the airport."))
        questions.append(question("I look forward to %s <i>(see)</i> you at the weekend."))
        questions.append(question("Are you thinking of %s <i>(visit)</i> London?"))
        questions.append(question("We decided %s <i>(run)</i> through the forest."))
        questions.append(question("The teacher expected Sarah %s <i>(study)</i> hard."))
        questions.append(question("She doesn't mind %s <i>(work)</i> the night shift."))
        questions.append(question("I learned %s <i>(ride)</i> the bike at the age of 5."))
        return render_template('gerund/B1.html', questions=questions, level=level)
    elif level == "B2":
        questions = []
        questions.append(question("We decided %s <i>(buy)</i> a new car."))
        questions.append(question("They've got some work %s <i>(do)</i>."))
        questions.append(question("Peter gave up %s <i>(smoke)</i>."))
        questions.append(question("He'd like %s <i>(fly)</i> an aeroplane."))
        questions.append(question("I enjoy %s <i>(write)</i> picture postcards."))
        questions.append(question("Do you know what %s <i>(do)</i> if there's a fire in the house?"))
        questions.append(question("Avoid %s <i>(make)</i> silly mistakes."))
        questions.append(question("My parents wanted me %s <i>(be)</i> home at 11 o'clock."))
        questions.append(question("I dream about %s <i>(build)</i> a big house."))
        questions.append(question("I'm hoping %s <i>(see)</i> Lisa."))
        return render_template('gerund/B2.html', questions=questions, level=level)
    elif level == "C1":
        questions = []
        questions.append(question("be bad %s + Gerund"))
        questions.append(question("danger %s + Gerund"))
        questions.append(question("be crazy %s + Gerund"))
        questions.append(question("difficulty %s + Gerund"))
        questions.append(question("be ashamed %s + Gerund"))
        questions.append(question("idea %s + Gerund"))
        questions.append(question("way %s + Gerund"))
        questions.append(question("be fond %s + Gerund"))
        questions.append(question("succeed %s + Gerund"))
        questions.append(question("accused %s + Gerund"))
        return render_template('gerund/C1.html', questions=questions, level=level)


    return render_template('gerund/gerund.html')
@app.route('/api/submit/<category>/<level>', methods=['POST'])
@login_required
def submit(category, level):
    if request.method == 'POST':
        #do stuff to test and store results
        data = dict((key, request.form.get(key)) for key in request.form.keys())
        return jsonify(data)

class question():
    def __init__(self, questionstring, options=None):
        self.question = questionstring
        self.options = options


# Section for Halil
@app.route("/nouns")
@login_required
def nouns():
    return "Nouns Exercises :DDDDDD"


# Section for Halil
@app.route("/results")
@login_required
def results():
    return render_template('results.html')

#is voor testen van db
@app.route('/sql')
def sql():
    return jsonify(init_db())


