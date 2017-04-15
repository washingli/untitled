# coding=utf-8

import pandas as pd
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
brics = pd.read_csv(u"C:\\Users\\92452\\Desktop\\a.csv", encoding='gbk')

for w in brics.index:
	if re.search(u'证监会', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'证监会'
	elif re.search(u'国家税务总局', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'国家税务总局'
	elif re.search(u'外汇局', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'外汇局'
	elif re.search(u'卫生计生委', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'卫生计生委'
	elif re.search(u'农业部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'农业部'
	elif re.search(u'水利部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'水利部'
	elif re.search(u'公安部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'公安部'
	elif re.search(u'商务部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'商务部'
	elif re.search(u'统计局', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'统计局'
	elif re.search(u'文化部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'文化部'
	elif re.search(u'财政部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'财政部'
	elif re.search(u'审计署', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'审计署'
	elif re.search(u'民航局', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'民航局'
	elif re.search(u'交通运输部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'交通运输部'
	elif re.search(u'国家安全生产监督管理总局', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'国家安全生产监督管理总局'
	elif re.search(u'工商总局', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'工商总局'
	elif re.search(u'发改委', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'发改委'
	elif re.search(u'人社部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'人社部'
	elif re.search(u'信访局', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'信访局'
	elif re.search(u'人力资源和生活保障部', brics.loc[w, u'标题']):
		brics.loc[w, u'标签'] = u'人力资源和社会保障部'
	else:
		brics.loc[w, u'标签'] = u'其他部门'

brics.to_csv(u"C:\\Users\\92452\\Desktop\\f.csv")
print brics