import sqlite3
with sqlite3.connect('tests/dbs/urls.db') as conn:
    cur = conn.cursor()
    cur.execute("select * from urls where city='portland_ME'")
    rows = cur.fetchall()
    print(len(rows))
