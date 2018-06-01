#!/usr/bin/env/python3
#coding = utf-8
'''
name:jason
date:5-30
email:370828117@qq.com
MODULES: python3.5 mysql pymysql
This is a dict project for AID1803
'''
from socket import *
from multiprocessing import *
import signal
import database_handler
import datetime
import sys
import os
# 定义一个服务器类用于封装服务器端的操作方法


class DictServer:
    def __init__(self, server_addr):
        self.mysocket = socket()
        self.mysocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.mysocket.bind(server_addr)
        self.mysocket.listen(5)
        self.server_name = server_addr[0]
        self.server_port = server_addr[1]
        self.my_database_handler = database_handler.My_Mysql()
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    def serve_forever(self):
        '''
        等待客户端的连接，每有一个连接创建一个新的进程进行处理
        '''
        while True:
            try:
                self.my_connection, self.client_addr = self.mysocket.accept()
                print('Connect from:', self.client_addr)
            except KeyboardInterrupt:
                os._exit(0)
            except:
                continue
            client_process = Process(target=self.request_handler)
            client_process.start()

    def request_handler(self):
        while True:
            data = self.my_connection.recv(1024)
            if data.decode() == 'L':
                self.do_login()
            elif data.decode() == 'R':
                self.do_register()
            elif data.decode() == 'S':
                self.do_search()
            elif data.decode() == 'H':
                self.do_history()
            elif data.decode() == 'Q':
                self.do_quit()

    def do_quit(self):
        print(self.client_addr, '离线')
        self.my_database_handler.close()
        self.my_connection.close()
        os._exit(0)

    def do_login(self):
        self.my_connection.send(b'Y')
        up_data = self.my_connection.recv(1024).decode()
        up_list = up_data.split('|')
        username, password = up_list[0], up_list[1]
        result = self.my_database_handler.select_user(username)
        if not result or result[0][2] != password:
            self.my_connection.send(b'N')
        else:
            self.user_id = result[0][0]
            self.username = result[0][1]
            self.my_connection.send(b'Y')

    def do_register(self):
        self.my_connection.send(b'Y')
        up_data = self.my_connection.recv(1024).decode()
        up_list = up_data.split('|')
        username, password = up_list[0], up_list[1]
        data = self.check_up(username, password)
        if data == 'Y':
            try:
                self.my_database_handler.add_user(username, password)
                self.username = username
            except:
                data = 'N'+'服务端数据库写入错误'
        self.my_connection.send(data.encode())

    def do_search(self):
        self.my_connection.send(b'Y')
        word = self.my_connection.recv(1024).decode()
        result = self.my_database_handler.select_dictionary(word)
        data = ''
        if not result:
            data = '查不到这个单词'
        else:
            dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            dict_id = result[0][0]
            meaning = result[0][2]
            self.my_database_handler.add_userlog(
                (int(self.user_id), int(dict_id), int(dt)))
            data = '释义是：'+meaning
        self.my_connection.send(data.encode())

    def do_history(self):
        self.my_connection.send(b'Y')
        results = self.my_database_handler.select_userlog(self.username)
        data = ''
        for result in results:
            _buffer = result[0]+'|' + result[2] + '|' + \
                result[1].strftime('%Y-%m-%d %H:%M:%S')+'\n'
            data += _buffer
        self.my_connection.send(data.encode())

    def check_up(self, username, password):
        if (not username) or (not password):
            return 'N'+'用户名或密码不能为空'
        if self.my_database_handler.select_user(username):
            return 'N'+'用户名已存在'
        return 'Y'


def main():
    if len(sys.argv) < 3:
        print('argv is error')
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        ADDR = (HOST, PORT)
    my_dict_server = DictServer(ADDR)
    my_dict_server.serve_forever()


if __name__ == '__main__':
    main()
