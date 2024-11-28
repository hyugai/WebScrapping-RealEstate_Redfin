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
scrapping_db_path = cwd + "/tests/dbs/homes_by_city.db"
url_db_path = cwd + "/tests/dbs/urls.db"
table_name = "html"
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
headers = {'User-Agent': user_agent}

logs_tracker = LogsTracker(scrapping_db_path)
city_tracker = CityTracker(scrapping_db_path)
url_tracker = URLTracker(url_db_path)
home_html_scrapper = HomeHTMLScrapper(table_name, headers, logs_tracker, city_tracker, url_tracker)
home_html_scrapper.load()