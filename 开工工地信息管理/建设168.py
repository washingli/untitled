# coding=utf-8

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import re
import pymongo
data_csv = pd.DataFrame(columns=['开工信息的地理位置', '经纬度', '标题','文章链接','城市'])
x=0
y=0
z=0
k=0
for p in range(960,963):
    print(p)
    p=str(p)
    if (p=='1'):
        url='http://jsgc168.com/gcxx/list-513.html'
    else:
        url='http://jsgc168.com/gcxx/list-513-'+p+'.html'
    try:
        html=urlopen(url)
        soup=bs(html.read())
    except:
        continue
# title
    i=0
    title=soup.find_all('li',class_="su021")
    print(title)
    for n in title:
        # print(n.text)
        i=i+1
        # print(i)
    for m in range(20):
        titlefirst=title[m].text.replace('[新增]','')
        titleend=re.sub(' ', '', titlefirst)
        print(titleend)
        data_csv.loc[x, '标题'] = titleend  # 导入csv
        x = x + 1

# 地址
    address=soup.find_all('li',class_="f_gray su022")
    # print(address)
    j=0
    for n in address:
        # print(n.text)
        j=j+1
        # print(j)
    for m in range(20):
        addressend=address[m].text.replace('工程地址：','')
        print(addressend)
        data_csv.loc[y, '开工信息的地理位置'] =addressend   # 导入csv
        y = y + 1
# title link
    link=soup.find_all('a',class_="yzgc")
    for m in link:
        linkend=m.get('href')
        # print(linkend)
        data_csv.loc[z,'文章链接'] = linkend  # 导入csv
        z = z + 1
#city
        url1=linkend
        html1=urlopen(url1)
        soup=bs(html1.read())
        city=soup.find_all('span',class_="su0092")
        if city:

            print(city[2].text)
            data_csv.loc[k,'城市']=city[2].text  #导入csv
        else:
            data_csv.loc[k, '城市'] = None  # 导入csv
        k=k+1

print(data_csv)

data_dict=data_csv.to_dict(orient='record')
print(data_dict)
client=pymongo.MongoClient('192.168.1.50',27017)
db=client.mydb
collection=db.projectIM
collection.insert_many(data_dict)
print(collection.find_one())






























