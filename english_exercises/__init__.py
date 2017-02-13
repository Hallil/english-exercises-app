from os import environ
from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('static/index.html')

# Section for Rene
@app.route("/adverbs")
def adverbs():
    return "Adverbs Exercises :DDDDDD"

# Section for Eelco
@app.route("/gerund")
def gerund():
    return "Gerund Exercises :DDDDDD"

# Section for Halil
@app.route("/nouns")
def nouns():
    return "Nouns Exercises :DDDDDD"



HOST = environ.get('SERVER_HOST', 'localhost')
try:
    PORT = int(environ.get('SERVER_PORT', '5555'))
except ValueError:
    PORT = 5555
app.run(HOST, PORT, debug = True)
