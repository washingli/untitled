# coding=utf-8
# coding=utf-8
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pymongo
import pandas as pd
import re



data_csv=pd.DataFrame(columns=['开工信息的地理位置','经纬度','标题','文章链接','城市'])
x=0
y=0
z=0
j=0
k=0



for p in range(1,3):
    print(p)
    p=str(p)
    url='http://gc.buildnet.cn/Home/Index/'+p
    print(url)
    html=urlopen(url)
    soup=bs(html, "html.parser")
#     title
    title=soup.find_all('h3')
    for m in title:
        a=m.text.replace(' ','')
        print(a)
        data_csv.loc[x,'标题']=a  #导入csv
        x=x+1
#     link
    for m in title:
        link=m.find('a',target="_blank")
        linkend='http://gc.buildnet.cn/'+link.get('href')
        print(linkend)
        data_csv.loc[y, '文章链接'] = linkend  # 导入csv
        y=y+1
#     address
        url1=linkend
        html1=urlopen(url1)
        soup1=bs(html1,"html.parser")
        address=soup1.find_all('p')
        addressend1 = address[2].text.replace('地址：', '')
        addressend=re.sub('\s+','',addressend1)
        print(addressend)
        data_csv.loc[z, '开工信息的地理位置'] = addressend  # 导入csv
        z=z+1
#
#      city
    i=0
    city=soup.find_all('tr')
    # print(city)
    for m in city:
        city1=m.find('td',class_="f-tal")
        if city1:
            cityend=city1.text
            print(cityend)
        else:
            continue
        data_csv.loc[j, '城市'] = cityend  # 导入csv
        j=j+1


print(data_csv)
data_dict=data_csv.to_dict(orient='record')
client=pymongo.MongoClient("192.168.1.50", 27017)
db=client.mydb
collectiion=db.projectIM1
collectiion.insert_many(data_dict)
print(collectiion.find_one())