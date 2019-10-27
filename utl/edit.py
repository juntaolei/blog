# Flask Lib
from flask import g
# User Modules
from .dbfunc import insert, get


def create_post(userid, author, title, content):
    try:
        insert("blogs", ["NULL", userid, author,
                         title, content, "datetime('now')"])
        blogid = get("blogs", "blogid", "WHERE title = '%s'" % title)[0][0]
        return blogid
    except:
        return False


def update_post(blog_id, blog_content):
    try:
        cur = g.db.cursor()
        cur.execute(
            "UPDATE blogs SET content = '%s', lastupdated = datetime('now') WHERE blogid = '%s'" % (blog_content, blog_id))
        g.db.commit()
        cur.close()
        return True
    except:
        return False


def delete_post(blogid):
    try:
        cur = g.db.cursor()
        cur.execute("DELETE FROM blogs WHERE blogid = '%s'" % blogid)
        g.db.commit()
        cur.close()
        return True
    except:
        return False
