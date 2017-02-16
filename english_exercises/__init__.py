import os
from os import environ
from flask import *
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'sqlite3.db'),
    SECRET_KEY='development key'
))
db_path = os.path.join(os.path.dirname(__file__), 'sqlite3.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

from english_exercises.dbconnector import *
#from english_exercises.dblayer import *
import english_exercises.views
import english_exercises.dblayer
