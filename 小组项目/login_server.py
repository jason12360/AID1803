from socket import *
from model.database_handler import My_Mysql
import sys
from threading import Thread

class Login_Server:
	def __init__(self):
		self.mysocket = socket()
		self.mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		self.database_handler = My_Mysql()
	def bind(self,addr):
		self.mysocket.bind(addr)
	def start(self):
		self.mysocket.listen(5)
		while True:
			self.my_connection,self.client_addr = self.mysocket.accept()
			print(self.client_addr,'用户连接')
			handle_thread = Thread(target = self.handle_client,args=(self.my_connection,))
			handle_thread.start()

	def handle_client(self,conn):
		self.mysocket.close()
		while True:
			data = conn.recv(2048).decode().split('|')
			command = data[0]
			username = data[1]
			password = data[2]
			if data[0]=='L':
				self.do_login(username,password)
			elif data[0]=='R':
				self.do_register(username,password)
			elif data[0]=='Q':
				self.do_quit()

	def do_login(self,username,password):
		result = self.database_handler.select_user(username)
		if password == result[0][2]:
			self.my_connection.send(b'Y')
		else:
			self.my_connection.send(b'N')


	def do_register(self,username,password):
		result = self.database_handler.select_user(username)
		if not result:
			self.database_handler.add_user(username,password)
			self.my_connection.send(b'Y')
		else:
			self.my_connection.send(b'N')

	def do_quit(self):
		self.my_connection.close()
		sys.exit()



def main():
	if len(sys.argv)<3:
		sys.exit('args not right')
	HOST=sys.argv[1]
	PORT=int(sys.argv[2])
	ADDR=(HOST,PORT)
	login_server = Login_Server()
	login_server.bind(ADDR)
	login_server.start()

if __name__=='__main__':
	main()