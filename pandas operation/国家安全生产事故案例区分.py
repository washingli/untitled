# coding=utf-8

import pandas as pd
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
brics = pd.read_csv(u"C:\\Users\\92452\\Desktop\\a.csv", encoding='gbk')

for w in brics.index:
	if re.search(u'案例', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'案例'
	elif re.search(u'事故', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'事故'
	else:
		brics.loc[w, u'标签'] = u'其他'

brics.to_csv(u"C:\\Users\\92452\\Desktop\\f.csv")
print brics