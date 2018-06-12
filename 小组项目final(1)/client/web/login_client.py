from socket import *
from view.login_view import Login_Page
import sys

class Login_Client:
	def __init__(self):
		self.login_page = Login_Page()
		self.login_handler = self.login_page.get_login_handler()
		self.mysocket = socket()
		self.mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	def connect(self,addr):
		self.mysocket.connect(addr)
		self.login_handler.bind_connection(self.mysocket)
	def start(self):
		self.login_page.run()

def main():
	if len(sys.argv)<3:
		sys.exit('args not right')
	HOST=sys.argv[1]
	PORT=int(sys.argv[2])
	ADDR=(HOST,PORT)
	login_client = Login_Client()
	login_client.connect(ADDR)
	login_client.start()

if __name__=='__main__':
	main()