import requests
from bs4 import BeautifulSoup
import pandas
url='https://ticker.finology.in/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
table=soup.find('table',class_='table table-sm table-hover screenertable')
head=table.find_all('th')
heading=[]
for i in head:
    heading.append(i.text)
df=pandas.DataFrame(columns=heading)
rows=table.find_all('tr')[1:]
for i in rows:
    n=i.find_all('td')[0].find('a',class_='complink').text.strip()
    data=i.find_all('td')[1:]
    row_data=[rd.text for rd in data]
    row_data.insert(0,n)
    l=len(df)
    df.loc[l]=row_data
df.to_csv('table.csv')