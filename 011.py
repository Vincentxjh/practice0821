#第十一个练习 - 批量删除指定的图书信息
import pymysql
db = pymysql.connect('localhost','root','root123','studypython')
cursor = db.cursor()
cursor.execute("delete from books where category = 'PHP'")
db.commit()
cursor.execute("select * from books")
data = cursor.fetchall()
for item in data:
    print("图书：《{}》, 价格：￥{}元".format(item[1],item[3]))
db.close()