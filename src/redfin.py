# libs
from _usr_libs import *

# class: redfin headless chrome browser
class RedfinHeadlessChromeBrowser():
    def __init__(self, 
                 download_dir: str, EMAIL: str, PASSWORD: str) -> None:
        self.user_agent ='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.download_dir = download_dir
        self.EMAIL = EMAIL; self.PASSWORD = PASSWORD

    def _set_up_browser(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f"user-agent={self.user_agent}")
        chrome_options.add_argument("--headless")
        prefs = {"download.default_directory": self.download_dir, 
                 "download.directory_upgrade": True, 
                 "download.prompt_for_download": False}
        chrome_options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=chrome_options)

        return browser