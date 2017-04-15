# coding=utf-8

import pandas as pd
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
brics = pd.read_csv(u"C:\\Users\\92452\\Desktop\\a.csv", encoding='gbk')

for w in brics.index:
	if re.search(u'涨', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'上涨'
	elif re.search(u'回落', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'稳中', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'稳定'
	elif re.search(u'下跌', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'降', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'稳', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'稳定'
	elif re.search(u'走低', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'跌', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'偏低', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'弱', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'低迷', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'回升', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'上涨'
	elif re.search(u'反弹', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'上涨'
	elif re.search(u'走高', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'上涨'
	elif re.search(u'升', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'上涨'
	elif re.search(u'下行', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	elif re.search(u'降势', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'下降'
	else:
		brics.loc[w, u'标签'] = u'未知'

brics.to_csv(u"C:\\Users\\92452\\Desktop\\f.csv")
print brics