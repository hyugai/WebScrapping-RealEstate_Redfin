import sqlite3
with sqlite3.connect('tests/dbs/urls.db') as conn:
    cur = conn.cursor()
    cur.execute("select * from urls")
    rows = cur.fetchall()
    print(rows)
    cur.close()