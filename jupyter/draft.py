import requests
from bs4 import BeautifulSoup
from lxml import etree
import re, json, sqlite3

# with requests.Session() as s:
#     # get respone of the GET request
#     user_agent = r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
#     headers = {'User-Agent': user_agent}
#     test_url = 'https://www.redfin.com/city/30818/TX/Austin'
#     r = s.get(test_url, headers=headers)

#     # soup
#     soup = BeautifulSoup(r.content, features='lxml')

#     # DOM object
#     dom = etree.HTML(str(soup))

# tag_content = re.sub(r'\\', '', dom.xpath("//script")[-2].text)
# # text = re.findall(r"\"homes\":[^'']*,\"dataSources\"", tag_content)
# text = re.findall(r"\"homes\":.*,\"dataSources\"", tag_content)
# x1 = re.sub(r",\"dataSources\"",'', text[0])[8:]
# x2 = re.sub(r"false", "False", x1)
# x3 = re.sub(r"true", "True", x2)
# #a = re.findall(r"\bmlsId\b.*(?!\bmlsId\b)\bisViewedListing\b(?!\bisViewedListing\b)", x3)
# b = re.split(r",\"isViewedListing\":False},", x3[1:-1])
# c = [i + '}' for i in b]

# for i, val in enumerate(c):
#     try:
#         t = eval(val)
#     except:
#         print(val)
#         continue

# print(eval(c[109]))
# eval(c[109])
# test_patt = r':"\w+'
# print(re.findall(test_patt, c[109]))

text = '{"mlsId":{"label":"MLS#","value":"4672288"},"showMlsId":False,"mlsStatus":"Active","showDatasourceLogo":False,"price":{"value":1175000,"level":1},"hideSalePrice":False,"hoa":{"level":1},"isHoaFrequencyKnown":True,"sqFt":{"value":1400,"level":1},"pricePerSqFt":{"value":839,"level":1},"lotSize":{"value":6969,"level":1},"beds":3,"baths":2.0,"fullBaths":2,"location":{"value":"Tarry Town 07","level":1},"stories":1.0,"latLong":{"value":{"latitude":30.2935182,"longitude":-97.7601638},"level":1},"streetLine":{"value":"2413 Winsted Ln","level":1},"unitNumber":{"level":1},"city":"Austin","state":"TX","zip":"78703","postalCode":{"value":"78703","level":1},"countryCode":"US","showAddressOnMap":True,"soldDate":1619766000000,"searchStatus":1,"propertyType":6,"uiPropertyType":1,"listingType":1,"propertyId":31232728,"listingId":193594487,"dataSourceId":92,"marketId":12,"yearBuilt":{"value":1955,"level":1},"dom":{"value":3,"level":1},"timeOnRedfin":{"value":205347765,"level":1},"originalTimeOnRedfin":{"value":205347797,"level":1},"timeZone":"USu002FCentral","primaryPhotoDisplayLevel":1,"photos":{"value":"0-30:0","level":1},"additionalPhotosInfo":[],"openHouseStart":1727632800000,"openHouseEnd":1727640000000,"openHouseStartFormatted":"Sep 29, 1:00PM","openHouseEventName":"Open House - 1:00 - 3:00 PM","url":"u002FTXu002FAustinu002F2413-Winsted-Ln-78703u002Fhomeu002F31232728","insight":{"value":{"note":"Large lot with a great "shed" in the backyard.  1 car garage, Completely updated.  ","agentName":"Eric Hegwer","agentType":1,"agentId":12592,"created":1596455027000},"level":1},"hasInsight":True,"sashes":[{"sashType":10,"sashTypeId":10,"sashTypeName":"Open House","sashTypeColor":"#73BB3C","isRedfin":False,"isActiveKeyListing":False,"openHouseText":"OPEN TODAY, 1PM TO 3PM","lastSaleDate":"","lastSalePrice":""}],"keyFacts":[{"description":"6,969 sq ft lot","rank":0},{"description":"Garage","rank":1},{"description":"Somewhat walkable","rank":2}],"isHot":False,"hasVirtualTour":False,"hasVideoTour":False,"has3DTour":False,"newConstructionCommunityInfo":{},"isRedfin":False,"isActiveKeyListing":False,"isNewConstruction":False,"listingRemarks":"An absolutely stunning single-story home in Tarrytown that has been updated offers the perfect blend of charm and modern upgrades. This incredible home features a light-filled, open floor plan and has been completely updated with beautiful white oak floors, a gourmet kitchen with state-of-the-art appliances, and exquisite marble bathrooms with designer fixtures. It also boasts custom closets and iron doors that lead to a spacious backyard, complete with a fabulous covered patio featuring an outdoor fireplace and a summer kitchen with a kegerator. Additionally, there is a detached back house, perfect for an office. This beautifully refined home is ideally located within walking distance to T","remarksAccessLevel":1,"businessMarketId":13,"isShortlisted":False}'
pattern = r':"[\w\s]+"[\w\s]+"[^"]+"'
print(re.findall(pattern, text))