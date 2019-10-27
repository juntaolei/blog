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


def update_post(blogid, blogcontent, blogtitle):
    try:
        cur = g.db.cursor()
        cur.execute(
            "UPDATE blogs SET content = '%s', lastupdated = datetime('now'), title='%s' WHERE blogid = '%s'" % (
                blogcontent, blogtitle, blogid
            )
        )
        g.db.commit()
        cur.close()
        return True
    except:
        return False


def update_user(username, field, newvalue):
    try:
        cur = g.db.cursor()
        print("UPDATE users SET %s = '%s' WHERE username = '%s'" % (
            field,
            newvalue,
            username
        ))
        cur.execute(
            "UPDATE users SET %s = '%s' WHERE username = '%s'" % (
                field,
                newvalue,
                username
            )
        )
        g.db.commit()
        cur.close()
        return "Operation Successful"
    except:
        return "Error With Update"


def delete_post(blogid):
    try:
        cur = g.db.cursor()
        cur.execute("DELETE FROM blogs WHERE blogid = '%s'" % blogid)
        g.db.commit()
        cur.close()
        return True
    except:
        return False
