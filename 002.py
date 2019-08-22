#第二个练习 - 新增用户数据
import sqlite3
conn = sqlite3.connect('mr.db')
cursor = conn.cursor()
cursor.execute('insert into user (id,name) values ("1", "mrsoft")')
cursor.execute('insert into user (id,name) values ("2", "Andy")')
cursor.execute('insert into user (id,name) values ("3", "小助手")')
cursor.close()
conn.commit()
conn.close()