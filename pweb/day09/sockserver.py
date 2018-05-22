#多进程tcp并发
from socketserver import *

class Server(ForkingMixIn,TCPServer):
	pass

class Handler(StreamRequestHandler):
	def handle(self):
		#self.request  = accept创建的新的套接字
		connection = self.request
		print('Connect from',connection.getpeername())
		while True:
			data = connection.recv(1024).decode()
			if not data:
				break
			connection.send(b'receive your message')


server = Server(('127.0.0.1',9999),Handler)
server.serve_forever()