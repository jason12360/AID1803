from socket import *
from select import *
import sys

mysocket = socket()
mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
mysocket.bind(('',9996))
mysocket.listen(10)
#将关注的IO放入rlist
rlist = [mysocket]
wlist = []
xlist = [mysocket]
while True:
	rs,ws,ss = select(rlist,wlist,xlist)
	for r in rs:
		if r is mysocket:
			connfd,addr = r.accept()
			print('Connect from',addr)
			#将新的套接字加入到关注列表
			rlist.append(connfd)
		elif r is connfd:
			data = r.recv(1024)
			if not data:
				rlist.remove(r)
				r.close()
			else:
				print('Received from:',r.getpeername(),':',data.decode())
				wlist.append(r)
	for w in ws:
		w.send('收到您的消息'.encode())
		wlist.remove(w)
	for s in ss:
		if s is mysocket:
			s.close()
			sys.close()

