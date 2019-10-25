# Standard Lib
import sqlite3
from hashlib import sha256
# Flask Lib
from flask import g
from utl.dbconn import conn_db, close_db

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
