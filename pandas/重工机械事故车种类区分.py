# coding=utf-8

import pandas as pd
import re

brics = pd.read_csv("D:\\a.csv")


for w in brics.index:
    if re.search('挖掘机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '挖掘机'
    elif re.search('装载机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '装载机'
    elif re.search('搅拌车', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '搅拌车'
    elif re.search('吊车', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '吊车'
    elif re.search('铣刨机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '铣刨机'
    elif re.search('铲车', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '铲车'
    elif re.search('牵引车', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '牵引车'
    elif re.search('压路机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '压路机'
    elif re.search('提升机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '提升机'
    elif re.search('起重机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '起重机'
    elif re.search('工程车', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '工程车'
    elif re.search('混凝土泵车', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '混凝土泵车'
    elif re.search('推土机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '推土机'
    elif re.search('平地机', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '平地机'
    elif re.search('塔吊', brics.loc[w, '标题']):
        brics.loc[w, '标签'] = '塔吊'
    else:
        brics.loc[w, '标签'] = '无'



brics.to_csv("D:\\b.csv")
