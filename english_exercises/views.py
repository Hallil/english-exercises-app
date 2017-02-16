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
        return render_template('gerund/A1.html')
    elif level == "A2":
        return render_template('gerund/A2.html')
    elif level == "B1":
        return render_template('gerund/B1.html')
    elif level == "B2":
        return render_template('gerund/B2.html')
    elif level == "C1":
        questions = []
        questions.append(question('My friend is good %s playing volleyball.'))
        questions.append(question("hello %s world"))
        questions.append(question("3 %s"))
        return render_template('gerund/C1.html', questions=questions)


    return render_template('gerund/gerund.html')
@app.route('/api/submit/<category>/<level>', methods=['POST'])
def submit(category, level):
    if request.method == 'POST':
        #do stuff to test and store results
        return redirect(url_for('home'))

class question():
    
    def __init__(self, questionstring):
        self.question = questionstring


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


