#线程对象属性
from threading import Thread,current_thread
from time import sleep

def fun(sec):
	print('线程属性测试')
	sleep(sec)
	# print('线程结束')
	print("%s 线程结束"%current_thread().getName())

tlist = []
for i in range(3):
	t = Thread(name = 'tedu'+str(i),target = fun,args = (3,))
	t.start()
	tlist.append(t)


for i in tlist:
	print('thread name:',i.name)
	print('alive:',i.is_alive())
	i.join()