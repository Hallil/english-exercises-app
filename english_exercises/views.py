from english_exercises import app
from english_exercises.level_access import calculate_score, allowed_in_level
from functools import wraps
from flask import render_template, request, session, url_for, redirect, jsonify, flash
from english_exercises.models import OpenQuestion, User, MultiQuestion
from english_exercises.authentication import user_exists, register_user
from english_exercises.db_layer import correct_answers_in_post, incorrect_answers_in_post, update_user_results


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
    return render_template('index.html')


@app.route("/adverbs")
@app.route("/adverbs/<level>", methods=['GET', 'POST'])
@login_required
def adverbs(level=None):
    if level == None:
        return render_template('adverbs/adverbs.html')
    else:
        if request.method == 'GET':
            if allowed_in_level(level, calculate_score(session['username'])):
                open_questions = OpenQuestion.query.filter_by(category='Adverbs').filter_by(level=level).all()
                return render_template('adverbs/' + level + '.html', level=level, questions=open_questions)
            else:
                return render_template('adverbs/locked.html')
        if request.method == 'POST':
            update_user_results(
            session['username'],
            correct_answers_in_post(request.form),
            incorrect_answers_in_post(request.form)
            )
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
        if user_exists(request.form['username'], request.form['password']):
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
@app.route('/gerund/<level>', methods=['GET', 'POST'])
@login_required
def gerund(level=None):
    options = ['about', 'for', 'on', 'to', 'of', 'up']
    if level == None:
        return render_template('gerund/gerund.html')
    else:
        if request.method == 'GET':
            if allowed_in_level(level, calculate_score(session['username'])):
                if level != "A2":
                    questions = OpenQuestion.query.filter_by(category='Gerund').filter_by(level=level).all()
                    return render_template('gerund/' + level + '.html', level=level, questions=questions)
                else:
                    questions = MultiQuestion.query.filter_by(category='Gerund').filter_by(level=level).all()
                    return render_template('gerund/' + level + '.html', level=level, questions=questions, options=options)
            else:
                return render_template('gerund/locked.html')
        if request.method == 'POST':
            update_user_results(
            session['username'],
            correct_answers_in_post(request.form),
            incorrect_answers_in_post(request.form)
            )
            return render_template('gerund/gerund.html')
        else:
            return render_template('gerund/gerund.html')
    return render_template('gerund/gerund.html')
    
@app.route('/api/submit/<category>/<level>', methods=['POST'])
@login_required
def submit(category, level):
    if request.method == 'POST':
        #do stuff to test and store results met user in gedachte vanuit session['username']
        data = dict((key, request.form.get(key)) for key in request.form.keys())
        return jsonify(data)

# Section for Halil
@app.route("/nouns")
@app.route('/nouns/<level>', methods=['GET', 'POST'])
@login_required
def nouns(level=None):
    if level == None:
        return render_template('nouns/nouns.html')
    else:
        if request.method == 'GET':
            if allowed_in_level(level, calculate_score(session['username'])):
                questions = OpenQuestion.query.filter_by(category='Nouns').filter_by(level=level).all()
                return render_template('nouns/' + level + '.html', level=level, questions=questions)
            else:
                return render_template('nouns/locked.html')
        if request.method == 'POST':
            update_user_results(
            session['username'],
            correct_answers_in_post(request.form),
            incorrect_answers_in_post(request.form)
            )
            return render_template('nouns/nouns.html')
        else:
            return render_template('nouns/nouns.html')


@app.route("/results")
@login_required
def results():
    return render_template('results.html', results=User.query.all())

#is voor testen van db
# @app.route('/sql')
# def sql():
#     print(query_db("SELECT u.username FROM users as u where u.username=?", ('Halil', )))
#     print(g.user)
#     return jsonify(query_db("SELECT * FROM users"))
#     return jsonify(init_db())
