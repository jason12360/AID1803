from socket import *
#TCP客户端
#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)
#发起连接
sockfd.connect(('127.0.0.1',9999))
#发送消息
while True:
	data_send = input('发消息')

	sockfd.send(data_send.encode())
	if not data_send:
		break
	print('客户端：',data_send)
	#接收消息
	data = sockfd.recv(1024)
	print(data.decode())
	
sockfd.close()
