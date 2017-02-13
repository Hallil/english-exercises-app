from os import environ
from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# Section for Rene
@app.route("/adverbs")
@app.route("/adverbs/<level>")
def adverbs(level=None):
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
