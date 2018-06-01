# 这是一个用来负责和数据库连接，并处理和数据库相关的函数

import pymysql
import re


class My_Mysql:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456",
                                  "dictionary", charset="utf8")
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
        self.cursor.execute('create table userlog(id int primary key auto_increment,user_id int,dict_id int,log_time datetime,foreign key(user_id) references user(id) on delete cascade on update cascade,foreign key(dict_id) references dict(id) on delete cascade on update cascade)default charset=utf8;')
    # 增加用户查询条目

    def add_userlog(self, user_log):
        sql = 'insert into userlog(user_id,dict_id,log_time) values(%d,%d,%d);' % user_log
        self.cursor.execute(sql)
        self.db.commit()

    # 查询用户查询条目
    def select_userlog(self, username):
        sql = '	select user.username,userlog.log_time,dict.vocabulary from userlog \
				inner join user on userlog.user_id = user.id\
				inner join dict on userlog.dict_id = dict.id\
				where user.username = "%s"' % username
        self.cursor.execute(sql)
        return self.cursor.fetchall()
# 字典表——————————————————————————————————————————

    def create_dictonary_table(self):
        self.cursor.execute(
            'create table dict(id int primary key auto_increment,vocabulary char(50),meaning text)default charset=utf8;')

    def add_all_words(self, resource_file):
        with open(resource_file, 'r') as file_obj:
            while True:
                line = file_obj.readline()
                if not line:
                    break
                line_list = re.split(r'[ ]+', line)
                sql = 'insert into dict(vocabulary,meaning) values("%s","%s");' % (
                    line_list[0], pymysql.escape_string(' '.join(line_list[1:])))
                self.cursor.execute(sql)
        self.db.commit()
    # 查询字典

    def select_dictionary(self, vocabulary):
        sql = 'select * from dict where vocabulary = "%s"' % (vocabulary)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


def main():
    my_mysql = My_Mysql()
    # try:
    # 	# # my_mysql.create_user_table()
    # print(my_mysql.select_user('jason','123214'))
    # 	# # my_mysql.create_dictonary_table()
    # my_mysql.create_userlog_table()
    # my_mysql.add_userlog((1,14043,20180912000000))
    # except pymysql.err.InternalError:
    # 	pass
    # # finally:
    # # my_mysql.add_all_words('word.txt')
    print(my_mysql.select_user('asd') == True)
    # print(my_mysql.select_dictionary('army'))
    my_mysql.close()


if __name__ == '__main__':
    main()
