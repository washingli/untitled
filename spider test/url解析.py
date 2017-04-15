from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj
    except AttributeError as e:
        return None
    return title

title = getTitle("https://list.tmall.com/m/search_items.htm?page_size=20&page_no=1&spm=a220m.1000858.0.0.2LhZr2&q=%CA%D6%BB%FA&sort=s&style=g&sarea_code=310100&active=1&shopType=any&type=pc")
if title == None:
    print("Title could not be found")
else:
    print(title)