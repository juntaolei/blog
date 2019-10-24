# Flask Lib
from flask import g

def header_types(tbl_name):
  cur = g.db.cursor()
  cur.execute("PRAGMA TABLE_INFO ({0})".format(tbl_name))
  heads = cur.fetchall()
  cur.close()
  return [str(head[1]) for head in heads]

def insert(tbl_name, values):
  try:
    g.db.execute("INSERT INTO {0} (id, username, passwd) VALUES (1, '{1}')".format(tbl_name, "','".join(values)))
    print("asdf")
    g.db.commit()
    return True
  except:
    return False

def get(tbl_name, query, identifier):
  cur = g.db.cursor()
  cur.execute("SELECT {0} FROM {1} WHERE {1}.passwd = '{2}'".format(query, tbl_name, identifier))
  values = cur.fetchall()
  for value in values:
    print(value)
  n = [value for value in values]
  print(n)
  if len(n) == 0:
    return ""
  return n