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
tmp_path = cwd + "/tests/tmp"

redfin = RedfinHeadlessChromeBrowser(tmp_path, EMAIL, PASSWORD)
url_tracker = URLTracker(urls_db_path)
url_scrapper = URLScrapper(tmp_path, url_tracker, redfin)
url_scrapper.transform()