from socket import *
import sys,os

#确定用哪个文件进行通信
SERVER_ADDRESS = './test'

#判断文件存在性，如果存在需要处理
if os.path.exists(SERVER_ADDRESS):
	os.unlink(SERVER_ADDRESS)
#创建本地套接字
my_local_socket = socket(AF_UNIX,SOCK_STREAM)
#绑定本地套接字文件
my_local_socket.bind(SERVER_ADDRESS)
#监听
my_local_socket.listen(5)

while True:
	local_connection,address = my_local_socket.accept()
	while True:
		data = local_connection.recv(1024)
		print(data.decode())
		if data:
			local_connection.sendall('收到消息'.encode())
		else:
			break
	local_connection.close()
my_local_socket.close()