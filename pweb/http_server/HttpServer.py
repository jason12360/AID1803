'''
完成httpserver的并发
并发使用多线程完成
用不同的后端程序，处理不同的请求
可以简单的显示静态页面
启动服务器终端输入 python3 HttpServer .py module app
'''

#导入需要的模块——————————————————————————————————————————————————————————————————————————
import sys
from socket import *
from threading import Thread
#——————————————————————————————————————————————————————————————————————————————————————

#全局变量————————————————————————————————————————————————————————————————————————————————
ADDR = ('',8000)
#存静态网页的目录
STATIC_ROOT = './static'
#存放Python处理模块的目录
HANDLER_ROOT = './handler'
#———————————————————————————————————————————————————————————————————————————————————————

#定义一个服务器类用于封装服务器段的操作方法————————————————————————————————————————————————————
class HttpServer(object):
	def __init__(self,server_addr):
		'''
		在实例化时创建套接字，并保留相关属性，以便调用
		'''
		self.__mysocket = socket()
		self.__mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		self.__mysocket.bind(server_addr)
		self.__mysocket.listen(5)
		self.__server_name = server_addr[0]
		self.__server_port = server_addr[1]

	def set_application(self,application):
		self.__application = application
	
	def serve_forever(self): 
		'''
		等待客户端的连接，没有一个连接，创建一个新的线程进行处理
		'''
		while True:
			self.__my_connection,self.__client_addr = self.__mysocket.accept()
			client_thread = Thread(target = self.__request_handler)
			client_thread.start()	

	def __request_handler(self):
		#接收request请求
		request = self.__my_connection.recv(2048)
		#获取请求头
		request_list = request.splitlines()
		#获取请求的应用
		req_app = request_list[0].decode().split(' ')[1]
		#当请求文件为html或其他静态文件时
		if req_app[-3:] != '.py':
			if req_app == '/':
				file_name = STATIC_ROOT + '/index.html'
			else:
				file_name = STATIC_ROOT + req_app
			try:
				with open(file_name,'r') as file_obj:
					response = 'HTTP/1.1 200 OK\r\n'
					response +='\r\n'
					for i in file_obj:
						response += i
			#当没有找到相应请求的文件时
			except IOError:
				response = 'HTTP/1.1 404 not found\r\n'
				response +='\r\n'
				response +='====sorry,file not found'
			finally:
				self.__my_connection.send(response.encode())
				self.__my_connection.close()
		else:
			#env代表需要的环境变量
			env = {}
			body_content = self.__application(env,self.__start_response)
			response = 'HTTP/1.1 {}\r\n'.format(self.__header_set[0])
			for header in self.__header_set[1:]:
				response += '{0}:{1}\r\n'.format(*header)
			response += '\r\n'
			response += body_content
			self.__my_connection.send(response.encode())
			self.__my_connection.close()

#提供一个包装方法供下层调用，从而生成header属性
	def __start_response(self,status,response_headers):
		server_headers = [
						('Data','2018-5-21'),
						('Server','HTTPServer 1.0')
		]
		self.__header_set = [status,response_headers + server_headers]

#———————————————————————————————————————————————————————————————————————————————————————

#服务器动主函数————————————————————————————————————————————————————————————————————————————
def main():
	#启动时直接告知使用那个模块那个函数来处理请求
	#python3 HttpServer.py module_name application_name
	if len(sys.argv) < 3:
		sys.exit('请选择一个模块和应用')
	module_name = sys.argv[1]
	application_name = sys.argv[2]
	#将处理模块目录加入到系统路径
	sys.path.insert(0,HANDLER_ROOT)
	#动态导入相应的模块
	my_module = __import__(module_name)
	#动态获取相应模块下的相应属性
	my_application = getattr(my_module,application_name)
	#创建服务器实例处理相应请求
	http_server = HttpServer(ADDR)
	print('Serving Http on port 8000')
	#将获取的相应属性传给服务器实例
	http_server.set_application(my_application)
	#运行服务器实例
	http_server.serve_forever()
#—————————————————————————————————————————————————————————————————————————————————————————

if __name__ =='__main__':
	main()
