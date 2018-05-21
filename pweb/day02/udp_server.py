# 服务端
#     1.创建数据报套接字
#         sockfd = socket(AF_INET,SOCK_DGRAM,0)
#     2.绑定服务端地址
#         ADDR = ('192.168.1.2',8888)
#         sockfd.bind(ADDR)
#     3.收发消息
#         data,addr = recvfrom(buffersize)
#             功能：接收数据报套接字消息
#             参数：每次最多接收消息的大小 字节
#             返回值： data:接收data的消息
#                     addr:消息发送者的地址
#         sendto(data,addr)
#             功能:发送消息
#             参数：data 要发送的消息
#                  addr 发送给某个主机的地址
#             返回值：发送信息的字节数
#     4.关闭套接字
#         close()
import sys
from socket import * 
from time import ctime

if len(sys.argv) < 3:
    print('argv is not correct')
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    BUFFERSIZE = 1024

#创建数据报套接字   
sockfd = socket(AF_INET,SOCK_DGRAM,0)
#绑定地址 
sockfd.bind(ADDR)
print('服务起启动成功，正在接收数据！')
#收发消息
while True:
    data,addr = sockfd.recvfrom(BUFFERSIZE)
    print('recv from %s: %s'%(addr,data.decode()))
    
    sockfd.sendto(("[%s]接收到消息"%ctime()).encode(),addr)

sockfd.close()



