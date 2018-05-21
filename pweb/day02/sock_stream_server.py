# TCP 服务端
from socket import *
#	1.创建套接字socket
sockfd = socket(AF_INET, SOCK_STREAM, 0)
#	2.绑定IP和端口号bind
sockfd.bind(('0.0.0.0', 9999))
#	3.让套接字具有监听功能listen
sockfd.listen(5)
print('waiting for connect...')
#	4.等待客户带连接accept
while True:
	connfd, addr = sockfd.accept()
	print('connect from', addr)
	#	5.消息的收发send recv
	while True:
		data = connfd.recv(1024)
		if not data:
			break
		print('接收的消息:',data.decode())
		data_send = input('发消息')
		connfd.send(data_send.encode())
		
	#	6.关闭套接字close
	connfd.close()
sockfd.close()
