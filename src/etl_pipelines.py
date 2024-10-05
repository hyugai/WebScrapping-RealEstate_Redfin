# libs
from _libs import *
from trackers import URLTracker, CityTracker, LogsTracker
from redfin import RedfinHeadlessChromeBrowser

# scrap urls from official website of each city
class URLScrapper():
    def __init__(self, 
                 path_to_tmp: str, 
                 url_tracker: URLTracker, redfin: RedfinHeadlessChromeBrowser) -> None:
        self.path_to_tmp = path_to_tmp
        self.url_tracker = url_tracker
        self.redfin = redfin
    def extract(self):
        self.redfin.start()
        parent_node = self.redfin.browser.find_element(By.XPATH, "//span[text()='Search for homes by city']/parent::div")
        try:
            button = parent_node.find_element(By.XPATH, "./descendant::span[text()='Show more']/parent::div")
            button.click()
        except:
            pass
        city = dict()
        city['nodes'] = parent_node.find_elements(By.XPATH, "./child::ul/child::li")

        for node in city['nodes'][:5]:
            child_node = node.find_element(By.XPATH, "./child::a")
            name = child_node.text; print(name)
        #     url = child_node.get_attribute("href")
        #     self.redfin.browser.get(url); time.sleep(5)
        #     try:
        #         csv_download_link = self.redfin.browser.find_element(By.XPATH, "//a[text()='(Download All)']")\
        #             .get_attribute("href")
        #         yield name, url, csv_download_link
        #     except:
        #         yield name, url, None
        
    def transform(self):
        for city, url, csv_dowload_link in self.extract():
            print(city)
    def load(self):
        pass

# scrap homes data from official website
class HomeWebScrapper():
    def __init__(self) -> None:
        pass
    def extract(self):
        pass
    def transform(self):
        pass
    def load(self):
        pass

# scrap homes data from API
class HomeAPIScrapper():
    def __init__(self, 
                 paths: dict, logs_tracker: LogsTracker) -> None:
        self.paths = paths
        self.logs_tracker = logs_tracker

    def extract(self):
        pass
    def transform(self):
        pass
    def load(self):
        pass
        