import sqlite3
import csv
import pandas as pd
with sqlite3.connect('tests/dbs/homes_by_city.db') as conn:
    pd.read_sql('select * from html', conn).to_csv('test.csv', index=False)
    # cur = conn.cursor()
    # cur.execute("drop table if exists html")

# with sqlite3.connect('tests/dbs/homes_by_city.db') as conn:
#     df = pd.read_sql('select * from logs where status=1', conn)
#     print(df.shape)

# a = {'x': [1, 2, 3], 'y': [4, 5, 6]}
# print(isinstance(a, dict))
# print(a.values())
# for row in zip(*a.values()):
#     print(row)

# print(tuple(a.keys()))