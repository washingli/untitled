# coding=utf-8

import pandas as pd
import re

brics = pd.read_csv("D:\\a.csv")
for w in brics.index:
	if re.search('钢', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '钢'
	elif re.search('金属', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '金属'
	elif re.search('橡胶', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '橡胶'
	elif re.search('合金', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '合金'
	elif re.search('玻璃', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '玻璃'
	elif re.search('化肥', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '化肥'
	elif re.search('煤炭', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '煤炭'
	elif re.search('成品油', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '成品油'
	elif re.search('农产品', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '农产品'
	elif re.search('铝', brics.loc[w, '标题']):
		brics.loc[w, '标签'] = '铝'
	else:
		brics.loc[w, '标签'] = '其他'


brics.to_csv("D:\\b.csv")
