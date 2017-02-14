import english_exercises
from english_exercises import app
from flask import render_template, make_response, request, session, escape, url_for, redirect, current_app, jsonify, json, abort, flash
from english_exercises.dblayer import *


@app.route("/")
def home():
    return render_template('index.html')

# Section for Rene
@app.route("/adverbs")
@app.route("/adverbs/<level>")
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
        if c == 1: flash('New entry was successfully posted')
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
            session['logged_in'] = True
            return "You are now logged in"
        else:
            return "access denied"
    else:
        return render_template('login.html')

# Section for Eelco
@app.route("/gerund")
@app.route('/gerund/<level>')
def gerund(level=None):
    return "Gerund Exercises :DDDDDD"


# Section for Halil
@app.route("/nouns")
def nouns():
    return "Nouns Exercises :DDDDDD"


# Section for Halil
@app.route("/results")
def results():
    return render_template('results.html')

@app.route('/sql')
def sql():
    print(query_db("SELECT u.username FROM users as u where u.username=?", ('eelco', )))
    return jsonify(query_db("SELECT * FROM users"))
