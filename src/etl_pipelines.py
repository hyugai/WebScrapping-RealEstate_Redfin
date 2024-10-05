# libs
from _libs import *
from trackers import URLTracker, CityTracker, LogsTracker
from redfin import RedfinHeadlessChromeBrowser

# scrap urls from official website of each city
class URLScrapper():
    def __init__(self, 
                 path_to_tmp: str, 
                 url_tracker: URLTracker, redfin: RedfinHeadlessChromeBrowser) -> Iterator[tuple]:
        self.path_to_tmp = path_to_tmp
        self.url_tracker = url_tracker
        self.redfin = redfin
    def extract(self):
        self.redfin.start()
        parent_node_div = self.redfin.browser.find_element(By.XPATH, "//span[text()='Search for homes by city']/parent::div")
        try:
            child_node_div_button = parent_node_div.find_element(By.XPATH, "./descendant::span[text()='Show more']/parent::div")
            child_node_div_button.click()
        except:
            pass
        descendant_nodes_li = parent_node_div.find_elements(By.XPATH, "./child::ul/child::li")

        city = dict()
        for node in descendant_nodes_li:
            node_a = node.find_element(By.XPATH, "./child::a")
            name = node_a.text
            url = node_a.get_attribute("href")
            city[name] = url

        for name, url in city.items():
            self.redfin.browser.get(url); time.sleep(5)
            try:
                csv_download_link = self.redfin.browser.find_element(By.XPATH, "//a[text()='(Download All)']")\
                    .get_attribute("href")
                yield name, url, csv_download_link
            except:
                yield name, url, None
        
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
        