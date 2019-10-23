# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import g

def hash(userid, password):
  return sha256(hex(userid) + password).hexdigest()

def auth(userid, password, hash):
  if hash(userid, password) == hash:
    return True
  return False