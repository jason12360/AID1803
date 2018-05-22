import socket
from threading import *
import os,sys

HOST='127.0.0.1'
PORT = 9999
#处理具体的客户端请求
def socket_handler(conn):
	print('Got connection from',conn.getpeername())
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		conn.send(b'receive your message')
	conn.close()

#创建套接字
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(5)

#主线程循环接受客户端连接
while True:
	try:
		c,addr = s.accept()
	except KeyboardInterrupt:
		raise()
	except Exception as e:
		print(e)
		continue
	t = Thread(target = socket_handler,args = (c,))
	t.setDaemon(True)
	t.start()


