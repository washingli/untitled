#heatmap图


# coding=utf-8
import pandas as pd
import numpy as np
import requests
import json
from to_Hbase import To_Hbase
# response = requests.put('http://192.168.1.50:32143/all?table=S1_QianChengWuYou')
# print(response.text)
# datas = json.loads(response.text)
# # print(data)
# data1 = pd.DataFrame(datas)
# print(data1)




# data1.to_csv('H:\工作\工作-沪东重机\图表展示\前程无忧1.csv', encoding='gbk',index=False)
# import matplotlib.pyplot as plt
#encoding=utf-8


# plt.style.use('ggplot')
data1 = pd.read_csv("H:\工作\工作-沪东重机\图表展示\前程无忧1.csv", encoding='gbk',low_memory=False)
data=data1.dropna()   #用于去除一列中有空的行

# file.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\1.csv")
# gdata1low=data['薪资下限'].groupby([data['城市'],data['发布时间']=='11月26日'])
# gdata1high=data['薪资上限'].groupby([data['城市'],data['发布时间']=='11月26日'])
gdata2low=data['薪资下限'].groupby([data['城市'],data['发布时间']=='11月25日'])  #按城市来分组输出相应的薪资下限，并且发布时间为11月25日
gdata2high=data['薪资上限'].groupby([data['城市'],data['发布时间']=='11月25日'])

file2low=gdata2low.mean()  #求上面分组后的平均值，每个城市的薪资平均值
file2high=gdata2high.mean()
# file1low=gdata1low.mean()
# file1high=gdata1high.mean()

# file1low.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\25low.csv.csv")
# file1high.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\25high.csv.csv")
file2low.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\26low.csv.csv")
file2high.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\26high.csv.csv")
# s25=pd.DataFrame({'city':a,'salary':b},columns=['city','salary''salary25'])



s26city = data[data['发布时间']=='11月26日']['城市'].value_counts().index  #输出各列的值（发布时间为11月26日的城市列表）
s26jobnum = data[data['发布时间']=='11月26日']['城市'].value_counts().values
# s25city = data[data['发布时间']=='11月25日']['城市'].value_counts().index
# s25jobnum= data[data['发布时间']=='11月25日']['城市'].value_counts().values
# data25 = pd.DataFrame({'city':s25city,'jobnum':s25jobnum,'date':25},columns=['city','jobnum'])
data26 = pd.DataFrame({'city':s26city,'jobnum':s26jobnum},columns=['city','jobnum'])   #建立新的dataframe 包括city、jobnum
# data25['date']=25
data26['date']=26
# print(data25)
# print(data26)


# gdata2=data['薪资下限'].groupby(data['城市'])
# print(data25)


# s25.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\25.csv")
# s26.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\26.csv")




#
# gtPRC_city = pd.DataFrame({'城市': data['城市'].value_counts().index, '次数': data['城市'].value_counts().values})


#
# print(gdata1.mean(),gdata2.mean(),gtPRC_city)

# print(data.mean(axis=0,skipna=False))
# print(gtPRC_city)

# brics25low = pd.read_csv("H:\\工作\\工作-沪东重机\\图表展示\\25low.csv.csv",encoding='gbk')
# brics25high = pd.read_csv("H:\\工作\\工作-沪东重机\\图表展示\\25high.csv.csv",encoding='gbk')
brics26low = pd.read_csv("H:\\工作\\工作-沪东重机\\图表展示\\26low.csv.csv",encoding='gbk')
brics26high= pd.read_csv("H:\\工作\\工作-沪东重机\\图表展示\\26high.csv.csv",encoding='gbk')
# brics25low = brics25low[brics25low['False']==True]
# del brics25low['False']
#
# brics2525low= pd.DataFrame(brics25low.values,columns=['city','salary_low'])
# # print(brics2525low)
#
# brics25high = brics25high[brics25high['False']==True]
# del brics25high['False']
#
# brics2525high= pd.DataFrame(brics25high.values,columns=['city','salary_high'])
# # print(brics2525high)

brics26low = brics26low[brics26low['False']==True]  #取出上面分组中时间是11月26日的那一行
del brics26low['False']  #删除标题为False的那一列

brics2626low= pd.DataFrame(brics26low.values,columns=['city','salary_low'])  #建立city salary_low两列
print(brics2626low)

brics26high= brics26high[brics26high['False']==True]
del brics26high['False']

brics2626high= pd.DataFrame(brics26high.values,columns=['city','salary_high'])
print(brics2626high)


# a=pd.merge(data25,brics2525low,on='city')
# aa=pd.merge(a,brics2525high,on='city')
# print(aa)

b=pd.merge(data26,brics2626low,on='city')  #将city salary_high  与city jobnum 按城市连接起来
bb=pd.merge(b,brics2626high,on='city')

del bb['date']  #删除date列
del bb['jobnum']  #删除jobnum列

dictsw = {}

# print(bb)
data3 = {}
for idx in bb.index:
    data3[bb.loc[idx,'city']] = bb.loc[idx].tolist()[1:3]
# print('data3=',data3)

# listsw = []
#
# cc = aa.append(bb)
# cc = pd.DataFrame(cc.values,columns=cc.columns,index=range(0,len(cc.index)))
# print(cc)
# cc=cc.reindex(columns=['salary_low','jobnum','salary_high','city','date'])
# aa=aa.reindex(columns=['salary_low','jobnum','salary_high','city','date'])
# bb=bb.reindex(columns=['salary_low','jobnum','salary_high','city','date'])
# cc.to_csv("H:\\工作\\工作-沪东重机\\图表展示\\scatter",encoding='utf-8')
# listsw.append(aa.values.tolist())
# listsw.append(bb.values.tolist())
# print(cc)
# print(bb.to_json(orient='records',force_ascii=False))

# print(listsw)



# print(bb.values.tolist())

for idx in bb.index:   #输出{name：[]，。。}格式
    dictsw[bb.loc[idx,'city']] = list(bb[['salary_low','salary_high']].applymap(lambda x:int(x)).loc[idx].values)
    # print( list(bb[['salary_low','salary_high']].loc[idx].values))
# dictsw['biaoti']='name'
# print(dictsw)
def f(x):
    try:
        return int(x)
    except:
        return x   #取整数
brics2626low = brics2626low.applymap(f)  #取整数
# print(brics2626low.to_json(orient='records',force_ascii=False))   #输出相应的json格式
data2 = brics2626low.to_json(orient='records',force_ascii=False)
data2 = json.loads(data2)
aim_json1 = {}
aim_json2 = {}
aim_json1['Data1'] = data3
aim_json2['Data2'] = data2
aim_json1['链接'] = 'http://echarts.baidu.com/demo.html#heatmap-map'
aim_json2['链接'] = 'http://echarts.baidu.com/demo.html#heatmap-map'
print(aim_json1)
print(aim_json2)

api = To_Hbase()
api.json_to_hbase(aim_json2,'Heatmap2')