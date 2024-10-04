# libs
from _usr_libs import *

# class: redfin headless chrome browser
class RedfinHeadlessChromeBrowser():
    def __init__(self, 
                 download_dir: str, EMAIL: str, PASSWORD: str) -> None:
        self.user_agent ='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.download_dir = download_dir
        self.EMAIL = EMAIL; self.PASSWORD = PASSWORD
        self.homepage_url = "https://www.redfin.com"

    def _set_up_browser(self) -> None:
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f"user-agent={self.user_agent}")
        chrome_options.add_argument("--headless")
        prefs = {"download.default_directory": self.download_dir, 
                 "download.directory_upgrade": True, 
                 "download.prompt_for_download": False}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.get(self.homepage_url)
        time.sleep(5)

    def _log_in(self):
        self._set_up_browser()
        # begin logging
        self.browser.find_element(By.XPATH, "//span[text()='Join / Sign in']/..").click()
        
        # email
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//input[@name='emailInput']").send_keys(self.EMAIL)
        self.browser.find_element(By.XPATH, "//span[text()='Continue with Email']/..").click()

        # password
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//input[@name='passwordInput']").send_keys(self.PASSWORD)
        self.browser.find_element(By.XPATH, "//span[text()='Continue with Email']/..").click()

    def start(self) -> None:
        self._set_up_browser()
        self._log_in()

    def quit(self) -> None:
        self.browser.quit()
    
    def return_homepage(self) -> None:
        self.browser.get(self.homepage_url)

    