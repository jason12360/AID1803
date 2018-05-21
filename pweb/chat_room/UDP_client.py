'''
name = jason
chatroom client
'''

from socket import *
import sys
import os
import signal

# 子进程发送消息==============================================================================
def do_child(s, name, addr):
    while True:
        text = input('发言(输入quit退出)：')
        if text == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), addr)
            # 从子进程结束父进程
            os.kill(os.getppid(), signal.SIGKILL)
            sys.exit("退出聊天室")
        else:
            message = 'C %s %s' % (name, text)
            s.sendto(message.encode(), addr)
# 父进程接收消息=============================================================================
def do_parent(s):
    while True:
        msg, addr = s.recvfrom(1024)
        print(msg.decode() + '\n发言(输入quit退出)：', end='')

#主进程=================================================================================
def main():
    if len(sys.argv) < 3:
        print('argv is error')
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        ADDR = (HOST, PORT)
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input('请输入用户名：')
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print('进入聊天室')
            break
        else:
            print('该用户已存在，请重新输入')
# 主进程一分为二
    pid1 = os.fork()
    if pid1 < 0:
        print('创建一级子进程失败')
    elif pid1 == 0:
        do_child(s, name, ADDR)
    else:
        do_parent(s)

#如果作为主程序执行，则调用main()函数
if __name__ == "__main__":
    main()
