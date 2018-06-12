from socket import *
from view.login_view import Login_Page
#导入控制器模块用来处理IO相应
from view.login_handler import Login_handler
import sys
import fyc_version6

class Login_Client:
	def __init__(self):
		self.login_page = Login_Page()
		self.login_handler = Login_handler(self.login_page)
		self.login_page.register_handler(self.login_handler)
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
	# fyc_version6.main()

if __name__=='__main__':
	main()