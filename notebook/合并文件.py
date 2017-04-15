import pandas as pd
import re
result1=pd.read_csv("C:\\Users\\hc\\Desktop\\E5生产原材料.csv",encoding='utf-8')
result2=pd.read_csv("C:\\Users\\hc\Desktop\\-E5生产原材料.csv",encoding='utf-8')
connect=pd.merge(result1,result2,how='outer')#所有的并集，相同的覆盖
# connect=pd.merge(result2,result1,left_on='专利名称',right_on='专利名称')#（交集）相同的（字段）列出并出现value_x和value_y
# connect=result1.combine_first(result2)#所有的并集，相同的不覆盖
# connect=result1.append(result2)#所有的并集，相同的不覆盖，而且index不重新排列
connect.to_csv("C:\\Users\\hc\\Desktop\\1.csv")
print(connect)