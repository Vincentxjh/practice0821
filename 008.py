#第八个练习 - 向Books图书表添加图书数据

import pymysql
db = pymysql.connect('localhost', 'root', 'root123', 'studypython',charset='utf8')
cursor = db.cursor()
data = [("零基础学Python", "Python", "79.80", "2018-5-20"),
        ("Python从入门到精通", "Python", "69.80", "2018-6-18"),
        ("零基础学PHP", "PHP", "69.80", "2017-5-21"),
        ("PHP项目开发实战入门", "PHP", "79.80", "2016-5-21"),
        ("零基础学Java", "Java", "69.80", "2017-5-21")]
try:
    cursor.executemany('insert into books(name, category, price, publish_time) values(%s,%s,%s,%s)', data)
    db.commit()
except:
    db.rollback()
db.close()