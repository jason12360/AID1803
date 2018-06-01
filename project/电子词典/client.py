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
import sys
import os
import getpass


class DictClient:
    def __init__(self, server_addr):
        self.myconnection = socket()
        self.myconnection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.myconnection.connect(server_addr)

    def run(self):
        self.show_first_menu()

    def show_first_menu(self):
        print('''
        	   =========Welcome========
        	   --1.登录  2.注册  3.退出--
        	   ========================
        	   ''')
        command = input('请选择：')
        if command == '1':
            self.do_login()
        elif command == '2':
            self.do_register()
        elif command == '3':
            self.do_quit()
        else:
            print('请输入正确的选项')
            # 保证不会有缓存影响下一次输入的结果
            sys.stdin.flush()
            self.show_first_menu()

    def do_quit(self):
        self.myconnection.send(b'Q')
        os._exit(0)

    def do_login(self):
        self.myconnection.send(b'L')
        data = self.myconnection.recv(1024)
        if data.decode() == 'Y':
            self.username = input('请输入用户名:')
            password = getpass.getpass('请输入密码:')
            up_data = self.username + '|'+password
            self.myconnection.send(up_data.encode())
            data = self.myconnection.recv(1024)
            if data.decode() == 'Y':
                self.show_second_menu()
            else:
                print('用户名密码错误')
                self.show_first_menu()
        else:
            print('服务器连接失败')
            self.show_first_menu()

    def do_register(self):
        self.myconnection.send(b'R')
        data = self.myconnection.recv(1024)
        if data.decode() == 'Y':
            self.username = input('请输入用户名:')
            password = getpass.getpass('请输入密码:')
            up_data = self.username + '|'+password
            self.myconnection.send(up_data.encode())
            data = self.myconnection.recv(1024)
            if data.decode() == 'Y':
                print('注册成功')
                self.show_second_menu()
            else:
                print(data.decode()[1:])
                self.do_register()
        else:
            print('服务器连接失败')
            self.show_first_menu()

    def do_search(self):
        self.myconnection.send(b'S')
        data = self.myconnection.recv(1024)
        if data.decode() == 'Y':
            print('=======================')
            word = input('请输入要查询的单词：')
            self.myconnection.send(word.encode())
            result = self.myconnection.recv(1024)
            print('=======================')
            print('查询结果:')
            print()
            print(result.decode())
            print('=======================')
            command = input('输入“q”退出，输入“r”继续查词，输入“回车”返回上级菜单:')
            if command == 'q':
                self.do_quit()
            elif command == 'r':
                self.do_search()
            elif command == '':
                self.show_second_menu()
        else:
            print('服务器连接失败')

    def do_history(self):
        self.myconnection.send(b'H')
        data = self.myconnection.recv(1024)
        if data.decode() == 'Y':
            data = self.myconnection.recv(1024)
            print('=================')
            print(data.decode())
            print('=================')
            command = input('输入“q”退出，输入“回车”返回上级菜单:')
            if command == 'q':
                self.do_quit()
            elif command == '':
                self.show_second_menu()
        else:
            print('服务器连接失败')

    def show_second_menu(self):
        print('''
        	   ========Welcome %s=========
        	   --1.查词  2.查询历史  3.退出--
        	   ============================
        	   ''' % self.username)
        command = input('请选择：')
        if command == '1':
            self.do_search()
        elif command == '2':
            self.do_history()
        elif command == '3':
            self.do_quit()
        else:
            print('请输入正确的选项')
            # 保证不会有缓存影响下一次输入的结果
            sys.stdin.flush()
            self.show_second_menu()


def main():
    if len(sys.argv) < 3:
        print('argv is error')
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        ADDR = (HOST, PORT)
    my_dict_client = DictClient(ADDR)
    my_dict_client.run()


if __name__ == '__main__':
    main()
