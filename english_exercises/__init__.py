import os
from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'sqlite3.db'),
    SECRET_KEY='development key'))

db_path = os.path.join(os.path.dirname(__file__), 'sqlite3.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

import english_exercises.views
import english_exercises.authentication
