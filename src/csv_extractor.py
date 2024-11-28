# libs
from _libs import *

# class csv extractor
class CSVExtractor():
    def __init__(self, 
                 db_path: str, csv_path: str | dict,
                 table: Literal['both','api','html']):
        self.db_path = db_path
        self.csv_path = csv_path
        self.table = table
    
    def extract(self):
        with sqlite3.connect(self.db_path) as conn:
            if self.table != 'both':
                pd.read_sql(f"SELECT * FROM {self.table}", conn)\
                    .to_csv(self.csv_path, index=False)
                conn.commit(); 
            else:
                names = ['api', 'html']
                for name in names:
                    pd.read_sql(f"SELECT * FROM {name}", conn)\
                        .to_csv(self.csv_path[name], index=False)
                    conn.commit()