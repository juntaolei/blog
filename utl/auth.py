# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import g

def hash(password):
  return sha256(hex(userid) + password).hexdigest()

def auth(password, hash, stored_hash):
  if hash(userid, password) == stored_hash:
    return True
  return False