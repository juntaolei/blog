# Flask Lib
from flask import g
# User Modules
from .dbfunc import insert, get


def create_post(userid, author, title, content):
    insert("blogs", ["NULL", userid, author,
                     title, content, "datetime('now')"])
    blogid = get("blogs", "blogid", "WHERE title = '%s'" % title)[0][0]
    return blogid


def update_post(blog_id, blog_content):
    cur = g.db.cursor()
    cur.execute(
        "UPDATE blogs SET content = '%s', lastupdated = datetime('now') WHERE blogid = '%s'" % (blog_content, blog_id))
    g.db.commit()
    cur.close()


def delete_post(blogid):
    cur = g.db.cursor()
    cur.execute("DELETE FROM blogs WHERE blogid = '%s'" % blogid)
    g.db.commit()
