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


from english_exercises.dbconnector import *
#from english_exercises.dblayer import *
import english_exercises.views
import english_exercises.dblayer