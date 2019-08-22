#第九个练习 - 获取指定数据表中的信息

import pymysql
db = pymysql.connect('localhost','root','root123','studypython')
cursor = db.cursor()
cursor.execute('select * from books')
data = cursor.fetchall()
for item in data:
    print("图书：《{}》, 价格：￥{}元".format(item[1],item[3]))
db.close()
