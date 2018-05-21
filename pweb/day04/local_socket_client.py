from socket import *
import sys

#确定用哪个文件进行通信
SERVER_ADDRESS = './test'
#创建本地套接字
try:
	my_local_socket = socket(AF_UNIX,SOCK_STREAM)
#连接本地套接字文件
	my_local_socket.connect(SERVER_ADDRESS)
except error as e:
	print(e)
	sys.exit(1)
while True:
	data = input('发消息>>')
	if data:
		my_local_socket.send(data.encode())
		print(my_local_socket.recv(1024).decode())
	else:
		my_local_socket.send(''.encode())
		break
my_local_socket.close()
