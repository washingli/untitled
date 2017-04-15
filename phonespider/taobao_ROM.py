# coding=utf-8
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import re

import urllib
import urllib.request
import html.parser
import requests
from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar


x=0
y=0
z=0
k=0
q=0
data_csv=pd.DataFrame(columns=['product','configuration','productshop','sales'])
import requests
import re

cs_url  = 'https://login.m.taobao.com/login.htm?_input_charset=utf-8'
# cs_user = 'user'
# cs_psw  = 'psw'
my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
               'Accept-Language':'zh-CN,zh;q=0.8',
                'Accept-Encoding':'gzip, deflate, sdch',
              'Cookie':'thw=cn; v=0; _tb_token_=fb78537e6771d; existShop=MTQ4ODgwMDU3OQ%3D%3D; cookie2=3c2514d526b1ddb31b5a7cadb3c7c4a4; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261488810470285; linezing_session=m0Y7RhYZGNBTfnePWN4CyyWE_1489411016833n8E7_3; UM_distinctid=15ac7d08731e-010bc14f6331a1-3e64430f-100200-15ac7d08732fd; _uab_collina=148941354970738009628602; ockeqeudmj=uDTxrls%3D; munb=1835402284; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BK1yiN9dFUnQQsT5dBR0%3D; _w_app_lg=19; yryetgfhth=%2B4cXpeDzLTAIW6kFUQRXP%2FykkQA5bmTeuI4tvm5k5tg454DVi03SezVUmNpYVXOqCtEtJmAJw88bO%2BnI7kZEP8AtVXF8sKdiYPc2qa7Xx8tF%2FDgMMoDKbBWt7MytQxrRQoadUYZcEbqDC0H5WrL5UFnkBSND2GZUKk0AfX4jYfg%2B3mDsluq3XLcQyk0hi1XMMBrb; uc3=sg2=W8t8ZBrp6WZPSJAPKnF2mmWJbzDnzwbA5p7CeeS08pg%3D&nk2=FPjHOD3eS052wqDx&id2=UonYtKcLq0d7Ow%3D%3D&vt3=F8dARVWNVOd344Zyhtc%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; uc1=cookie14=UoW%2FVOb21tJjCw%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&cookie15=VFC%2FuZ9ayeYq2g%3D%3D; lgc=washingli007; tracknick=washingli007; ntm=0; skt=9d259e627d6a547e; t=bdedf0d2ba601c9a1b0d0778370bc225; _cc_=Vq8l%2BKCLiw%3D%3D; cna=ev7bEDOHuUMCAbSgkLaBGPlz; _umdata=E01C1DF6322B4D0E39047E15D1B9174CDA55778F9CD5F2C22DD975B91297A56523A69978DEA6C02DCD43AD3E795C914CCE0E9ED60E5EAF8F8570E2AD4ACFF968; l=AmNjV6X1xc6NGXBsaIJ3NIYJc7wNWPea; isg=AsHBPIxXfdZgQJFxg7yU7xbc0A0qtDXghHA0hiMWvkgnCuLcfD6Nsc1InsSz',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Content-Type':'text/html;charset=UTF-8'}
sss= requests.Session()
r       = sss.get(cs_url, headers = my_headers)
# print(r.text)
# reg     = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
# pattern = re.compile(reg)
# result  = pattern.findall(r.content)
# token   = result[0]
my_data = values={'TPL_username':'washingli007','TPL_password':'1994n7n12r'}
# for p in range(1,5):
#     p=str(p)

cs_url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000722.109.xlMkoV&cat=50024400&q=%CA%D6%BB%FA&prop=12304004:21555&sort=s&style=g&search_condition=4&sarea_code=310100&from=sn_1_prop&industryCatId=50024400#J_crumbs'
# cs_url  = 'https://list.tmall.com/search_product.htm?type=pc&q=%CA%D6%BB%FA&totalPage=100&sort=s&style=g&sarea_code=310100&jumpto=1#J_Filter'
r = sss.post(cs_url,  data = my_data,headers = my_headers)
# print (r.url, r.status_code,r.text)
# print(r.ok)
# print(r.text)
soup=bs(r.text,'html.parser')
# print(soup.find_all('span'))




# for p in range(1):
#     p=str(p)
#
#     url = 'https://list.tmall.com/search_product.htm?type=pc&q=%CA%D6%BB%FA&totalPage=100&sort=s&style=g&sarea_code=310100&jumpto=' + p + '#J_Filter'

# try:
#     req = urllib.request.Request(url, None, {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
#     cj = CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     response = opener.open(req)
#     raw_response = response.read().decode('utf-8', errors='ignore')
#     response.close()
#     print(raw_response)
# except urllib.request.HTTPError as inst:
#     output = format(inst)
#     print(output)


# soup=bs(raw_response,'html.parser')
# print(soup)
soupprice=soup.find_all('p', class_="productPrice")
for m in soupprice:
    price=m.find('em').text
    price=re.sub('¥','',price)
    # print(price)
    data_csv.loc[q,'price']=price
    q=q+1
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
data_csv.to_csv('H:\\毕业设计\\phone1(ram6G)3.24.csv')

