from socket import *
from select import *
import sys

mysocket = socket()

usernames = {}


mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
mysocket.bind(('',9996))
mysocket.listen(10)
while True:
	rlist = [mysocket]
	wlist = []
	xlist = [mysocket]
	while True:
		rs,ws,ss = select(rlist,wlist,xlist)
		for r in rs:
			if r is mysocket:
				connfd,addr = r.accept()
				username = connfd.recv(1024).decode()
				for socket in usernames:
					message = username + '上线'
					socket.send(message.encode())
				usernames[connfd] = username
				#将新的套接字加入到关注列表
				rlist.append(connfd)
			elif r in usernames:
				data = r.recv(1024)
				if not data:
					username = usernames[r]
					usernames.pop(r)
					for socket in usernames:
						message = username + '下线'
						socket.send(message.encode())
					rlist.remove(r)
					r.close()
				else:
					for socket in usernames:
						socket.send(data)
		for s in ss:
			if s is mysocket:
				s.close()
				sys.close()
			



