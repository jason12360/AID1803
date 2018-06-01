#coding=utf-8
'''
功能：完成httpserver
'''
from socket import *
import sys
import re
from threading import Thread
from WebFramework import app



#处理http请求
class HTTPServer:
	def __init__(self,app):
		self.my_socket = socket()
		self.my_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		self.app = app
	def bind(self,addr):
		self.my_socket.bind(addr)
		self.server_addr = addr
	def start(self):
		self.my_socket.listen(10)
		while True:
			self.my_connection,self.client_addr = self.my_socket.accept()
			print(self.client_addr,'用户连接')
			handle_thread = Thread(target = self.handle_client,args=(self.my_connection,))
			handle_thread.start()
	#处理请求头
	def set_headers(self,status,headers):
		'''
		在app调用该函数，希望得到
		status = '200 OK'
		headers = [("Content_Type","text/plain"),(),()]
		'''
		response_headers = 'HTTP/1.1 '+status+'\r\n'
		for header in headers:
			response_headers += '%s: %s\r\n'%header
		self.response_headers = response_headers


	#客户端处理函数
	def handle_client(self,my_connection):
		#接收浏览器request
		request_data = my_connection.recv(2048)
		request_lines = request_data.splitlines()
		request_line = request_lines[0].decode('utf-8')
		#找到request的方法
		request_match = re.match(r'(\w+)\s+(/\S*)',request_line)
		request_method,request_filename = request_match.group(1),request_match.group(2)
		#要传递的内容写入一个字典中，传递给应用程序
		env = {'METHOD':request_method,'PATH_INFO':request_filename}
		#编辑请求头
		response_body = self.app(env,self.set_headers)
		response = self.response_headers + '\r\n'+response_body
		my_connection.send(response.encode('utf-8'))
		my_connection.close()
#完成httpserver对象属性的添加和创建
def main():
	#选择一个要使用的网站的某个应用
	if len(sys.argv) < 2:
		sys.exit('''
			run the server as :
			python3 HttpServer.py FrameworkName:app
			''')
	framework_name,app_name= sys.argv[1].split(':')
	#动态导入
	sys.path.insert(1,'.')
	m = __import__(framework_name)
	app = getattr(m,app_name)
	HOST = '127.0.0.1'
	PORT = 8000
	ADDR = (HOST,PORT)
	http_server = HTTPServer(app)
	http_server.bind(ADDR)
	http_server.start()
	print('Listen on port',PORT)

if __name__=='__main__':
	main()


