import requests 
from bs4 import BeautifulSoup

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
price=soup.find_all('h4',class_="pull-right price")
for i in price:
    print(i.string)
dscrptn=soup.find_all('p',class_='description')
for i in dscrptn:
    print(i.string)
