"""
DB Abstraction layer
"""

import sqlite3
from flask import g
from english_exercises.dbconnector import *

def check_login(username, password):
    user = query_db("SELECT * FROM users WHERE username==? AND password ==?;", (username, password, ), 1)
    if user is None:
        return False
    else:
        if username == user['username'] and password == user['password']:
            return True

def register_user(username, password):
    # query = """
    # INSERT INTO users 
    # VALUES (%(u)s, %(p)s, 0, 0)
    # """ % {'u' : username, 'p' : password}

    if query_db("SELECT u.username FROM users as u where u.username=?", (username,)) is not None:
        res = query_db("INSERT INTO users (username, password, correct, incorrect) VALUES (?, ?, 0, 0)", (username, password, ))
        print("register_user | "+str(res))
        return 1
    else: return 0
