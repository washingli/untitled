#coding=utf-8
#python version：2.7
#author:sharpdeep

import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS
import pandas as pd

data_csv=pd.DataFrame(columns=['title','link','time','desc'])
x=0
y=0
z=0
k=0
baseUrl = 'http://www.baidu.com/s'
for page in range(1,5):


    # page = 1 #第几页
    word = '钢铁价格'  #搜索关键词 不限格式
    word1='filetype:xls '+'钢铁价格' #搜索关键词 按execl
    word2='filetype:pdf '+'钢铁价格' #搜索关键词 按pdf
    word3='filetype:ppt'+'钢铁价格' #搜索关键词 按ppt
    word4='filetype:doc '+'钢铁价格' #搜索关键词 按doc
    word5='filetype:rtf'+'钢铁价格' #搜索关键词 按rtc


    data = {'wd':word1,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1','bs':'filetype:xls 机械'}
    data = urllib.urlencode(data)
    url = baseUrl+'?'+data
    print url

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    except urllib2.HttpError,e:
        print e.code
        exit(0)
    except urllib2.URLError,e:
        print e.reason
        exit(0)

    html = response.read()
    soup = BS(html)
    td = soup.find_all(class_='f')

    for t in td:
        a= t.h3.a.get_text()
        data_csv.loc[x,'title']=a
        x=x+1
        b= t.h3.a['href']
        data_csv.loc[y, 'link'] = b
        y=y+1
        font_str = t.find_all('font',attrs={'size':'-1'})[0].get_text()
        start = 0 #起始
        realtime = t.find_all('div',attrs={'class':'realtime'})
        if realtime:
            realtime_str = realtime[0].get_text()
            start = len(realtime_str)
            c= realtime_str
            data_csv.loc[z, 'time'] = c
            z=z+1
        end = font_str.find('...')
        d= font_str[start:end+3]
        data_csv.loc[k, 'desc'] = d
        k=k+1
# print data_csv
for n in data_csv.index:
    data_csv.loc[n,'daynum']=re.sub('',data_csv.loc[n,'time'])
print data_csv.sort_index(by='daynum')

