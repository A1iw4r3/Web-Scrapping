import requests
from bs4 import BeautifulSoup
import pandas
url='https://www.psx.com.pk/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
table=soup.find('table',class_='table')
head=table.find_all('th')
heading=[]
for i in head:
    heading.append(i.text)
df=pandas.DataFrame(columns=heading)
rows=table.find_all('tr',class_='first-tr')
for i in rows[1:]:
    data=i.find_all('td')
    row_data=[rd.text for rd in data]
    l=len(df)
    df.loc[l]=row_data
print(df)