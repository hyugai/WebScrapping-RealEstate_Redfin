import sqlite3
import csv
import pandas as pd
# with sqlite3.connect('tests/dbs/homes_by_city.db') as conn:
#     pd.read_sql('select * from api', conn).to_csv('test.csv', index=False)

# with sqlite3.connect('tests/dbs/homes_by_city.db') as conn:
#     df = pd.read_sql('select * from logs where status=1', conn)
#     print(df.shape)

a = {'x': [1, 2, 3], 'y': [4, 5, 6]}
print(a.values())
for i, j in zip(*a.values()):
    print(i, j)