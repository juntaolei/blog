# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import current_app, g

# User Modules
from .dbfunc import insert, get


def get_hash(password):
    return sha256((current_app.config["SALT"] + password).encode()).hexdigest()


def auth(username, password):
    if get_hash(password) == get("users", "hashpassword", "WHERE username = '%s'" % (username)):
        return True
    return False


def register(username, password):
    if not auth(username, password):
        insert("users", [username, get_hash(password), username])
    return True
