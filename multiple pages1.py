import requests
from bs4 import BeautifulSoup
for i in range(2,11):
    url='https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page='+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    np=soup.find('a',class_='_1LKTO3').get('href')
    c_url='https://www.flipkart.com/'+np
    print(c_url)