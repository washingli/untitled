# 地图map
# coding=utf-8
import pandas as pd
import numpy as np
import requests
import json
from to_Hbase import To_Hbase

# response = requests.put('http://192.168.1.50:8324/all?table=S1_QianChengWuYou')
# print(response.text)
# datas = json.loads(response.text)
# # print(data)
# data1= pd.DataFrame(datas)
# # print(data1)
# data1.to_csv('H:\工作\工作-沪东重机\图表展示\前程无忧1.csv', encoding='gbk',index=False)



# import matplotlib.pyplot as plt
#encoding=utf-8


# plt.style.use('ggplot')
data1 = pd.read_csv('H:\工作\工作-沪东重机\图表展示\前程无忧1.csv', encoding='gbk')
# print(data1)
data=data1.dropna()   #用于去除一列中有空的行
# print(data)

# file.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\1.csv")

s26city = data[data['发布时间']=='11月26日']['城市'].value_counts().index  #按city列输出
s26jobnum = data[data['发布时间']=='11月26日']['城市'].value_counts().values  #按city列索引输出城市工作量
s25city = data[data['发布时间']=='11月25日']['城市'].value_counts().index
s25jobnum= data[data['发布时间']=='11月25日']['城市'].value_counts().values
data25 = pd.DataFrame({'city':s25city,'jobnum':s25jobnum,'date':25},columns=['city','jobnum'])  #建立city，jobnum两列的dataframe
data26 = pd.DataFrame({'city':s26city,'jobnum':s26jobnum},columns=['city','jobnum'])



print(data25)
print(data25.to_json(orient='records',force_ascii=False))  #输出相应格式的json格式
data2 = data25.to_json(orient='records',force_ascii=False)
data2 = json.loads(data2)
aim_dict = {}
aim_dict['Data'] = data2
aim_dict['链接'] = 'http://echarts.baidu.com/demo.html#map-china-dataRange'
print(aim_dict)
api = To_Hbase()
api.json_to_hbase(aim_dict,'map')