import requests
from bs4 import BeautifulSoup
i=1
url='https://www.daraz.pk/catalog/?spm=a2a0e.home.search.1.5bc64076lw3mAm&q=mobiles%20phones&_keyori=ss&from=search_history&sugg=mobiles%20phones_0_1'
req=requests.get(url)
soup=BeautifulSoup(req.text,'lxml')
box=soup.find_all('div',class_='box--pRqdD boxWithSku--Abyff')
print(box)