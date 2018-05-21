import mysqlpython

mysql = mysqlpython.MysqlPython(db='day03')
sql_update = 'update sheng set id=150 where id=1;'
mysql.execute(sql_update)