# libs
from _usr_libs import *
from trackers import LogsTracker

# class CSVLoaderFromScrapping
class CSVLoaderFromScrapping():
    def __init__(self) -> None:
        pass

# class CSVLoaderFromAPI
class CSVLoaderFromAPI():
    def __init__(self, 
                 paths: dict, logs_tracker: LogsTracker) -> None:
        self.paths = paths
        self.logs_tracker = logs_tracker
        