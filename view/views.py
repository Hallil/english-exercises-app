from flask import *
from . import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')