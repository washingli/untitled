# coding=utf-8
#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'python进行代理的curl数据提交'
__author__ = 'ken'
import os;
import sys;
curPath = os.path.abspath(os.path.dirname(__file__));
sys.path.append(curPath);
import urllib.request;
import urllib.parse;
import socket;
class curl:
    def __init__(self):
        pass;
    # 获取用户浏览器信息
    def getUserAgent(self):
        userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0';
        return userAgent;
    # 进行数据提交
    def run(self, url, param):
        self.url = url;
        self.param = param;
        self.userAgent = self.getUserAgent();
        self.proxyIpList = ['117.135.196.197:55336', '117.158.98.214:80', '117.177.243.42:84', '117.177.243.42:85'];
        data = urllib.parse.urlencode(self.param).encode(encoding='UTF8');
        req = urllib.request.Request(self.url, data);
        req.add_header('User-Agent', self.userAgent);
        for proxyIp in self.proxyIpList:
            socket.setdefaulttimeout(3);  # 3秒未响应则为超时，跳过执行下一条
            try:
                # 添加代理
                proxy_handler = urllib.request.ProxyHandler({'http': proxyIp});
                proxy_auth_handler = urllib.request.ProxyBasicAuthHandler();
                opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler);
                # 添加头信息
                opener.addheaders = [
                    ('User-Agent', self.userAgent)
                ]
                # 数据请求
                response = opener.open(self.url, data);
                # 获取请求返还数据
                response_data = response.read().decode('utf8');
                print(proxyIp, '正确：' + response_data);
                # return response_data;
            except urllib.error.HTTPError as e:
                print(proxyIp, '错误：错误代码：', e.code);
                # print('错误内容：', e.read().decode('utf8'));
            except urllib.error.URLError as e:
                print(proxyIp, '错误：未能获取服务器信息.');
                # print('错误原因: ', e.reason);
            except:
                print(proxyIp, '错误：其他未知错误！');
# coding=utf-8
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
import re
x = 0
y = 0
z = 0
k = 0
data_csv = pd.DataFrame(columns=['product', 'configuration', 'productshop', 'sales'])
for p in range(15, 17):
p = str(p)

url = 'https://list.tmall.com/search_product.htm?type=pc&q=%CA%D6%BB%FA&totalPage=100&sort=s&style=g&sarea_code=310100&jumpto=' + p + '#J_Filter'
html = urlopen(url)
soup = bs(html.read(), 'html.parser')
# print(soup)
soup1 = soup.find_all('div', class_='productTitle')
# print(soup1)
for m in soup1:
    product = m.find('a').text  # product
    # print(product.text)
    data_csv.loc[x, 'product'] = product  # into csv
    x = x + 1
    config = m.find('a').get('title')  # configuration
    # print(config)
    data_csv.loc[y, 'configuration'] = config  # into csv
    y = y + 1
soup2 = soup.find_all('a', class_='productShop-name')
for n in soup2:
    productshop = n.text  # productshop
    productshop1 = re.sub('(\n)|(\t)|(' ')', '', productshop)
    productshop2 = re.sub(' ', '', productshop1)
    # print(productshop)
    data_csv.loc[z, 'productshop'] = productshop2  # into csv
    z = z + 1
soupfinal = soup.find_all('div', class_='product')
# print(soupfinal)
for m in soupfinal:
    if (m.find('p', class_='productStatus')):
        soup3 = m.find('p', class_='productStatus')
        sale = soup3.text
        # print(sale)
        sale1 = re.sub('该款月成交', '', sale)
        sale2 = re.sub(' ', '', sale1)
        if (re.search('万笔', sale2)):
            sale3 = float(re.sub('[^ -~]', '', sale2)) * 10000
        elif (re.search('笔', sale1)):
            sale3 = float((re.sub('[^ -~]', '', sale2)))
    else:
        sale3 = None
    data_csv.loc[k, 'sales'] = sale3  # into csv
    k = k + 1
# cu = curl();
# cu.run('www.test.com','{'key':123456789}');