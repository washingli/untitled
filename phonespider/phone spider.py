# coding=utf-8
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import re
x=0
y=0
z=0
k=0
q=0
data_csv=pd.DataFrame(columns=['product','configuration','productshop','sales'])
for p in range(1,9):
    p=str(p)

    url='https://list.tmall.com/search_product.htm?type=pc&q=%CA%D6%BB%FA&search_condition=4&totalPage=19&cat=50024400&sort=s&style=g&from=sn_1_prop&sarea_code=310100&jumpto='+p+'#J_crumbs'
    html=urlopen(url)
    soup=bs(html.read(),'html.parser')
    # print(soup)
    soupprice = soup.find_all('p', class_="productPrice")
    for m in soupprice:
        price = m.find('em').text
        price = re.sub('¥', '', price)
        # print(price)
        data_csv.loc[q, 'price'] = price
        q = q + 1
    soup1=soup.find_all('div',class_='productTitle')
    # print(soup1)
    for m in soup1:
        product=m.find('a').text                                 #product
        # print(product.text)
        data_csv.loc[x,'product']=product  #into csv
        x=x+1
        config=m.find('a').get('title')                           #configuration
        # print(config)
        data_csv.loc[y,'configuration']=config  #into csv
        y=y+1
    soup2=soup.find_all('a',class_='productShop-name')
    for n in soup2:
        productshop=n.text                                         #productshop
        productshop1=re.sub('(\n)|(\t)|(' ')','',productshop)
        productshop2 = re.sub(' ', '', productshop1)
        # print(productshop)
        data_csv.loc[z,'productshop']=productshop2   #into csv
        z=z+1
    soupfinal=soup.find_all('div',class_='product')
    # print(soupfinal)
    for m in soupfinal:
        if(m.find('p',class_='productStatus')):
            soup3=m.find('p',class_='productStatus')
            sale=soup3.text
            # print(sale)
            sale1=re.sub('该款月成交','',sale)
            sale2=re.sub(' ','',sale1)
            if(re.search('万笔',sale2)):
                sale3=float(re.sub('[^ -~]','',sale2))* 10000
            elif(re.search('笔',sale1)):
                sale3=float((re.sub('[^ -~]','',sale2)))
        else:
            sale3=None
        data_csv.loc[k, 'sales'] = sale3  # into csv
        k = k + 1
        # print(sale3)
print(data_csv)
data_csv.to_csv('H:\\毕业设计\\shangchengphone(1-9)3.24.csv')

