from socket import *
from select import *
import sys

mysocket = socket()
mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
mysocket.bind(('',9996))
mysocket.listen(10)
#创建IO事件地图
IOmap = {mysocket.fileno():mysocket}
#创建poll对象
mypoll = poll()
#将套接字加入到关注
mypoll.register(mysocket,(POLLIN | POLLERR))
while True:
	events = mypoll.poll()
	for n,event in events:
		if IOmap[n] is mysocket and event & POLLIN:
			socket1,addr = IOmap[n].accept()
			print('connect from',addr)
			IOmap[socket1.fileno()] = socket1
			mypoll.register(socket1,(POLLIN | POLLERR))
		if IOmap[n] is socket1 and event & POLLIN:
			data = IOmap[n].recv(2048)
			if not data:
				mypoll.unregister(n)
				del IOmap[n]		 
			print(data.decode())
			mypoll.register(socket1,POLLOUT)
		if IOmap[n] is socket1 and event & POLLOUT:
			IOmap[n].send('已接收您的信息'.encode())
			mypoll.unregister(n)
			



