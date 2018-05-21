from multiprocessing import Process,Semaphore,current_process
from time import sleep
#创建信号量初始值为3
sem = Semaphore(3)
def fun():
	print('进程 %s 等待信号量'%current_process())
	#第四个进程无信号资源被阻塞
	sem.acquire()
	print('进程 %s 消耗信号量'%current_process())
	sleep(3)
	print('进程 %s 添加信号量'%current_process())
	sem.release()
plist = []
for i in range(4):
	p = Process(target = fun)
	p.start()
	plist.append(p)

for i in plist:
	i.join() 
