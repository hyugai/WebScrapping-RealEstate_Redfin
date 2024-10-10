# libs
from _libs import *

# class LogsTracker
class LogsTracker():
    def __init__(self, 
                 path_to_db: str) -> None:
        self.path_to_db = path_to_db

    # insert
    def insert(self,
                    city: str, url: str, status: int) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS logs(city TEXT UNIQUE, url TEXT, status INTEGER)")
            cur.execute("INSERT OR REPLACE INTO logs(city, url, status) VALUES(?, ?, ?)", (city, url, status))
            conn.commit(); cur.close()

    # update
    def update(self, 
               city: str, status: int) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(f"UPDATE logs SET status={status} WHERE city='{city}'")
            conn.commit(); cur.close()

    # retrive case(s) bases on status
    def retrieve(self, 
                       status: int) -> list[tuple]:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT city, url FROM logs WHERE status={status}")
            rows = cur.fetchall()
            conn.commit(); cur.close()
        if rows:
            return rows
        else:
            raise Exception("There is no any failed cases!")
    
# class CityTracker
class CityTracker():
    def __init__(self, 
                 path_to_db: str) -> None:
        self.path_to_db = path_to_db
    
    # create table
    def create_table(self, 
               table_name: str,
               uniq_column: str, columns: tuple):
        with sqlite3.connect(self.path_to_db) as conn:
            # create table 
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({uniq_column} TEXT UNIQUE)"); conn.commit()
            
            # existing columns
            cur.execute(f"PRAGMA table_info({table_name})")
            table_info = cur.fetchall(); conn.commit()
            existing_columns = [row[1] for row in table_info]

            # add columns
            for column in columns:
                if column not in existing_columns:
                    cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {column}"); conn.commit()
                else:
                    continue
            
            # close
            cur.close()
    
    # insert 
    def insert(self, 
               table_name: str,
               features: tuple, row: tuple) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(f"INSERT OR REPLACE INTO {table_name}{features} VALUES{row}")
            conn.commit(); cur.close()

# class URL tracker
class URLTracker():
    def __init__(self, 
                 path_to_db: str) -> None:
        self.path_to_db = path_to_db

    def insert(self, 
               city: str, url: str, csv_download_link: str) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS urls(city TEXT UNIQUE, url TEXT, csv_download_link TEXT)")
            cur.execute(f"INSERT OR REPLACE INTO urls(city, url, csv_download_link) VALUES(?, ?, ?)", (city, url, csv_download_link))
            conn.commit(); cur.close()

    def retrive(self, csv_download_link_IS_NULL: bool=True) -> list[tuple]:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            if csv_download_link_IS_NULL:
                cur.execute("SELECT city, url FROM urls WHERE csv_download_link IS NULL")
                rows = cur.fetchall(); conn.commit()

                return rows
            else:
                cur.execute("SELECT city, csv_download_link FROM urls WHERE csv_download_link IS NOT NULL")
                rows = cur.fetchall()

                return rows