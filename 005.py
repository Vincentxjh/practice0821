#第五个练习 - 删除用户数据
import sqlite3
conn = sqlite3.connect('mr.db')
cursor = conn.cursor()
cursor.execute('delete from user where id = 1')
cursor.execute('select * from user')
result = cursor.fetchall()
print(result)
cursor.close()
conn.commit()
conn.close()