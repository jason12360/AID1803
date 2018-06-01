#coding=utf-8
'''
功能：完成后端请求处理服务代码
说明：模拟web框架的基本原理
'''
import time
#设置静态文件文件夹
HTML_ROOT_DIR = './static'
#Python方法
PYTHON_DIR = './wsgiPy'

class Application:
	def __init__(self,urls):
		self.urls = urls
	def __call__(self,env,set_headers_function):
		path = env.get('PATH_INFO','/')
		#/static/index.html 获取静态文件
		if path.startswith('/static'):
			file_name = path[7:]
			try:
				with open(HTML_ROOT_DIR+file_name,'rb') as file_obj:
					file_data = file_obj.read()
					status = '200 OK'
					headers = [("Content_Type","text/plain")]
					set_headers_function(status,headers)
					return file_data.decode('utf-8')
			except:
				#没有找到静态网页
				status = '404 Not Found'
				headers = []
				set_headers_function(status,headers)
				return'<h1>====Sorry not found the page====<h1>'
		else:
			for url,headler in self.urls:
				if url == path:
					return headler(env,set_headers_function)
				#请求的url未找到
			status = '404 Not Found'
			headers = []
			set_headers_function(status,headers)
			return'<h1>====Sorry not found the url====<h1>'	
		#/time 表示用python方法处理请求

def show_time(env,set_headers_function):
	status = '200 OK'
	headers = [("Content_Type","text/plain")]
	set_headers_function(status,headers)
	return time.ctime()
def say_hello(env,set_headers_function):
	status = '200 OK'
	headers = [("Content_Type","text/plain")]
	set_headers_function(status,headers)
	return 'hello'
def say_bye(env,set_headers_function):
	status = '200 OK'
	headers = [("Content_Type","text/plain")]
	set_headers_function(status,headers)
	return 'goodbye'
urls = [
	('/time',show_time),
	('/hello',say_hello),
	('/bye',say_bye)
	]
app = Application(urls)