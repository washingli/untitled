from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

html=urlopen('http://peijian.lmjx.net/wjj/?p=2')
bsobj=bs(html,"html.parser")
# print(bsobj)
# product name
names=bsobj.find_all('h2')
i=1
for n in names:
    i=i+1
print(i)
for n in range(i-4):
    name=names[n].text
    print(name)
# 4 field
four_field=bsobj.find_all('div')
for n in four_field:
    if n.find('span',class_='s'):
        print(n.get_text())

