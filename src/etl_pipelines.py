# libs
from _libs import *
from trackers import URLTracker, CityTracker, LogsTracker
from redfin import RedfinHeadlessChromeBrowser

# scrap urls from official website of each city
class URLScrapper():
    def __init__(self, 
                 paths: dict, 
                 url_tracker: URLTracker, redfin: RedfinHeadlessChromeBrowser) -> None:
        self.path_to_db = paths
        self.url_tracker = url_tracker
        self.redfin = redfin
         
    def extract(self):
        pass
    def transform(self):
        pass
    def load(self):
        pass

# scrap homes data from official website
class HomeWebScrapper():
    def __init__(self) -> None:
        pass

# scrap homes data from API
class HomeAPIScrapper():
    def __init__(self, 
                 paths: dict, logs_tracker: LogsTracker) -> None:
        self.paths = paths
        self.logs_tracker = logs_tracker
        