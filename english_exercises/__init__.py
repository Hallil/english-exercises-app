import os
from os import environ
from flask import *
import sqlite3

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'sqlite3.db'),
    SECRET_KEY='development key'
))

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
        db = get_db()
        db.execute("INSERT INTO users (username, password, correct, incorrect) VALUES (?, ?, 0, 0);",
                     [request.form['username'], request.form['password']])
        db.commit()
        flash('New entry was successfully posted')
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


def check_login(username, password):
    user = query_db("SELECT * FROM users WHERE username==?;", [username], 1)
    passw = query_db("SELECT * FROM users WHERE username==?;", [password], 2)
    if user or passw is None:
        return False
    else:
        if user == username and password == passw:
            return True


def query_db(query, i, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[i] if rv else None) if one else rv



def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


# Section for Eelco
@app.route("/gerund")
def gerund():
    return "Gerund Exercises :DDDDDD"


# Section for Halil
@app.route("/nouns")
def nouns():
    return "Nouns Exercises :DDDDDD"


# Section for Halil
@app.route("/results")
def results():
    return render_template('results.html')


HOST = environ.get('SERVER_HOST', 'localhost')
try:
    PORT = int(environ.get('SERVER_PORT', '5555'))
except ValueError:
    PORT = 5555
app.run(HOST, PORT, debug = True)
