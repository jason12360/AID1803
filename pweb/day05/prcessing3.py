import multiprocessing as mp
import os
import time

def th1():
	print(os.getppid(),'----',os.getpid())

	print('吃早饭')
	time.sleep(1)
	print('吃午饭')
	time.sleep(2)
	print('吃晚饭')
	time.sleep(3)

def th2():
	print(os.getppid(),'----',os.getpid())
	print('睡午觉')
	time.sleep(2)
	print('睡晚觉')
	time.sleep(3)

def th3():
	print(os.getppid(),'----',os.getpid())
	print('打豆豆')
	time.sleep(2)
	print('打豆豆')
	time.sleep(2)
things = [th1,th2,th3]
process = []

for th in things:
	p = mp.process(target=th)
	p.daemon = True
	process.append(p)
	p.start
# for p in process:
# 	p.join()


print('++++++++++++父进程+++++++++++++++')

th1()
th2()
th3()


