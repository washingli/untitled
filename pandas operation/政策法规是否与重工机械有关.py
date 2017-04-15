# coding=utf-8

import pandas as pd
import re

brics = pd.read_csv("D:\\a.csv")
keywords = pd.read_csv("D:\\key.csv")
for x in keywords.sort_index():
#	for w in brics.sort_index():
		# if x==w:
		# 	brics.loc[w, '标签'] =keywords.keys()
		# else:
		# 	brics.loc[w, '标签'] = '其他'





#brics.to_csv("D:\\b.csv")
	print x