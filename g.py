import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
gt=requests.get(url)
soup= BeautifulSoup(gt.text,'lxml')
price=soup.find('h4',{'class':'pull-right price'})
des=soup.find('p',{'class':'description'})
d=soup.find('p',class_="description")
print(d.string)
print(des.string)
print(price)
print(price.string)
print(soup.h4.string)