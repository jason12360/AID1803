# TCP 服务端
from socket import *
#    1.创建套接字socket
sockfd = socket(AF_INET, SOCK_STREAM, 0)
#    2.绑定IP和端口号bind
sockfd.bind(('0.0.0.0', 9998))
#    3.让套接字具有监听功能listen
sockfd.listen(5)
print('waiting for connect...')
#    4.等待客户带连接accept

connfd, addr = sockfd.accept()
print('connect from', addr)
#    5.消息的收发send recv
filename = input('请输入要传输的文件的地址:')
if '/' in filename:
    filename_ = filename.split('/')[-1]
else:
    filename_ = filename
    # print(filename_)
connfd.send(filename_.encode())
with open(filename, 'br') as file_obj:
    while True:
        buffer = file_obj.read(1024)
        if not buffer:
            break
        connfd.send(buffer)
        # print(buffer)

	#    6.关闭套接字close
connfd.close()
sockfd.close()
