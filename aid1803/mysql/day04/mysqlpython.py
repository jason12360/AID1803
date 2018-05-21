import pymysql


class MysqlPython:
    def __init__(self, db, host='localhost', port=3306,  user='root', passwd='123456', charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def __enter__(self):
        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    passwd=self.passwd,
                                    db=self.db,
                                    port=self.port,
                                    charset=self.charset
                                    )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self,exec_type,exec_value,exec_tb):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print('ok')


with MysqlPython('day04') as sqltool:
    sqltool.execute('select * from ICBC;')

