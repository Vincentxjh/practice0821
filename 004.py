#第四个练习 - 修改用户数据信息

import sqlite3
conn = sqlite3.connect('mr.db')
cursor = conn.cursor()
cursor.execute('update user set name = ? where id = ?',('Mrsoft',1))
cursor.execute('select * from user')
result = cursor.fetchall()
print(result)
cursor.close()
conn.commit()
conn.close()