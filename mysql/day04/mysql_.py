import pymysql

# 1.创建数据库连接
db = pymysql.connect("localhost", "root", "123456",
                     "day03", charset="utf8")

# 2.创建游标对象
cursor = db.cursor()

# 3.利用游标对象cursor的方法来操作数据库
cursor.execute('insert into sheng values(11,200000,\
	             "四川省");')

# 4.提交到数据库commit
db.commit()

# 关闭游标对象
cursor.close()

# 关闭数据库连接
db.close()
