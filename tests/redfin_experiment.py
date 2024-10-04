# libs
import os, sys
cwd = os.getcwd()
os.chdir('src/')
path_to_src = os.getcwd(); os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from _usr_libs import *
from redfin_config import EMAIL, PASSWORD
from redfin import RedfinHeadlessChromeBrowser

# test
print(cwd)
os.chdir('tests/dbs'); download_dir = os.getcwd()
os.chdir(cwd)
redfin = RedfinHeadlessChromeBrowser(download_dir, EMAIL, PASSWORD)
redfin._set_up_browser()

