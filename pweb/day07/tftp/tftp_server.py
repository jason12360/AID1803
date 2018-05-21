# TFTP文件服务器
# 设计思路
# 文件的上传，下载，和服务端文件库的查看

from socket import *
from multiprocessing import Process,current_process
import sys,os
import signal

def upload_file(socket,_dir):
	print('收到客户端的上传请求')
	#先接收文件名称
	#把文件名称存在数据结构中以便调用
	#接收文件内容
def download_file(socket,_dir):
	print('收到客户端的下载请求')
def list_file(socket,_dir):
	print('收到客户端的查看请求')
	#遍历dir
	file_list = os.listdir(_dir)
	#组成字符串，发送给客户端
	file_string = ''
	for file in file_list:
		file_string += '  ' + file
	socket.send(file_string.encode())

#写一个进程处理的函数
def request_handler(socket,_dir):
	print('我是一个子进程，我的名字叫',current_process().name)
	while True:
		command = socket.recv(1024).decode()
		if command =='U':
			upload_file(socket,_dir)
		elif command =='D':
			download_file(socket,_dir)
		elif command =='L':
			list_file(socket,_dir)
		elif command =='Q':
			break
	sys.exit(1)


def main():
#创建TCP套接字，设定端口，开始监听

	if len(sys.argv) < 3:
	    print('argv is error')
	    return
	HOST = sys.argv[1]
	PORT = int(sys.argv[2])
	ADDR = (HOST, PORT)
	#确定文件所保存的目录
	DIR = './files'
	s = socket(AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind(ADDR)
	s.listen(10)

	signal.signal(signal.SIGCHLD,signal.SIG_IGN)
	#每监听一个就创建一个进程对请求进行处理
	
	while True:
		connfd,addr = s.accept()
		p = Process(name = addr,target = request_handler,args = (connfd,DIR))
		p.start()
		


if __name__ =='__main__':
	main()


