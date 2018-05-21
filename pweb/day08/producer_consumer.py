from threading import Thread
#python标准库队列
import queue
from time import sleep

#创建一个队列作为仓库
q = queue.Queue()
#生产者
class Producer(Thread):
	def run(self):
		count = 0
		while True:
			if q.qsize() < 50:
				for i in range(3):
					count += 1
					msg = '产品%d'%count
					q.put(msg)
			sleep(1)
#消费者
class Consumer(Thread):
	def run(self):
	 	while True:
	 		if q.qsize() > 20:
	 			for i in range(2):
	 				product = q.get()
	 				print('消费了%s'%product,'还有%d'%q.qsize())
	 		sleep(1)
#创建两个生产者
for i in range(2):
	p = Producer()
	p.start()

#创建三个消费者
for i in range(3): 
	c= Consumer()
	c.start()
