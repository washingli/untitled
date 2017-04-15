#conding=utf-8

import pymongo
from 开工工地信息管理 import change


client = pymongo.MongoClient('192.168.1.50', 27017)
db = client.mydb
collection = db.projectIM

for a in collection.find():
    print(a['开工信息的地理位置'])
    dd = a['开工信息的地理位置']
    jwd = change.locatebyAdd(dd)
    print(a['_id'])
    print(jwd)
    collection.update({'_id':a['_id']},{'$set':{'经纬度':jwd}})

    print(a)
print(collection.find_one())