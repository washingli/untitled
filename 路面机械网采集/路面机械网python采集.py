# coding=utf-8
import urllib
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import pandas
import pymysql
data_csv = pandas.DataFrame(columns=['工程项目', '项目简介', '发布日期'])
x=0
y=0
z=0
for p in range(1,41):
    print(p)

    p = str(p)
    if(p == '1'):
        url = 'http://news.lmjx.net/List_201.shtml'
    else:
        url = 'http://news.lmjx.net/List_201_'+p+'.shtml'
    try:
        html = urlopen(url)
        soup = bs(html.read())
    except:
        continue
#title
    title = soup.find_all('h1')
    i=0
    for n in title:
        i=i+1
    print(i)
    for m in range(i):
        titletext = title[m].text.replace(' ', '')
        titletext = title[m].text.replace('&mdash;', '')
        titletext = title[m].text.replace('&rdquo;', '')
        titletext = title[m].text.replace('&ldquo;', '')
        titletext = title[m].text.replace('&middot;', '')
        titletext = re.sub('(\n)|(\r)|(\t)', '', titletext)
        print(titletext)
        data_csv.loc[x, '工程项目'] = titletext    #导入csv
        x=x+1
#description
    j=0
    desc=soup.find_all('p','description'or'description hhdescription')
    for n in desc:
        j=j+1
    print(j)
    for m in range(j):
        describ=desc[m].text.replace(' ','')
        describ = desc[m].text.replace('&mdash;', '')
        describ = desc[m].text.replace('&rdquo;', '')
        describ = desc[m].text.replace('&ldquo;', '')
        describ = desc[m].text.replace('&middot;', '')
        describ= re.sub('(\n)|(\r)|(\t)', '', describ)
        print(describ)
        data_csv.loc[y, '项目简介'] = describ    #导入csv
        y=y+1
#time
    k=0
    time=soup.find_all('label','nmore')
    for m in time:
        k=k+1
    print(k)
    for m in range(k):
        date = time[m].text.replace(' ', '')
        date = re.sub('(\n)|(\r)|(\t)|(:)|([^ -~])', '', date)
        geshi = '(\d{4}-\d{2}-\d{2})'
        datetime=re.match('(\d{4}-\d{2}-\d{2})',date ).group()
        print(datetime)
        data_csv.loc[z, '发布日期'] = datetime   #导入csv
        z = z + 1
print(data_csv)
# # 导入数据库
for i in data_csv.index:
    a = data_csv.loc[i, '工程项目']
    b = data_csv.loc[i, '项目简介']
    c = data_csv.loc[i, '发布日期']
#     # print(a, b, c)
#
    conn = pymysql.connect(host='192.168.1.50', user='washingli', password='qwert', db='origin', charset='utf8')
    try:
        cursor = conn.cursor()
         # 插入数据
        cursor.execute("insert into 路面机械展会动态(工程项目,项目简介,发布日期) values(%s,%s,%s)", (a, b, c))
#         # 更新数据
#         # cursor.execute("update 路面机械招标信息 set 发布日期='2'")
#         # 查找数据
#         # cursor.execute("select 工程项目,项目详情,发布日期,pageUrl from 路面机械招标信息")
#         # 输出数据
#         # for a,b,c,d in cursor:
#         #     print(a,b,c,d)
#         # 删除数据
#         # cursor.execute("delet all from student")
        conn.commit()
    finally:
        conn.close()






















