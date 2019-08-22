#第六个练习 - 使用PyMySQL连接数据库

import pymysql
db = pymysql.connect('localhost', 'root', 'root123', 'studyPython')
cursor = db.cursor()
cursor.execute('select version()')
date = cursor.fetchone()
print('Datebase version: %s' %date)
cursor.close()
db.close()