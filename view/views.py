from flask import *

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')