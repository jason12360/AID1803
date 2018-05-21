
from socket import *
from time import sleep,ctime
import traceback

sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(('0.0.0.0', 9999))
sockfd.listen(5)

print('waiting for connect...')
sockfd.settimeout(5)
while True:
    try:
        connfd, addr = sockfd.accept()
    except Exception:
        traceback.print_exc()
        continue
    print('connect from', addr)

    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        data_send = input('发消息')
        connfd.send(data_send.encode())
        print('服务器：', data_send)

    connfd.close()
sockfd.close()