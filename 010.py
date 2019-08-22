#第十个练习 - 查找指定年份之后的图书信息

import pymysql
db = pymysql.connect('localhost','root','root123','studypython')
cursor = db.cursor()
cursor.execute("select * from books where (price < 70 and publish_time >= '2017-1-1')")
data = cursor.fetchall()
for item in data:
    print("图书：《{}》, 价格：￥{}元，出版日期：{}".format(item[1],item[3],item[4]))
db.close()