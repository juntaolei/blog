import sqlite3
import csv

def displayEntry(userid):
    # give to templates

def displayEntries(userid):
    command = "SELECT blog_id, title FROM blogs INNER JOIN entries ON users.userid = blogs.userid WHERE blogs.userid = {};".format(blog_id)
    c.execute(command)
    q = c.fetchall()
