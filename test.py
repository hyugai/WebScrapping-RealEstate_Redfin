import sqlite3
import pandas as pd
with sqlite3.connect('tests/dbs/urls.db') as conn:
    pd.read_sql('select * from urls', conn).to_csv('test.csv', index=False)