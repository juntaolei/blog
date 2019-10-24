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
    g.db.execute('INSERT INTO %s VALUES (%s)' % (tbl_name, ",".joing(values)))
    g.db.commit()
    return True
  except:
    return False

def get(tbl_name, query, identifier):
  cur = g.db.cursor()
  cur.execute('SELECT %s FROM %s WHERE %s = %s' % (query, tbl_name, identifier))
  values = cur.fetchall()
  cur.close()
  return ",".join([value for value in values])