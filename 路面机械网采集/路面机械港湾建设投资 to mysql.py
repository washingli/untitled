import pymysql
import pandas as pd

data = pd.read_csv("D:\重工招标信息\路面机械港湾建设投资.csv")
print(data)
for i in data.index:
    a = data.loc[i, '工程项目']
    b = data.loc[i, '项目简介']
    c = data.loc[i, '发布日期']
    d = data.loc[i, 'PageUrl']
    print(a,b,c,d)

    conn = pymysql.connect(host='192.168.1.50', user='washingli', password='qwert', db='origin', charset='utf8')
    try:
        cursor = conn.cursor()

        # 插入数据

        cursor.execute("insert into 路面机械港湾建设投资(工程项目,项目简介,发布日期,PageUrl) values(%s,%s,%s,%s)",(a,b,c,d))
        # 更新数据
        # cursor.execute("update 路面机械招标信息 set 发布日期='2'")
        # 查找数据
        # cursor.execute("select 工程项目,项目详情,发布日期,pageUrl from 路面机械招标信息")
        # 输出数据
        # for a,b,c,d in cursor:
        #     print(a,b,c,d)

        #删除数据
        # cursor.execute("delet all from 路面机械招标信息")
        conn.commit()

    finally:
        conn.close()



