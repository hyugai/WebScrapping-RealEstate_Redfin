# libs
import os, sys
cwd = os.getcwd()
os.chdir('src/'); path_to_src = os.getcwd()
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from _libs import *
from _usr_libs import *

# exp
db_path = cwd + "/tests/dbs/homes_by_city.db"
csv_path = {'api': cwd + "/resource/data/api.csv", 
            'html': cwd + "/resource/data/html.csv"}
csv_extractor = CSVExtractor(db_path, csv_path, table='both')
csv_extractor.extract()