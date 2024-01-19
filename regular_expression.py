import requests
from bs4 import BeautifulSoup
import re

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
#finding all about tags
soup.find_all(['h4','p'])
# finding about exect string
exect=soup.find_all(string='Galaxy Tab 3')
print(exect)
# finding all related
related= soup.find_all(string=re.compile('Galaxy'))
print(related)