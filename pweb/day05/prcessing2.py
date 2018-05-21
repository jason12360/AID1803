from multiprocessing import *
from time import sleep

def worker(sec,msg):
	for i in range(3):
		sleep(sec)
		print('worker message:',msg)
#位置传参
# p = Process(target = worker,args = (2,'hello'))
#字典传参
p = Process(name = 'worker',target = worker,kwargs = {'sec':2,'msg':'hello'})
#也可以混合传参
p.start()

print('p.name:',p.name)
#p所代表的子进程的pid号
print('p.pid:',p.pid)
print('p.alive:',p.is_alive())
p.join()
