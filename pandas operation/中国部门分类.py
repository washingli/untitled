# coding=utf-8

import pandas as pd
import re

brics = pd.read_csv("D:\\a.csv")
for w in brics.index:
    if re.search('统计局', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '统计局'
    elif re.search('教育部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '教育部'
    elif re.search('农业部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '农业部'
    elif re.search('信访局', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '信访局'
    elif re.search('发改委', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '发改委'
    elif re.search('计生委', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '计生委'
    elif re.search('水利部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '水利部'
    elif re.search('商务部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '商务部'
    elif re.search('外汇局', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '外汇局'
    elif re.search('财政部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '财政部'
    elif re.search('文化部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '文化部'
    elif re.search('旅游局', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '旅游局'
    elif re.search('民航局', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '民航局'
    elif re.search('中央司改办', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '中央司改办'
    elif re.search('交通运输部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '交通运输部'
    elif re.search('社会保障部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '社会保障部'
    elif re.search('人社部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '人社部'
    elif re.search('国税局', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '国税局'
    elif re.search('工商总局', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '工商总局'
    elif re.search('公安部', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '公安部'
    elif re.search('审计署', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '审计署'
    elif re.search('证监会', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '证监会'
    else:
        brics.loc[w, '标签'] = '其他'

brics.to_csv("D:\\b.csv")
print brics
