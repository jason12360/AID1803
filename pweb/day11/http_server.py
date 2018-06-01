try:
	from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
except ImportError:
	from http.server import BaseHTTPRequestHandler,HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print(self.headers)
		with open('test.html','rb') as fd:
			content = fd.read()
			#组织响应行
			self.send_response(200)
			#组织相应头
			self.send_header('Content-Type','text/html')
			#相应头结束
			self.end_headers()
			#发送相应体
			self.wfile.write(content)
			return
	def do_POST(self):
		pass
#指定地址
address = ('0.0.0.0',8000)
#生成服务器对象
server = HTTPServer(address,RequestHandler)
server.serve_forever()
