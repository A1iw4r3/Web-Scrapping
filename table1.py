import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://ticker.finology.in/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
table=soup.find('table',class_='table table-sm table-hover screenertable')
index=table.find_all('th')
index_list=[]
for i in index:
    index_t=i.text
    index_list.append(index_t)
print(index_list)
pd=pd.DataFrame(columns='index_list')
print(pd)