#encoding='utf-8'
import pandas as pd
import re
data_csv1=pd.read_csv("H:\\毕业设计\\size\\phone1111(3.14.csv",encoding='gbk')
data_csv2 = pd.read_csv("H:\\毕业设计\\size\\phone2222(3.14.csv",encoding='gbk')


def Append(file1,file2):
    connect = file1.append(file2)
    return connect

if __name__ == '__main__':
    connect=Append(data_csv1,data_csv2)
    print(connect)
    connect.to_csv("H:\\毕业设计\\size\\phonesize(3.14.csv",encoding='gbk')