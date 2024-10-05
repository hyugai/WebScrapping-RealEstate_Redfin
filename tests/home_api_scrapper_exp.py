# libs
import os, sys
cwd = os.getcwd()
os.chdir('src/'); path_to_src = os.getcwd()
os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from _libs import *
from _usr_libs import *

# exp
urls_db_path = cwd + "/tests/dbs/urls.db"
api_db_path = cwd + "/tests/dbs/api.db"
tmp_path = cwd + "/tests/tmp"

logs_tracker = LogsTracker(api_db_path)
city_tracker = CityTracker(api_db_path)
url_tracker = URLTracker(urls_db_path)
redfin = RedfinHeadlessChromeBrowser(tmp_path, EMAIL, PASSWORD)
home_api_scrapper = HomeAPIScrapper(tmp_path, logs_tracker, city_tracker, url_tracker, redfin)
