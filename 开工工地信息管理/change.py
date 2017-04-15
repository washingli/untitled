# coding=utf-8

import requests
import json

#由地址调用api算出经纬度等
def locatebyAdd(address, city=None):
    items={'output':'json','ak':'n9qc4tGrNVQ3K1dDR5773ZIsljF3Vkgx','address':address}
    if city:
        items['city']=city
    r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
    # print(r.text)
    dictResult = json.loads(r.text)

    return dictResult['result']['location']if not dictResult['status']else None

# 有经纬度算出大致地址
def locatebyLatLon(lat, lon, pois=0):

    items = {'location': str(lat) + ',' + str(lon), 'ak': 'n9qc4tGrNVQ3K1dDR5773ZIsljF3Vkgx', 'output': 'json'}
    if pois:
        items['pois'] = 1
    r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
    dictResult = json.loads(r.text)
    return dictResult['result'] if not dictResult['status'] else None

def main():
    address = input('输入地址：')
    city = input('输入城市：（可选）')
    result = locatebyAdd(address, city)
    print(result)

if __name__ == '__main__':
    main()