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

# scrap homes data from official website html
class HomeHTMLScrapper():
    def __init__(self, 
                 table_name: str, headers: dict,
                 logs_tracker: LogsTracker, city_tracker: CityTracker, 
                 url_tracker: URLTracker) -> None:
        self.table_name = table_name
        self.headers = headers
        self.redfin_homepage_url = "https://www.redfin.com/"
        self.logs_tracker = logs_tracker
        self.city_tracker = city_tracker
        self.url_tracker = url_tracker

    def extract(self) -> Iterator[tuple[str, list]]:
        rows = self.url_tracker.retrive(True)
        # limit the number of cities for testing
        for name, url in rows:
            print(name)
            flag_to_yield = True
            with requests.Session() as s:
                r = s.get(url, headers=self.headers)
                if r.status_code != 200:
                    self.logs_tracker.insert(name, url, 0)
                    continue
                else:
                    dom = etree.HTML(str(BeautifulSoup(r.content, features="lxml")))
                    node_script = dom.xpath("//script")[-2]
                    json_content = node_script.text
                    nodes_a = dom.xpath("//span[@class='ButtonLabel']/parent::a")
                    pages = [f"{self.redfin_homepage_url}{node.get('href')}" for node in nodes_a]
                    maphomecards = list()
                    for i, page_url in enumerate(pages):
                        r = s.get(page_url, headers=self.headers)
                        if r.status_code != 200:
                            self.logs_tracker.insert(name, url, 0)
                            flag_to_yield = False
                            break
                        else:
                            if i == len(pages) - 1:
                                self.logs_tracker.insert(name, url, 1)
                            dom = etree.HTML(str(BeautifulSoup(r.content, features="lxml")))
                            parent_nodes_div = dom.xpath("//div[contains(@id, 'MapHomeCard')]")
                            descendant_nodes_script = [node.xpath("./descendant::script")[0].text for node in parent_nodes_div]
                            maphomecards.extend(descendant_nodes_script)
                
                    if flag_to_yield:
                        yield json_content, maphomecards
                    else:
                        continue

    def transform(self):
        for json_content, maphomecards in self.extract():
            # maphomecards
            maphomecards: list[dict] = [eval(ele)[0] if isinstance(eval(ele), list) else eval(ele) for ele in maphomecards]
            maphomecards = [ele for ele in maphomecards if ele != None]
            keys = ['address', '@type']
            new_maphomecards = []
            for ele in maphomecards:
                new = {key:(value['streetAddress'] if isinstance(value, dict) else value) for (key, value) in ele.items() if key in keys}
                new_maphomecards.append(new)
            # maphomecards

            # json elements
            json_content = re.findall(r'\\"homes\\":.*,\\"dataSources\\"', json_content)[0]
            subtitutions = {r'\\': '', r',"dataSources"': '', r'"homes":': '', 
                            r'true': 'True', r'false': 'False'}
            for patt in list(subtitutions.keys()):
                json_content = re.compile(pattern=patt).sub(subtitutions[patt], json_content)
            
            split_pts = [r',"isViewedListing":False},', r',"dom.*']
            json_elements = re.split(split_pts[0], json_content[1:-1])
            json_elements = [re.split(split_pts[1], ele)[0] for ele in json_elements]

            json_elements: list[dict] = [eval(ele + '}') for ele in json_elements]

            features = ['price', 'hoa', 'sqFt', 'pricePerSqFt', 'lotSize', 'beds', 'baths', 
                        'streetLine', 'city', 'state', 'zip', 'postalCode', 'countryCode', 'yearBuilt']

            new_json_elements: list[dict] = []
            _func = lambda x: x if not isinstance(x, dict) else \
                x['value'] if 'value' in x else None
            for ele in json_elements:
                new: dict = {key: value for (key, value) in ele.items() if key in features}
                new.update(ele['latLong']['value'])
                new_json_elements.append({key: _func(value) for (key, value) in new.items()})
            new_json_elements = [ele for ele in new_json_elements if 'streetLine' in ele]
            # json elements

    def load(self):
        pass

# scrap homes data from API
class HomeAPIScrapper():
    def __init__(self,
                 tmp_path: str, table_name: str,
                 logs_tracker: LogsTracker, city_tracker: CityTracker,
                 url_tracker: URLTracker, redfin: RedfinHeadlessChromeBrowser) -> None:
        self.tmp_path = tmp_path
        self.table_name = table_name
        self.logs_tracker = logs_tracker
        self.city_tracker = city_tracker
        self.url_tracker = url_tracker
        self.redfin = redfin

    def _adjust_features_format(self, text: str):
        adjusted_text = re.sub(r'\s\(.*\)', '', text)
        adjusted_text = adjusted_text.strip().lower()\
            .replace('#', '').replace(' ', '_').replace('/', '_per_').replace('$', 'dollars')
        
        return adjusted_text

    def extract(self, 
                url_retriving_func: Callable[[bool | int | None], list[tuple]], 
                func_param: bool | int | None) -> Iterator[tuple[str, list]]:
        rows = url_retriving_func(func_param)
        self.redfin.start()
        for name, csv_download_link in rows:
            self.redfin.browser.get(csv_download_link); time.sleep(3)
            file_name = os.listdir(self.tmp_path)[0]
            file_path = f"{self.tmp_path}/{file_name}"
            with open(file_path, 'r+') as f:
                table = list(csv.reader(f, delimiter=','))
            os.remove(file_path)
            if len(table) <= 1:
                self.logs_tracker.insert(name, csv_download_link, 0)
                continue
            else:
                self.logs_tracker.insert(name, csv_download_link, 1)
                yield table

    def transform(self,
                  url_retriving_func: Callable[[bool | int | None], list[tuple]], 
                  func_param: bool | int | None) -> Iterator[tuple]:
        for table in self.extract(url_retriving_func, func_param):
            table.pop(1)
            features: list[str] = table.pop(0)
            features = tuple(list(map(self._adjust_features_format, features)))
            self.city_tracker.create_table(self.table_name, 'address', features)
            records = [tuple(i) for i in table]
            for record in records:
                yield features, record

    def load(self):
        for features, record in self.transform(self.url_tracker.retrive, False):
            self.city_tracker.insert(self.table_name, features, record)

    def reload(self):
        for features, record in self.transform(self.logs_tracker.retrieve, 0):
            self.city_tracker.insert(self.table_name, features, record)
        