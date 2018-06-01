import gevent
from gevent import monkey
#在导入socket前执行改变socket的阻塞形态
monkey.patch_all()
from socket import *
from time import ctime

def server(port):
	s = socket()
	s.bind(('0.0.0.0',port))
	s.listen(5)
	while True:
		c,addr = s.accept()
		print('Connect from',addr)
		gevent.spawn(handler,c)

def handler(c):
	while True:
		data = c.recv(1024)
		print('sadsadas')
		if not data:
			break
		print('recv:',data.decode())
		c.send(ctime().encode())
	c.close()

if __name__ == '__main__':
	server(9999)