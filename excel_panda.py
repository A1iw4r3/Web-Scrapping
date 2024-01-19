import requests
from bs4 import BeautifulSoup
import pandas

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
#name
names=soup.find_all('a',class_ = 'title')
product_list=[]
for i in names:
    name=i.text
    product_list.append(name)
#print(product_list)
#price
prices=soup.find_all('h4',class_ = 'pull-right price')
price_list=[]
for i in prices:
    price=i.text
    price_list.append(price)
print(price_list)
#discreption
dis=soup.find_all('p',class_='description')
dis_list=[]
for i in dis:
    diss=i.text
    dis_list.append(diss)
#print(dis_list)
#reviews
review= soup.find_all('p',class_='pull-right')
review_list=[]
for i in review:
    reviews=i.text
    review_list.append(reviews)
#print(review_list)

#pandas library
df=pandas.DataFrame({'Product list':product_list,'prices':price_list,'Review':review_list,'Discreption':dis_list})
print(df)
df.to_csv('product details.csv')