import data_port
from threading import Thread
def run(data_socket,control_socket,addr):
	#把myconnection传给handler进行相关的登录操作

	#当用户成功登录后,如果需要上传下载,开辟新线程进行处理
	t = Thread(target=data_port.run,arg=(data_socket))