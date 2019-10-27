# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import current_app, g

# User Modules
from .dbfunc import insert, get
uid = 0

def get_hash(password):
    return sha256((current_app.config["SALT"] + password).encode()).hexdigest()


def auth(username, password):
    try:
        hashpassword = get("users", "hashpassword",
                           "WHERE username = '%s'" % (username))[0][0]
        global uid
        uid = get("users", "userid",
                           "WHERE username = '%s'" % (username))[0][0]
        if get_hash(password) == hashpassword:
            return True
    except:
        pass
    return False


def register(username, password):
    if not auth(username, password):
        insert("users", ["NULL", username, get_hash(password), username])
        global uid
        uid = get("users", "userid",
                           "WHERE username = '%s'" % (username))[0][0]
    return True

def currentUser():
    global uid
    return uid
