# Standard Lib
from os import urandom
from uuid import uuid4
# Flask Lib
from flask import Flask, g, session, redirect, url_for, render_template, request as req

# Custom Modules
from utl.dbconn import conn, close
from utl.auth import get_hash, auth
from utl.dbfunc import insert, get

# Initialize Flask app that stores a reference to a database file
app = Flask(__name__)
app.secret_key = urandom(32)
app.config.from_mapping(DATABASE = "data/database.db")

# Random hash
salt = "abcdef"

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
  if req.args:
    try:
      assert req.args["username"], "No Username Entered"
      assert req.args["password"], "No Password Entered"
      print(get("users", "passwd", req.args["password"]))
      if auth(get("users", "username", req.args["username"]), salt, get("users", "passwd", req.args["password"])):
        session["usr"] = request.args["username"]
        return redirect(url_for("home"))
      return render_template("login.html", error = "Invalid Credentials")
    except AssertionError:
      return render_template("login.html", error = AssertionError.__str__)
  return render_template("login.html")
    
# Allow the view to signup
@app.route("/signup")
def signup():
  if req.args:
    try:
      assert req.args["username"], "No Username Entered"
      assert req.args["password"], "No Password Entered"
      print(insert("users", [req.args["username"], get_hash(salt, req.args["password"])]))
      session["usr"] = req.args["username"]
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
