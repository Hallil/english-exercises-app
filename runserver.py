"""
This script runs the webshop application using a development server.
"""
from flask import Flask
from os import environ
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "English Exercises :DDDDDD"

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

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
