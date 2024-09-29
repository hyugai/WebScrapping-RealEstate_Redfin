import requests
from bs4 import BeautifulSoup
from lxml import etree
import re, json, sqlite3

with requests.Session() as s:
    # get respone of the GET request
    user_agent = r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    headers = {'User-Agent': user_agent}
    test_url = 'https://www.redfin.com/city/30818/TX/Austin'
    r = s.get(test_url, headers=headers)

    # soup
    soup = BeautifulSoup(r.content, features='lxml')

    # DOM object
    dom = etree.HTML(str(soup))

tag_content = re.sub(r'\\', '', dom.xpath("//script")[-2].text)
# text = re.findall(r"\"homes\":[^'']*,\"dataSources\"", tag_content)
text = re.findall(r"\"homes\":.*,\"dataSources\"", tag_content)
x1 = re.sub(r",\"dataSources\"",'', text[0])[8:]
x2 = re.sub(r"false", "False", x1)
x3 = re.sub(r"true", "True", x2)
#a = re.findall(r"\bmlsId\b.*(?!\bmlsId\b)\bisViewedListing\b(?!\bisViewedListing\b)", x3)
b = re.split(r",\"isViewedListing\":False},", x3[1:-1])

print(b[-3]+'}')
# print(type(eval(b[0]+'}')))