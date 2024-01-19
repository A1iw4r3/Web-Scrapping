import requests
from bs4 import BeautifulSoup
import pandas
j=0
name=[]
price=[]
discription=[]
review=[]
for i in range(2,11):
    url='https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    box=soup.find('div',class_='_1YokD2 _3Mn1Gg')
    # for names of devices

    nme=box.find_all('div',class_='_4rR01T')
    for i in nme:
        try:
            name.append(i.text)
        except:
            name.append('')

    # for prices of devices

    prc=box.find_all('div',class_='_30jeq3 _1_WHN1')
    for i in prc:
        try:
            price.append(i.text)
        except:
            price.append(' ')

    # for discription

    disc=box.find_all('ul',class_='_1xgFaf')
    for i in disc:
        try:
            discription.append(i.text)
        except:
            discription.append('')

    # for reviews
    
    rev=box.find_all('span',class_='_2_R_DZ')

    for i in rev:
        try:
            review.append(i.text)
        except:
            review.append('')
    

print(len(name))
print(len(price))
print(len(discription))
print(len(review))
# df=pandas.DataFrame({'Products':name, 'Prices':price, 'Discription':discription,'Reviews':review})
# print(df)
# df.to_csv('Mobile under 50000.csv')