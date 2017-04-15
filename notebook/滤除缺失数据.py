import numpy
import pandas as pd
from numpy import nan as NA
result=pd.read_csv("C:\\Users\\hc\\Desktop\\订单动态.csv",encoding='utf-8')
noNAN=result.dropna()
noNAN.to_csv("C:\\Users\\hc\\Desktop\\订单动态2.csv")
print(noNAN)


#一行中只要有一个空格缺失就可以将整行去掉