import sqlite3
with sqlite3.connect('../resource/data/api.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_schema WHERE type='table'")
    conn.commit()
    rows = [name[0] for name in cur.fetchall()]
    print(rows[0])
    cur.close()
