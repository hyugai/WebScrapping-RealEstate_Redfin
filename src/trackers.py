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
            cur.execute(f"INSERT OR REPLACE INTO logs VALUES('{city}', '{url}', {status})")
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

    def _check_table_existence(self, city: str) -> bool:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_schema WHERE type='table'")
            tables = [row[0] for row in cur.fetchall()]
            if city in tables: return True 
            else: return True
    
    def create_table(self, 
               city: str,
               uniq_column: str, columns: list):
        # check table's existence
        if self._check_table_existence(city):
            with sqlite3.connect(self.path_to_db) as conn:
                # create table 
                cur = conn.cursor()
                cur.execute(f"CREATE TABLE IF NOT EXISTS {city}({uniq_column} UNIQUE TEXT)"); conn.commit()
                
                # existing rows
                cur.execute(f"PRAGMA table_info({city})")
                table_info = cur.fetchall(); conn.commit()
                existing_columns = [row[1] for row in table_info]

                # add columns
                for column in columns:
                    if column not in existing_columns:
                        cur.execute(f"ALTER TABLE {city} ADD COLUMN {column}"); conn.commit()
                
                # close
                cur.close()
        else:
            pass
    
    def insert(self, 
               city: str, row: dict) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(f"INSERT OR REPLACE INTO {city}{tuple(row.keys())} VALUES{tuple(row.values())}")
            conn.commit()

