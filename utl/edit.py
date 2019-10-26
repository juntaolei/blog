# User Modules
from .dbfunc import insert, get
from flask import g

def create_post(userid):
    auth = get("users", "username", "WHERE userid = %s" % userid)
    insert("blogs", [userid, auth])
    blog_id = get("blogs", "blogid", "WHERE title = %s" % NULL)
    return blog_id

def update_post(blog_id, blog_title, blog_content, time_stamp):
    cur = g.db.cursor()
    cur.execute("UPDATE blogs SET title = blog_title, content = blog_content, last_updated = time_stamp WHERE blogid = blog_id")
    g.db.commit()

def delete_post(id):
    cur = g.db.cursor()
    cur.execute("DELETE FROM blogs WHERE blogid = '{}';".format(id))
    g.db.commit()
