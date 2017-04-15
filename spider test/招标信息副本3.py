# coding=utf-8

import urllib
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import pandas
import pymysql

data_csv = pandas.DataFrame(columns=['名称', '地点', '类型', '时间'])
n = 0

for p in range(140000, 150000):
    print(p)

    p = str(p)

    urlsw = 'http://p.tgnet.com/PersonalService/Bidding/Search.aspx?p=' + p

    # data = pandas.read_table(urlsw,encoding='gbk',sep=None)


    # data = pandas.read_table(urlsw)
    try:
        url = urlopen(urlsw)

        # print(url.read().decode('gbk'))

        # tablesw = url.read().decode('gbk')
        soup = bs(url.read().decode('gbk'), 'html.parser')
    except:
        continue

    for trsw in soup.table.find_all('tr'):
        if len(trsw.find_all('td')) == 4:
            mid = trsw.find_all('td')

            mc = mid[0].text.replace(' ', '')
            mc = re.sub('(\n)|(\r)|(：)', '', mc)
            # print(mc)

            dd = mid[1].text.replace(' ', '')
            lx = mid[2].text.replace(' ', '')
            sj = mid[3].text.replace(' ', '')
            # print(mc, dd, lx, sj)

            # 导入msql
            conn = pymysql.connect(host='192.168.1.50', port=3306, user='MC', passwd='ldx915959688', db='origin',
                                   charset='utf8')
            try:
                with conn.cursor() as cur:
                    sql = "insert into 天工网招标信息 (工程项目,地点,类型,时间) values(%s,%s,%s,%s)"

                    cur.execute(sql, (mc, dd, lx, sj))

                    conn.commit()


            finally:
                conn.close()


            # 导入csv
#             data_csv.loc[n, '名称'] = mc
#             data_csv.loc[n, '地点'] = dd
#             data_csv.loc[n, '类型'] = lx
#             data_csv.loc[n, '时间'] = sj
#             n = n + 1
#
# print(n)
# data_csv.to_csv("C:\\Users\\hc\\Desktop\\天工网\\TianGongWang_ZhaoBiao.csv", index=None)
