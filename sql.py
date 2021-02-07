import sqlite3
db = sqlite3.connect('server.db')
sql =db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
login text,
v1 int,
v2 int,
v3 int,
v4 int,
v5 int,
v6 int,
v7 int,
v8 int,
)""")

db.commit()