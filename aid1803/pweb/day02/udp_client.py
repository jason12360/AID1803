import sys
from socket import * 

if len(sys.argv) < 3:
    print('argv is not correct')
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    BUFFERSIZE = 1024

#创建数据报套接字   
sockfd = socket(AF_INET,SOCK_DGRAM,0)
while True:
    data_input = input('消息>>')
    if not data_input:
        break
    print(sockfd.getsockname())
    sockfd.sendto(data_input.encode(),ADDR)
    print(sockfd.getsockname())
    data,addr = sockfd.recvfrom(BUFFERSIZE)
    print('从服务器',addr,'接收到：',data.decode())
sockfd.close()
