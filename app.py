# Standard Lib
from os import urandom
from uuid import uuid4
# Flask Lib
from flask import Flask, g, session, redirect, url_for, render_template, request

# Custom Modules
from utl.dbconn import conn, close
from utl.auth import auth

# Initialize Flask app that stores a reference to a database file
app = Flask(__name__)
app.secret_key = urandom(32)
app.config.from_mapping(DATABASE = "data/database.db")

# Random hash
app_hash = uuid4().hex

# Initialize the database
with app.app_context():
  conn()
  with app.open_resource("schema.sql") as f:
    g.db.executescript(f.read().decode('utf8'))
  close()

# Invoke database connection before each request is processed
@app.before_request
def database_connection():
  conn()

# Terminate database connection after each request is processed
@app.teardown_request
def close_database_connection(ex):
  close()

# Redirects the viewer to the appropriate route
@app.route("/")
def index():
  if "usr" in session:
    return redirect(url_for("home"))
  return redirect(url_for("login"))

# Authenticates the user
@app.route("/login")
def login():
  if "usr" in session:
    return redirect(url_for("/home"))
  if request.args:
    try:
      assert request.args["username"], "No Username Entered"
      assert request.args["password"], "No Password Entered"
      if auth(g.db):
        session["usr"] = request.args["username"]
        return redirect(url_for("home"))
    except AssertionError:
      return render_template("login.html", error = AssertionError.__str__)
  return render_template("login.html")
    
# Allow the view to signup
@app.route("/signup")
def signup():
  if request.args:
    try:
      assert request.args["username"], "No Username Entered"
      assert request.args["password"], "No Password Entered"
      g.db.execute("INSERT INTO users (username, password) VALUES ({0}, {1})".format(request.args["username"], hash(request.args["password"])))
      session["usr"] = request.args["username"]
      return redirect(url_for("home"))
    except AssertionError:
      return render_template("signup.html", error = AssertionError.__str__)
  return render_template("signup.html")

# Displays the home for logged in user
@app.route("/home")
def home():
  if "usr" in session:
    return render_template("home.html")
  return(redirect(url_for("")))

# Executes the Flask app if this file is the main file
if __name__ == "__main__":
  app.run(debug=True)
