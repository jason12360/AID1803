from threading import Thread
from time import ctime,sleep

#编写自己的线程类
class MyThread(Thread):
	def __init__(self,func,args,name = 'Tedu'):
		super().__init__()
		self.func = func
		self.args = args
		self.name = name
		
	#调用start会自动用型
	def run(self):
		self.func(*self.args)

def player(music,times):
	for i in range(times):
		sleep(1)
		print('正在听',music,ctime())

my_thread = MyThread(func = player,args = ('baby.mp3',3))
my_thread.start()
my_thread.join()
