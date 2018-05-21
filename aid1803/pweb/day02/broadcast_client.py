from socket import *

HOST = ''
PORT = 9999
ADDR = (HOST,PORT)


#创建套接字
mysocket = socket(AF_INET,SOCK_DGRAM)
#设置套接字可以接收广播
mysocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#固定接收端的端口号
mysocket.bind(ADDR)
while True:
    try:
        message,addr = mysocket.recvfrom(4096)
        print('从{}获取信息: {}'.format(addr,message.decode()))
        mysocket.sendto(b'I am here',addr)
    except (KeyboardInterrupt,SyntaxError):
        raise
    except Exception as e:
        print(e)
mysocket.close()
