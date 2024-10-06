import sqlite3
import csv
import pandas as pd
with sqlite3.connect('tests/dbs/homes_by_city.db') as conn:
    pd.read_sql('select * from api', conn).to_csv('test.csv', index=False)