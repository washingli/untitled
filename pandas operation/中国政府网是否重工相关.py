
# coding=utf-8

import pandas as pd
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
brics = pd.read_csv(u"C:\\Users\\92452\\Desktop\\a.csv", encoding='gbk')

for w in brics.index:
	if re.search(u'钢铁', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'煤炭', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'重工', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'机械', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'工程', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'三一', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'徐工', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'厦工', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'小松', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	elif re.search(u'龙工', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'是'
	else:
		brics.loc[w, u'标签'] = u'否'

brics.to_csv(u"C:\\Users\\92452\\Desktop\\f.csv")
