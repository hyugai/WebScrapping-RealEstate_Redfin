# libs
from _usr_libs import *

# class LogsTracker
class LogsTracker():
    def __init__(self, 
                 path_to_db: str) -> None:
        self.path_to_db = path_to_db

    def insert(self,
                    city: str, url: str, status: int) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS logs(city UNIQUE TEXT, url TEXT, status INTEGER)")
            cur.execute(f"INSERT INTO logs VALUES('{city}', '{url}', {status})")
            conn.commit(); cur.close()

    def update(self, 
               city: str, status: int) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(f"UPDATE logs SET status={status} WHERE city='{city}'")
            conn.commit(); cur.close()

    def retrieve(self, 
                       status: int) -> tuple[str, str]:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT city, url FROM logs WHERE status={status}")
            rows = cur.fetchall()
            conn.commit(); cur.close()

        return rows
    
# class CityTracker
class CityTracker():
    def __init__(self, 
                 path_to_db: str) -> None:
        self.path_to_db = path_to_db
    
    def insert(self, 
               city: str,
               uniq_column: str, columns: list):
        with sqlite3.connect(self.path_to_db) as conn:
            # create table 
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE IF NOT EXISTS {city}({uniq_column} UNIQUE TEXT)")
            
            # existing rows
            cur.execute(f"PRAGMA table_info({city})")
            table_info = cur.fetchall()
            existing_columns = [row[1] for row in table_info]

            # add columns
            