#encoding='utf-8'
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import urllib
import pandas as pd
import requests
from http.cookiejar import CookieJar
from requests.exceptions import HTTPError
import re
data_csv=pd.DataFrame(columns=['brand'])
x=0
url='http://mobile.zol.com.cn/manu_list.html'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
try:
    req=urllib.request.Request(url,None,headers=header)
    cj=CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    response=opener.open(req)
    raw_response=response.read().decode('gbk',errors='ignore')
    # print(raw_response)
except urllib.request.HTTPError as inst:
    output=format(inst)
    print(output)
soup=bs(raw_response)
# print(soup)
brands=soup.find_all('ul',class_="brandsTxt clearfix")
for m in brands:
    brand1=m.find_all('li')
    for n in brand1:
        brand=n.text
        brand=re.sub('\\n','',brand)
        brand=re.sub('\\t','',brand)
        brand=re.sub('\s+','',brand)
        print(brand)
        data_csv.loc[x,'brand']=brand
        x=x+1
print(data_csv)
data_csv.to_csv("H:\\毕业设计\\phonebrands.csv")