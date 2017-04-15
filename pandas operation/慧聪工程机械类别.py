
# coding=utf-8

import pandas as pd
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
brics = pd.read_csv(u"C:\\Users\\92452\\Desktop\\a.csv", encoding='gbk')

for w in brics.index:
	if re.search(u'挖掘机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'挖掘机'
	elif re.search(u'装载机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'装载机'
	elif re.search(u'搅拌车', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'搅拌机'
	elif re.search(u'吊车', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'吊车'
	elif re.search(u'塔吊', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'塔吊'
	elif re.search(u'铲车', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'铲车'
	elif re.search(u'重载工程车', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'重载工程车'
	elif re.search(u'起重机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'起重机'
	elif re.search(u'救援机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'救援机'
	elif re.search(u'提升机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'提升机'
	elif re.search(u'挖机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'挖机'
	elif re.search(u'工程车', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'工程车'
	elif re.search(u'推土机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'推土机'
	elif re.search(u'重型半挂牵引车', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'重型半挂牵引车'
	elif re.search(u'压路机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'压路机'
	elif re.search(u'平地车', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'平地车'
	elif re.search(u'铣刨机', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'铣刨机'
	else:
		brics.loc[w, u'标签'] = u'其他'

brics.to_csv(u"C:\\Users\\92452\\Desktop\\f.csv")
print brics
