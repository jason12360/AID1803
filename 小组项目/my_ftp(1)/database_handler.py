# 这是一个用来负责和数据库连接，并处理和数据库相关的函数

import pymysql
import re
from file import File



class My_Mysql:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456",
                                  "crazy_coder", charset="utf8")
        self.cursor = self.db.cursor()

    def close(self):

        self.cursor.close()
        self.db.close()

# 用户表——————————————————————————————————————————
    def create_user_table(self):
        self.cursor.execute(
            'create table user(id int primary key auto_increment,username char(20) unique,password char(30))default charset=utf8;')
        self.db.commit()
    # 增加用户

    def add_user(self, username, password):
        sql = 'insert into user(username,password) values("%s","%s");' % (
            username, password)
        self.cursor.execute(sql)
        self.db.commit()

    # 查询用户
    def select_user(self, username):
        sql = 'select * from user where username = "%s"' % (username)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
# 用户查询表———————————————————————————————————————

    def create_userlog_table(self):
        self.cursor.execute('create table userlog(id int primary key auto_increment,\
                                                  user_id int,\
                                                  file_id int,\
                                                  log_time datetime,\
                                                  operation enum("upload","download"),\
                                                  foreign key(user_id) references user(id) \
                                                  on delete cascade \
                                                  on update cascade,\
                                                  foreign key(file_id) references file(id)\
                                                  on delete cascade\
                                                  on update cascade)default charset=utf8;')
    # 增加用户查询条目

    def add_userlog(self, user_log):
        sql = 'insert into userlog(user_id,file_id,operation,log_time) values(%d,%d,"%s",%d);' % user_log
        self.cursor.execute(sql)
        self.db.commit()

    # 查询用户查询条目
    def select_userlog(self):
        sql = '	select user.username,file.filename,userlog.operation,userlog.log_time from userlog \
				inner join user on userlog.user_id = user.id\
				inner join file on userlog.file_id = file.id'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
# 文件表——————————————————————————————————————————

    def create_file_table(self):
        self.cursor.execute(
            'create table file(id int primary key auto_increment,\
                               filename char(50),\
                               filesize int,\
                               file_path_on_server char(50),\
                               last_modified_time datetime,\
                               first_create_time datetime)default charset=utf8;')

    def add_file(self, file):
        sql = 'insert into file(filename,filesize,file_path_on_server,\
                                last_modified_time,first_create_time)\
                                 values("%s",%d,"%s",%d,%d);' % file.get_info()
        self.cursor.execute(sql)
        self.db.commit()
    # 查询文件

    def select_file_by_id(self, id):
        sql = 'select * from file where id = %d' % id
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_file_by_filename(self, filename):
        sql = 'select * from file where filename = "%s"' %filename
        self.cursor.execute(sql)
        return self.cursor.fetchall()


def main():
    my_mysql = My_Mysql()
    my_mysql.create_user_table()
    my_mysql.create_file_table()
    my_mysql.create_userlog_table()
    # my_mysql.add_user('jason','12345')
    # print(my_mysql.select_user('jason'))
    # f = File('database_handler.py')
    # f.set_last_mtime(20180101101010)
    # f.set_file_create_time(20180101101010)
    # print(f.get_info())
    # my_mysql.add_file(f)
    # print(my_mysql.select_file_by_filename('database_handler.py'))
    # my_mysql.add_userlog((1,1,'upload',10200912000000))
    # print(my_mysql.select_userlog())

    my_mysql.close()


if __name__ == '__main__':
    main()
