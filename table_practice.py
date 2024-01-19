import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://ticker.finology.in/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
table=soup.find('table',class_='table table-sm table-hover screenertable')
row=table.find_all('th')
header=[]
for i in row:
    header.append(i.text)
df=pd.DataFrame(columns=header)
rows=table.find_all('tr')
for i in rows[1:]:
    n=i.find_all('td')[0].find('a',class_='complink').text.strip()
    data=i.find_all('td')[1:]
    rows_data=[rd.text for rd in data]
    rows_data.insert(0,n)
    l=len(df)
    df.loc[l]=rows_data
print(df)