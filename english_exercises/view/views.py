from flask import *
from . import app

@app.route("/")
def home():
    return "render_template('index.html')"

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
