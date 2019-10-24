# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import g

# User Modules
from . import dbfunc

def get_hash(salt, password):
  return sha256((salt + password).encode()).hexdigest()

def auth(password, salt, hashed):
  if get_hash(salt, password) == hashed:
    return True
  return False

def register(usrname, passwd):
  return True