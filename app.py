# Standard Lib
from os import urandom
from uuid import uuid4
# Flask Lib
from flask import Flask, g, session, redirect, url_for, render_template, request
import sqlite3
# Custom Modules
from utl.dbconn import conn_db, close_db, makeUsersTable, makeBlogTable
from utl.auth import get_hash, auth, register
from utl.dbfunc import insert, get, get_posts

# Initialize Flask app that stores a reference to a database file
app = Flask(__name__)
app.secret_key = urandom(32)
app.config.from_mapping(DATABASE = "data/database.db")

# Random Hash (TBI)
salt = "abcdef"

makeUsersTable()
makeBlogTable()
# Initialize the database
#with app.app_context():
 # conn_db()
#  with app.open_resource("schema.sql") as f:
#    g.db.executescript(f.read().decode("utf8"))
 # close_db()

# Invoke database connection before each request is processed
@app.before_request
def database_connection():
  conn_db()
  try:
    g.usrname = request.args["username"]
    g.passwd = request.args["password"]
    g.creds = len(g.usrname) and len(g.passwd)
  except:
    pass

# Terminate database connection after each request is processed
@app.teardown_request
def close_database_connection(Exception):
  close_db()
  try:
    g.pop("usrname", None)
    g.pop("passwd", None)
    g.pop("creds", None)
  except:
    pass

# Redirects the viewer to the appropriate route
@app.route("/")
def index():
  if "usr" in session:
    return redirect(url_for("home"))
  return redirect(url_for("login"))

def loggedin(username, password):
    DB_FILE = "data/databases.db"
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()
    command = "SELECT userid, username FROM users WHERE username = \"{}\" AND hash_passwd = \"{}\";".format(username, password)
    cur.execute(command)
    q = cur.fetchall()
    db.commit() #save changes
    db.close()  #close database
    if get_hash(salt, password) == :
        return True
    else:
        return false

# Authenticates the user
@app.route("/login")
def login():
  if "usr" in session:
    return redirect(url_for("home"))
  if "creds" in g:
    try:
      assert g.usrname, "No Username Entered"
      assert g.passwd, "No Password Entered"
      if loggedin(g.usrname, g.passwd):
        session["usr"] = request.args["username"]
        return redirect(url_for("home"))
      return render_template("login.html", error = "Invalid Credentials")
    except AssertionError as ae:
      return render_template("login.html", error = str(ae.args[0]))
  return render_template("login.html")

# Allow the view to signup
@app.route("/signup")
def signup():
  if "creds" in g:
    try:
      assert g.usrname, "No Username Entered"
      assert g.passwd, "No Password Entered"
      if register(g.usrname, g.passwd):
        session["usr"] = request.args["username"]
        return redirect(url_for("home"))
      return render_template("signup.html", error = "User Already Exist")
    except AssertionError as ae:
      return render_template("login.html", error = str(ae.args[0]))
  return render_template("signup.html")

# Displays the home for logged in user
@app.route("/home")
def home():
  if "usr" in session:
    return render_template("home.html")
  return(redirect(url_for("")))


#get_posts()


# Executes the Flask app if this file is the main file
if __name__ == "__main__":
  app.run(debug=True)
