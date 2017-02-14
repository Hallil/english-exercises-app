"""
DB Abstraction layer
"""

import sqlite3
from flask import g
from english_exercises.dbconnector import *

def check_login(username, password):
    #values komen terug als unicode! convert to ascii!
    user = query_db("SELECT * FROM users WHERE username==? AND password ==?;", (username, password, ), 1)
    for k, v in user.items():
        #column print(k)
        #value print(v)
        user[k] = str(v)
    #print(user)
    if user is None:
        return False
    else:
        if username == user['username'] and password == user['password']:
            print("login checked: True")
            return True

def register_user(username, password):
    # query = """
    # INSERT INTO users 
    # VALUES (%(u)s, %(p)s, 0, 0)
    # """ % {'u' : username, 'p' : password}
    t = query_db("SELECT u.username FROM users as u where u.username=?", (username,)) 
    if t is None or t == []:
        res = query_db("INSERT INTO users (username, password, correct, incorrect) VALUES (?, ?, 0, 0)", (username, password, ))
        get_db().commit()
        print("register_user | "+str(res))
        return 1
    else: return 0