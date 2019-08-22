#第一个练习 - 创建SQLite数据库文件

import  sqlite3
conn = sqlite3.connect('mr.db')
cursor = conn.cursor()
cursor.execute('create table user (id int(10), name varchar (20))')
cursor.close()
conn.close()
