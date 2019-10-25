# Flask Lib
from flask import g


def header_types(tbl_name):
    cur = g.db.cursor()
    cur.execute("PRAGMA TABLE_INFO (%s)" % (tbl_name))
    heads = cur.fetchall()
    cur.close()
    return [str(head[1]) for head in heads]


def insert(tbl_name, values):
    try:
        cur = g.db.cursor()
        cur.execute("INSERT INTO %s VALUES (NULL,'%s')" %
                    (tbl_name, "','".join(values)))
        g.db.commit()
        return True
    except:
        return False


def get(tbl_name, column, conditional=""):
    cur = g.db.cursor()
    print("SELECT %s FROM %s %s" % (column, tbl_name, conditional))
    cur.execute("SELECT %s FROM %s %s" % (column, tbl_name, conditional))
    values = cur.fetchall()
    cur.close()
    return ",".join([str(value[0]) for value in values])
