from multiprocessing import Process,Pipe
import os,time

#创建一个双向管道
#fd1,fd2 = Pipe()
#如果参数为False，则为单向管道，fd1只能recv,fd2只能send
fd1,fd2 = Pipe(False)
def fun(name):
	time.sleep(1)
	#发字符串到管道
	fd2.send('hello' + str(name))


	print(os.getppid(),'------',os.getpid())

jobs = []

for i in range(5):
	p = Process(target = fun,args = (i,))
	jobs.append(p)
	p.start()

接收子进程发送的消息
for i in range(5):
	data = fd1.recv()
	print(data)

for i in jobs:
	i.join()

