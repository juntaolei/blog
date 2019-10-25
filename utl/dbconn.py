import sqlite3
# Standard Lib
from sqlite3 import connect
# Flask Lib
from flask import current_app, g

# Initialize a database connection
def conn_db():
  if "db" not in g:
	  g.db = connect(current_app.config["DATABASE"])

# Close an existing database connection
def close_db():
	db = getattr(g, "db", None)
	if db is not None:
		db.close()

def makeUsersTable():
    DB_FILE = "data/databases.db"
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
      userid INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      hash_passwd TEXT NOT NULL,
      displayname TEXT NOT NULL
    );""")
    db.commit() #save changes
    db.close()  #close database

def makeBlogTable():
    DB_FILE = "data/databases.db"
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS blogs(
      blog_id INTEGER PRIMARY KEY AUTOINCREMENT,
      userid INTEGER NOT NULL,
      auther TEXT NOT NULL,
      title TEXT NOT NULL,
      FOREIGN KEY (userid) REFERENCES users (userid)
    );""")
    db.commit() #save changes
    db.close()  #close database
