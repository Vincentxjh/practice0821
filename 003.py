#第三个练习 - 查询用户数据信息

import sqlite3
conn = sqlite3.connect('mr.db')
cursor = conn.cursor()
cursor.execute('select * from user')
result1 = cursor.fetchone()
print(result1)
result2 = cursor.fetchmany(2)
print(result2)
result3 = cursor.fetchall()
print(result3)
cursor.execute('select * from user where id > ?',(1,))
result4 = cursor.fetchall()
print(result4)
cursor.close()
conn.close()