import english_exercises
from english_exercises import app
from functools import wraps
from flask import render_template, make_response, request, session, escape, url_for, redirect, current_app, jsonify, json, abort, flash
from english_exercises.dblayer import *

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    flash("Welcome!")
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
            print(request.form['next'])
            session['logged_in'] = True
            if request.form['next'] != "": return redirect(request.form['next'])
            else: return redirect(url_for('home'))
        else:
            return "access denied"
    else:
        return render_template('login.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    if session['logged_in'] is not None:
        del session['logged_in']
        return redirect(url_for('index'))

# Section for Eelco

@app.route("/gerund")
@app.route('/gerund/<level>')
@login_required
def gerund(level=None):
    return "Gerund Exercises :DDDDDD"


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

@app.route('/sql')
def sql():
    print(query_db("SELECT u.username FROM users as u where u.username=?", ('eelco', )))
    print(g.user)
    return jsonify(query_db("SELECT * FROM users"))


