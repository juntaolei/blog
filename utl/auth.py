# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import g

def get_hash(salt, password):
  print(type(sha256((salt + password).encode()).hexdigest()))
  return sha256((salt + password).encode()).hexdigest()

def auth(password, salt, hashed):
  if get_hash(salt, password) == hashed:
    return True
  return False