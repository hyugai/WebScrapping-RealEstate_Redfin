from contextlib import redirect_stdout
import sys
import random
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

sys.path.append((Path.cwd()/'src').as_posix())
from redfin_conf import redfin 

def foo1() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=random.choice(redfin['headers'])['User-Agent'])
        page = context.new_page()
        
        page.goto(redfin['homepage'], wait_until="domcontentloaded")
        title = page.title()
        print(title)

        page.wait_for_timeout(100000)

