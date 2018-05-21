from socket import *
import sys,os
from select import *
'''
本项目采取tcp协议完成聊天室的功能，在客户端采取状态机来实现
state 0 ：用户注册
state 1 : 用户收发消息
state 2 : 结束收发消息
项目使用多路复用方select方式来监听IO事件，从而完成边接收，边发送。
'''

main():
	#初始化套接字，使用tcp协议
	sockfd = socket(AF_INET,SOCK_STREAM)
	sockfd.connect(('',9996))
	#初始化状态机参数为0，用户名为‘’，监听列表
	state = 0
	username = ''
	rlist = [sockfd,sys.stdin]
	wlist = []
	xlist = [sockfd,sys.stdin]
	#开启状态机
	while True:
		#如果为0状态，则运行用户注册，用户成功注册则进出1状态，
		if state == 0:
			username = input('用户名：')
			if username:
				sockfd.send(username.encode())
				state = 1
			continue
		if state ==1:
			rs,ws,ss = select(rlist,wlist,xlist)
			for r in rs:
				if r is sockfd:
					data = r.recv(1024)
					print(data.decode())
				else:
					data_send = r.readline()[:-1]
					if not data_send:
						sockfd.send(b'')
						rlist.remove(sockfd)
						state = 2
					else:
						data =  username +":" + data_send
						sockfd.send(data.encode())
			continue
		if state ==2:
			sockfd.close()
			break


if __name__ = '__main__':
	main()


	#接收消息
	# data = sockfd.recv(1024)
	# print(data.decode())

