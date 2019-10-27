# Standard Lib
from os import urandom, path
from uuid import uuid4
# Flask Lib
from flask import Flask, g, session, redirect, url_for, render_template, request

# Custom Modules
from utl.dbconn import conn, close
from utl.auth import get_hash, auth, register
from utl.dbfunc import insert, get
from utl.edit import create_post, delete_post, update_post

# Initialize Flask app that stores a reference to a database file and the salt
app = Flask(__name__)
app.secret_key = urandom(32)
if not path.exists("data/database.db"):
    with open("data/database.db", "w+") as f:
        f.close()
app.config.from_mapping(DATABASE="data/database.db")

# Initialize the database
with app.app_context():
    conn()
    with app.open_resource("schema.sql") as f:
        g.db.executescript(f.read().decode("utf8"))
    existing_salt = get("storedsalt", "salt", "WHERE id = 0")
    if not existing_salt:
        salt = str(uuid4())
        insert("storedsalt", [0, salt])
        app.config.from_mapping(SALT=salt)
    else:
        app.config.from_mapping(SALT=existing_salt[0][0])
    close()

# Invoke database connection before each request is processed
@app.before_request
def database_connection():
    conn()
    try:
        g.username = request.args["username"]
        g.password = request.args["password"]
        g.creds = g.username and g.password
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
    if "isloggedin" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

# Authenticates the user
@app.route("/login")
def login():
    if "isloggedin" in session:
        return redirect(url_for("home"))
    if "creds" in g:
        try:
            assert g.username, "No Username Entered"
            assert g.password, "No Password Entered"
            if auth(g.username, g.password):
                session["isloggedin"] = True
                session["username"] = g.username
                session["userid"] = str(get("users", "userid", "WHERE username = '%s'" % g.username)[0][0])
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
            assert not get("users", "username", "WHERE username = '%s'" % g.username), "Username Already Used"
            assert g.password, "No Password Entered"
            assert g.password == request.args["confirm"], "Password Does Not Match"
            if register(g.username, g.password, request.args["displayname"]):
                session["isloggedin"] = True
                session["username"] = g.username
                session["userid"] = str(get(
                    "users", "userid", "WHERE username = '%s'" % g.username)[0][0])
                return redirect(url_for("home"))
            return render_template("signup.html", error="Registration Failed")
        except AssertionError as ae:
            return render_template("signup.html", error=str(ae.args[0]))
    return render_template("signup.html")

# Display the home for logged in user
@app.route("/home")
def home():
    if "isloggedin" in session:
        collection = get("users", "userid, displayname")
        return render_template("home.html", collection=collection)
    return redirect("/")

# Display blog of logged in user
@app.route("/myblog")
def myblog():
    if "isloggedin" in session:
        return redirect(url_for("user", userid = session["userid"]))
    return redirect("/")


# Display the blog for each user
@app.route("/<userid>")
def user(userid):
    if "isloggedin" in session:
        selected_user = get("users", "displayname", "WHERE userid = '%s'" % userid)[0][0]
        collection = get("blogs", "title, blogid",
                          "WHERE userid = '%s'" % userid)
        if userid != session["userid"]:
            return render_template("blog.html", canedit = False, userid=userid ,user = selected_user, collection = collection)
        return render_template("blog.html", canedit = True, userid=userid, user=selected_user, collection = collection)
    return redirect("/")

# Display the entry for each user's blog
@app.route("/<userid>/<blogid>")
def post(userid, blogid):
    if "isloggedin" in session:
        author = get("blogs", "author", "WHERE blogid = '%s'" % blogid)[0][0]
        title = get("blogs", "title", "WHERE blogid = '%s'" % blogid)[0][0]
        content = get("blogs", "content", "WHERE blogid = '%s'" % blogid)[0][0]
        lastupdated = get("blogs", "lastupdated", "WHERE blogid = '%s'" % blogid)[0][0]
        if userid != session["userid"]:
            return render_template("post.html", canedit = False, title = title, content = content, author = author, lastupdated = lastupdated)
        return render_template("post.html", canedit = True, userid = userid, blogid = blogid, content = content, author = author, title = title, lastupdated = lastupdated)
    return redirect("/")


@app.route("/<userid>/<blogid>/update")
def update(userid, blogid = "new"):
    if "isloggedin" in session:
        try:
            assert request.args["newTitle"], "No Title Entered"
            author = get("users", "displayname",
                         "WHERE username = '%s'" % session["username"])[0][0]
            title = request.args["newTitle"]
            content = request.args["newContent"]
            if blogid == "new":
                blogid = create_post(userid, author, title, content)
            else:
                update_post(blogid, content)
            return redirect(url_for("post", userid = userid, blogid = blogid))
        except AssertionError as ae:
            return render_template("edit.html", error=str(ae.args[0]))
    return redirect("/")

@app.route("/<userid>/new/edit")
@app.route("/<userid>/<blogid>/edit")
@app.route("/<userid>/<blogid>/edit?t=<title>&c=<content>")
def edit(userid, blogid = "new", title = "", content = ""):
    if "isloggedin" in session:
        if userid != session["userid"]:
            return render_template("edit.html", canedit = False)
        return render_template("edit.html", canedit = True, userid = userid, blogid = blogid, title = title, content = content)
    return redirect("/")


@app.route("/<userid>/<blogid>/delete")
def delete(userid, blogid):
    if "isloggedin" in session and userid == session["userid"]:
        delete_post(blogid)
    return redirect("/")

# Logout the user
@app.route("/logout")
def logout():
    if "isloggedin" in session:
        session.pop("username", None)
        session.pop("userid", None)
        session.pop("isloggedin", None)
    return redirect("/")


# Executes the Flask app if this file is the main file
if __name__ == "__main__":
    app.run(debug=True)
