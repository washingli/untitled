# coding=utf-8
import pandas as pd
import re

brics = pd.read_csv("D:\\a.csv")

for x in brics.index:
	select_sw = re.search(' .+', brics.loc[x, 'dd'])
	if select_sw:
		print(brics.loc[x, 'dd'])
	# 	s = select_sw.group()
	# 	y = s[1:len(s)]
	# 	brics.loc[x, '厂家'] = y
	#
	# 	select_sw1 = re.match('.+ ', brics.loc[x, 'dd'])
	# 	s = select_sw1.group()
	# 	w = s[0:len(s) - 1]
	# 	brics.loc[x, '车种类'] = w
	#
	# else:
	# 	brics.loc[x, '厂家'] = brics.loc[x, 'dd']

# for z in brics.index:
# 	select_sw = re.match(' .+', brics.loc[z, 'dd'])
# 	if select_sw:
# 		s = select_sw.group()
# 		w = s[0:len(s) - 1]
# 		brics.loc[z, '车种类'] = w



# brics.to_csv("D:\\b.csv")

# print brics
