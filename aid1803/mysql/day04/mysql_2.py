import pymysql

db = pymysql.connect("localhost", "root", "123456", "day03", charset="utf8")
cursor = db.cursor()
sql_select = "select * from city;"
cursor.execute(sql_select)
print('fetchone 的结果为',cursor.fetchone())
print('fetchall 的结果为',cursor.fetchall())
print('fetchmany 的结果为',cursor.fetchmany(2))



db.commit()
cursor.close()
db.close()
