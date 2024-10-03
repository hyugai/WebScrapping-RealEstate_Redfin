# libs
from _usr_libs import *
from trackers import LogsTracker

# scrap urls from official website of each city
class URLScrapper():
    def __init__(self) -> None:
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
        