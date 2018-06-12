#分配两个进程,分别处理聊天与主要功能
#第一个进程将使用tcp首先接收客户端连接请求,为客户端分配单独进程处理相应请求
#第二个进程将使用udp进行聊天通信
from socket import *
from signal import *
from multiprocessing import Process
import client_control_port
import chat_port

def client_control_port(control_socket,addr):
	client_control_port.run(data_socket,control_socket,addr)



def control_port():
	#建立登录和主要功能连接,端口号为xxx
	HOST=''
	PORT=18527
	ADDR=(HOST,PORT)
	control_socket = socket()
	control_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	control_socket.connect(ADDR)
	#TODO:创建UDP套接字
	data_socket = socket(...)
	#为不同的client分配不同的进程
	process = Process(target=client_control_port.run,args=(data_socket,control_socket,addr))
	#
#当用户成功登录后,分配进程用来处理聊天,聊天将为群聊,故使用udp协议	


def main()
	#设置父进程信号处理僵尸进程
	#TODO

	t1 = Process(target=control_port)
	t2 = Process(target=chat_port)
	t1.start()
	t2.start()



