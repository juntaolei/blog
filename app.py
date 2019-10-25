# Standard Lib
from os import urandom, path
from uuid import uuid4
# Flask Lib
from flask import Flask, g, session, redirect, url_for, render_template, request

# Custom Modules
from utl.dbconn import conn, close
from utl.auth import get_hash, auth, register
from utl.dbfunc import insert, get

# Initialize Flask app that stores a reference to a database file and the salt
app = Flask(__name__)
app.secret_key = urandom(32)
if not path.exists("data/database.db"):
    with open("data/database.db", "w+") as f:
        f.close()
app.config.from_mapping(DATABASE="data/database.db", SALT="abcdef")

# Initialize the database
with app.app_context():
    conn()
    with app.open_resource("schema.sql") as f:
        g.db.executescript(f.read().decode("utf8"))
    close()

# Invoke database connection before each request is processed
@app.before_request
def database_connection():
    conn()
    try:
        g.username = request.args["username"]
        g.password = request.args["password"]
        g.creds = len(g.username) and len(g.password)
    except:
        pass

# Terminate database connection after each request is processed
@app.teardown_request
def close_database_connection(Exception):
    close()
    try:
        g.pop("username", None)
        g.pop("password", None)
        g.pop("creds", None)
    except:
        pass

# Redirects the viewer to the appropriate route
@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

# Authenticates the user
@app.route("/login")
def login():
    if "user" in session:
        return redirect(url_for("/home"))
    if "creds" in g:
        try:
            assert g.username, "No Username Entered"
            assert g.password, "No Password Entered"
            if auth(g.username, g.password):
                session["user"] = g.username
                return redirect(url_for("home"))
            return render_template("login.html", error="Invalid Credentials")
        except AssertionError as ae:
            return render_template("login.html", error=str(ae.args[0]))
    return render_template("login.html")

# Allow the view to signup
@app.route("/signup")
def signup():
    if "creds" in g:
        try:
            assert g.username, "No Username Entered"
            assert g.password, "No Password Entered"
            if register(g.username, g.password):
                session["user"] = g.username
                return redirect(url_for("home"))
            return render_template("signup.html", error="User Already Exist")
        except AssertionError as ae:
            return render_template("login.html", error=str(ae.args[0]))
    return render_template("signup.html")

# Display the home for logged in user
@app.route("/home")
def home():
    if "user" in session:
        collection = zip(get("users", "displayname").split(
            ","), get("users", "userid").split(","))
        return render_template("home.html", collection=collection)
    return redirect("/")

# Display the blog for each user
@app.route("/<userid>")
def user(userid):
    if "user" in session:
        collections = get("blogs", "title, userid",
                          "WHERE userid = %s" % userid).split(",")
        return render_template("blog.html", user=session["user"], collections=collections)
    return redirect("/")

# Display the entry for each user's blog
@app.route("/<userid>/<blogid>")
def blog(userid, blogid):
    if "user" in session:
        return render_template("post.html")
    return redirect("/")

# Logout the user
@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
    return redirect("/")


# Executes the Flask app if this file is the main file
if __name__ == "__main__":
    app.run(debug=True)
