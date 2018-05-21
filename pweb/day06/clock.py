from multiprocessing import Process
import time

class ClockProcess(Process):
	def __init__(self,value):
		self.value = value
		super().__init__()
	#在自定义的进程类中重写父类的方法
	def run(self):
		n = 5
		while n>0:
			print('The time is {}'.format(time.ctime()))
			time.sleep(self.value)
			n -= 1

#用自己的进程类创建对象
p = ClockProcess(2)
#自动执行run方法
p.start()
p.join()


