
import pymysql

try:
	conn=pymysql.connect(host='192.168.3.59',port=3306,user='hadoop',passwd='chinacloud',charset='utf8')
except Exception,e:
print(e)

cur=conn.cursor()
cur.execute('select id,password from accont')
for i,p in cur:
	print('ID:{},PASS{}').format(i,p)
cur.executemany('insert into account values (%s,%s))',[(4,'004'),(5,'005')])
cur=conn.cursor()
