import sys
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

sys.path.append((Path.cwd()/'src').as_posix())
from src.redfin_conf import redfin 
