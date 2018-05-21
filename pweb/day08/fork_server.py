from socket import *
import os,sys
import signal

def client_handler(s):
	try:
		print('子进程接收客户端请求',s.getpeername())
		while True:
			data = s.recv(1024).decode()
			if not data:
				break
			print(data)
			s.send('收到你的消息'.encode())
	except (KeyboardInterrupt,SystemExit):
		raise
	except Exception as e:
		print(e)
	s.close()
	os._exit(0)



while len(sys.argv) < 3:
	print('args not valid')
HOST  = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

mysocket = socket()
mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
mysocket.bind(ADDR)
mysocket.listen(10)
print('父进程%d等待客户端的连接'%os.getpid())
while True:
	try:
		c,addr = mysocket.accept()
	except KeyboardInterrupt:
		raise
	except Exception as e:
		print(e)
		continue
	#为新的客户端创建新的进程
	
	#确保不会出现僵尸进程
	signal.signal(signal.SIGCHLD,signal.SIG_IGN)

	childpid = os.fork()

	if childpid ==0:
		#保证原来的用来接收客户端的套接字关闭，以防误操作
		mysocket.close()
		#处理客户端请求
		client_handler(c)
	elif childpid > 0:
		#保证创建的连接关闭，以防误操作
		c.close()
		continue
	else:
		print('创建子进程失败')
		c.close()
		continue