# coding=utf-8
import pandas as pd
import pymysql
import pymongo

conn = pymysql.connect(host='192.168.1.50', user='washingli',
                       password='qwert', db='origin', charset='utf8')
try:
    sql = "select * from 路面机械产经新闻"
    df_mysql = pd.read_sql(sql, conn)
    data_dict = df_mysql.to_dict(orient='records')
    print(df_mysql)

finally:
    conn.close()

client = pymongo.MongoClient("localhost", 27017)
db = client.mydb
collection = db.cjxw

# post = {'a': 'b'}

collection.insert_many(data_dict)

print(collection.find_one())
