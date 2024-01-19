import requests
from bs4 import BeautifulSoup

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')

box=soup.find_all('div',class_='col-sm-4 col-lg-4 col-md-4')
#name
box_no=(int(input("Enter the number of box: "))-1)
b=box[box_no]
name=b.find('a')
print(name.string)
# discription
box_no=((int(input("Enter the number of box: ")))-1)
b=box[box_no]
discription=b.find('p')
print(discription.string)
#price
box_no=(int(input("Enter the number of box: "))-1)
p=box[box_no]
price=p.find('h4')
print(price.string)
#review
box_no=(int(input("Enter the number of box: "))-1)
r=box[box_no]
review=r.find("p",class_='pull-right').text
print(review)