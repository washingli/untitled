#funnel plot饼图
# coding=utf-8
import pandas as pd
import numpy as np
import requests
import json
from to_Hbase import To_Hbase
#读hbase的文件
response = requests.put('http://192.168.1.50:32143/all?table=E3_DingDanDongTai')
# print(response.text)
data = json.loads(response.text)
# print(data)
file= pd.DataFrame(data)
# print(read_csvsw)



file=pd.read_csv("H:\工作\工作-沪东重机\图表展示\E3订单动态.csv",encoding='gbk')

i=0
x=0
y=0
z=0
for n in file.index:

    # if file.loc[n,'发布
    date=file.loc[n,'发布日期']
    a=date.split('/')   #将发布日期分为4各部分
    if a[0]=='2016':    #找到2016年的日期，并统计个数
        i=i+1
    elif a[0]=='2015':
        x=x+1
    elif a[0]=='2014':
        y=y+1
    elif a[0]=='2013':
        z=z+1
    else:
        continue
# print(i,x,y,z)
# pd.to_csv("H:\工作\工作-沪东重机\图表展示\pie.csv",encoding='utf-8')
# file2=pd.DataFrame.to_csv("H:\工作\工作-沪东重机\图表展示\pie.csv",encoding='utf-8')
# for m in file2.index:
# file2.loc[0,'year']='2016'
# file2.loc[1,'year']='2015'
# file2.loc[2,'year']='2014'
# file2.loc[3,'year']='2013'
# file2.loc[0,'num']=i
# file2.loc[1,'num']=x
# file2.loc[2,'num']=y
# file2.loc[3,'num']=z
print(i,x,y,z)   #输出各个年份的个数
l = [i,x,y,z]
data = pd.DataFrame({'year':[2016,2015,2014,2013],'num':l},columns=['year','num'])
# print(data)

# data.to_csv("H:\工作\工作-沪东重机\图表展示\pie.csv",encoding='utf-8')
# pd.DataFrame({'year':2016,'num':i},{'year':2015,'num':x},{'year':2014,'num':y},{'year':2013,'num':z})
# pd.DataFrame.to_csv("H:\工作\工作-沪东重机\图表展示\pie.csv",encoding='utf-8')
print(data.reset_index())
datasw = data.reset_index()   #重新指定索引
del datasw['index']
print(datasw.to_json(orient='records'))  #按相应json格式输出
#
data2 = datasw.to_json(orient='records')
data2 = json.loads(data2)
aim_dict = {}
aim_dict['Data'] = data2
aim_dict['链接'] = 'http://echarts.baidu.com/demo.html#pie-simple'
print(aim_dict)
api = To_Hbase()
api.json_to_hbase(aim_dict,'funnelplot')