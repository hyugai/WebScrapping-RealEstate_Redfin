# libs
from _libs import *
from trackers import URLTracker, CityTracker, LogsTracker
from redfin import RedfinHeadlessChromeBrowser

# scrap urls from official website of each city
class URLScrapper():
    def __init__(self, 
                 url_tracker: URLTracker, redfin: RedfinHeadlessChromeBrowser) -> Iterator[tuple]:
        self.url_tracker = url_tracker
        self.redfin = redfin

    def extract(self) -> Iterator[tuple[str, str, str]]:
        self.redfin.start()
        parent_node_div = self.redfin.browser.find_element(By.XPATH, "//span[text()='Search for homes by city']/parent::div")
        try:
            child_node_div_button = parent_node_div.find_element(By.XPATH, "./descendant::span[text()='Show more']/parent::div")
            child_node_div_button.click()
        except:
            pass
        descendant_nodes_li = parent_node_div.find_elements(By.XPATH, "./child::ul/child::li")

        cities = list()
        for node in descendant_nodes_li:
            node_a = node.find_element(By.XPATH, "./child::a")
            name = node_a.text
            url = node_a.get_attribute("href")
            cities.append((name, url))

        for name, url in cities:
            self.redfin.browser.get(url); time.sleep(5)
            try:
                csv_download_link = self.redfin.browser.find_element(By.XPATH, "//a[text()='(Download All)']")\
                    .get_attribute("href")
                yield name, url, csv_download_link
            except:
                yield name, url, None
        
    def transform(self) -> Iterator[tuple[str, str, str]]:
        for city, url, csv_dowload_link in self.extract():
            state = re.search(r'[A-Z]{2}', url).group()
            city = city.lower().strip()\
                .replace(' real estate', '').replace(',', '').replace('.', '').replace(' ', '_')
            full_name = f"{city}_{state}"
            yield full_name, url, csv_dowload_link

    def load(self):
        for full_name, url, csv_download_link in self.transform():
            print(full_name)
            self.url_tracker.insert(full_name, url, csv_download_link)

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
                 tmp_path: str,
                 logs_tracker: LogsTracker, city_tracker: CityTracker,
                 url_tracker: URLTracker, redfin: RedfinHeadlessChromeBrowser) -> None:
        self.tmp_path = tmp_path
        self.logs_tracker = logs_tracker
        self.city_tracker = city_tracker
        self.url_tracker = url_tracker
        self.redfin = redfin

    def extract(self):
        rows = self.url_tracker.retrive(False)
        self.redfin.start()
        for name, csv_download_link in rows:
            self.redfin.browser.get(csv_download_link); time.sleep(3)
            file_name = os.listdir(self.tmp_path)[0]
            with open(f"{self.tmp_path}/{file_name}", 'r+') as f:
                rows = list(csv.reader(f, delimiter=','))
            if rows <= 1:
                self.logs_tracker.insert(name, csv_download_link, 0)
                continue
            else:
                yield name, csv_download_link, rows

    def transform(self):
        pass
    def load(self):
        pass
        