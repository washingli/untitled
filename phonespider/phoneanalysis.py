#encoding='utf-8'
import pandas as pd
import re
import numpy as np
allphones=pd.read_csv("H:\\毕业设计\\tianmaoshangchengphone(1-19)3.29.csv",encoding='gbk')
# print(allphones)
data_csv=pd.DataFrame(columns=['brand','product','sales'])
x=0
# print(allphones)
# print(allphones.sort_index(by='sales'))             #手机总排行
brands=pd.read_csv("H:\\毕业设计\\phonebrands.csv",encoding='gbk')
for m in allphones.index:
    product=allphones.loc[m,'product']
    for n in brands.index:
        if(re.search(brands.loc[n,'brand'],product)):
            allphones.loc[m,'brand']=brands.loc[n,'brand']
            break
# print(allphones)
def totlerank(phones):                                  #手机品牌总排行
    rank1=phones.sort_index(by='sales',ascending=False).reset_index()
    return rank1

def brandrank(phones):                                       #手机按品牌排行
    rank2=phones['sales'].groupby(phones['brand'])
    rank2=rank2.aggregate(np.sum).reset_index().sort(['sales'],ascending=False).reset_index()
    return rank2

def brandinternaorank(phones):                                       #手机品牌内部排行
    rank3=phones['sales'].groupby([phones['brand'],phones['product'],phones['price']])
    rank3=rank3.sum()

    rank3=pd.DataFrame(rank3).reset_index()
    return rank3
def pricerangerank(phones):                                     #价格区间排行
    for m in phones.index:
        if(phones.loc[m,'price']<500):
            phones.loc[m,'pricerange']='0~500'
        elif(phones.loc[m,'price']<1000):
            phones.loc[m,'pricerange']='500~1000'
        elif (phones.loc[m, 'price'] < 1500):
            phones.loc[m, 'pricerange'] = '1000~1500'
        elif (phones.loc[m, 'price'] < 2000):
            phones.loc[m, 'pricerange'] = '1500~2000'
        elif (phones.loc[m, 'price'] < 3000):
            phones.loc[m, 'pricerange'] = '2000~3000'
        elif (phones.loc[m, 'price'] < 4000):
            phones.loc[m, 'pricerange'] = '3000~4000'
        else :
            phones.loc[m, 'pricerange'] = '4000以上'
    rank4=phones['sales'].groupby([phones['pricerange'],phones['brand']])
    rank4=rank4.sum()
    rank4 = pd.DataFrame(rank4).reset_index()
    return(rank4)
if __name__ == '__main__':
    rank1=totlerank(allphones)
    print(rank1[0:50])
    rank2=brandrank(allphones)
    print(rank2)
    # print(rank2['brand'][0:15])
    rank3=brandinternaorank(allphones)
    print(rank3)
    # for m in rank2['brand'][0:15]:
    #     print(m)
    #     for n in rank3.index:
    #         if(rank3.loc[n,'brand']==m):
    #             print(rank3.loc[[n]]
    rank3.to_csv("C:\\Users\\washingli\\Desktop\\手机品牌内部排行.csv")
    rank4=pricerangerank(allphones)
    print(rank4)


