import requests
from bs4 import BeautifulSoup
url='https://webscraper.io/test-sites/e-commerce/allinone'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')

menu=soup.find_all('ul',class_='nav',id='side-menu')[0]
bar=menu.find_all('li',class_='active').text
print(bar)