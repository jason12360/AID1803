from multiprocessing import Process,Lock
import sys
from time import sleep

#sys.stdout为所有进程的共有资源
def worker1():
	with lock:
		for i in range(5):
			sleep(1)
			sys.stdout.write('worker1 输出\n')

def worker2():
	with lock:
		for i in range(5):
			sleep(1)
			sys.stdout.write('worker2 输出\n')

lock = Lock()

w1 = Process(target = worker1)
w2 = Process(target = worker2)

w1.start()
w2.start()

w1.join()
w2.join()