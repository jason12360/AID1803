from socket import *
from select import *
import sys
import os

mysocket = socket()
mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
mysocket.bind(('',9996))
mysocket.listen(10)
#将关注的IO放入rlist
while True:
	connection1,addr = mysocket.accept()
	child_pid = os.fork()
	if child_pid == 0:
		while True:
			data = connection1.recv(1024)
			if not data:
				os._exit(0)
			print(data.decode())


	