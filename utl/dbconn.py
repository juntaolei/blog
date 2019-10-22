from sqlite3 import connect
from flask import current_app, g

@app.before_request
def conn():
	if "db" not in g:
		g.db = connect(current_app.config["DATABASE"])
	return g.db

@app.teardown_request
def terminate():
	db = getattr(g, "db", None)
	if db is not None:
		db.close()
