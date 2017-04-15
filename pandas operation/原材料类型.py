# coding=utf-8

import pandas as pd
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
brics = pd.read_csv(u"C:\\Users\\92452\\Desktop\\a.csv", encoding='gbk')

for w in brics.index:
	if re.search(u'钢', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'钢'
	elif re.search(u'金属', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'金属'
	elif re.search(u'橡胶', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'橡胶'
	elif re.search(u'合金', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'合金'
	elif re.search(u'玻璃', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'玻璃'
	elif re.search(u'化肥', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'化肥'
	elif re.search(u'煤', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'煤'
	elif re.search(u'成品油', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'成品油'
	elif re.search(u'农产品', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'农产品'
	elif re.search(u'铝', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'铝'
	else:
		brics.loc[w, u'标签'] = u'其他'

brics.to_csv(u"C:\\Users\\92452\\Desktop\\f.csv")
print brics