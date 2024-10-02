# libs
from _usr_libs import *

# class LogsTracker
class LogsTracker():
    def __init__(self, 
                 path_to_db: str) -> None:
        self.path_to_db = path_to_db

    def insert_logs(self,
                    city: str, url: str, status: int) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS logs(city UNIQUE TEXT, url TEXT, status INTEGER)")
            cur.execute("INSERT INTO logs VALUES(?, ?, ?)", (city, url, status))
            conn.commit(); cur.close()

    def update(self, 
               city: str, status: int) -> None:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE logs SET status=? WHERE city=?", (status, city))
            conn.commit(); cur.close()

    def retrieve_cases(self, 
                       status: int) -> tuple[str, str]:
        with sqlite3.connect(self.path_to_db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT city, url FROM logs WHERE status=?", (status,))
            rows = cur.fetchall()
            conn.commit(); cur.close()

        return rows
