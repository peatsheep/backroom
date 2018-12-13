import sqlite3
from flask import g

DATABASE = 'data/bloodborne.db'

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = dict_factory
  return db

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_weapons():
  pass

def get_armor():
  cur = get_db().cursor()
  cur.execute('SELECT * FROM attire;')
  return cur.fetchall()