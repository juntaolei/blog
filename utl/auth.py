# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import current_app, g

# User Modules
from .dbfunc import insert, get


def get_hash(password):
    return sha256((current_app.config["SALT"] + password).encode()).hexdigest()


def auth(username, password):
    try:
        hashpassword = get("users", "hashpassword",
                           "WHERE username = '%s'" % username)[0][0]
        if get_hash(password) == hashpassword:
            return True
    except:
        return False


def register(username, password, displayname):
    if not auth(username, password):
        if not displayname:
            displayname = username
        insert("users", ["NULL", username, get_hash(password), displayname])
    return True
