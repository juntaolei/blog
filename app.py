# Standard library
from os import urandom
from flask import Flask, g

# Custom Modules
from utl.dbconn import conn, close

# Initialize Flask app that stores a reference to a database file
app = Flask(__name__)
app.secret_key = urandom(32)
app.config.from_mapping(DATABASE = "data/database.db")

# Invoke database connection before each request is processed
@app.before_request
def database_connection():
  conn()

# Terminate database connection after each request is processed
@app.teardown_request
def close_database_connection(ex):
  close()

# Testing at the moment
@app.route("/")
def index():
  cur = g.db
  print(cur)
  return "index"

# Executes the Flask app if this file is the main file
if __name__ == "__main__":
  app.run(debug=True)
