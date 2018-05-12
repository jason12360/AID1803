import pymysql

db = pymysql.connect("localhost", "root", "123456", "day04", charset="utf8")
cursor = db.cursor()
try:
    cursor.execute('update CCB set money=5000 where name = "Zhuanqian";')
    cursor.execute('update ICBC set money=9000 where name = "Shouqian";')
    db.commit()
    print('ok')
except Exception as e:
    db.rollback()
    print('出现错误，已回滚')
cursor.close()
db.close()
