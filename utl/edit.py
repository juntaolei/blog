# Flask Lib
from flask import g
# User Modules
from .dbfunc import insert, get


def create_post(userid, author, title, content):
    insert("blogs", ["NULL", userid, title,
                     author, content, "datetime('now')"])
    blogid = get("blogs", "blogid", "WHERE title = '%s'" % title)[0][0]
    return blogid


def update_post(blog_id, blog_content, time_stamp):
    cur = g.db.cursor()
    cur.execute(
        "UPDATE blogs SET content = blog_content, last_updated = time_stamp WHERE blogid = blog_id")
    g.db.commit()
    cur.close()


def delete_post(blogid):
    cur = g.db.cursor()
    cur.execute("DELETE FROM blogs WHERE blogid = '%s'" % blogid)
    g.db.commit()
