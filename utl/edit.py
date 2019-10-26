# User Modules
from .dbfunc import insert, get
from flask import g

def create_post(user_id, author):
    insert("blogs", [user_id, author])

def update_post(blog_id, blog_title, blog_content, time_stamp):
    cur = g.db.cursor()
    cur.execute("UPDATE blogs SET title = blog_title, content = blog_content, last_updated = time_stamp WHERE blogid = blog_id")
    g.db.commit()

def delete_post(id):
    cur = g.db.cursor()
    cur.execute("DELETE FROM blogs WHERE blogid = '{}';".format(id))
    g.db.commit()
