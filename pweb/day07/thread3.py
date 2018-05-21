#测试daemon属性
from threading import Thread
from time import sleep

def fun():
	print('Daemon 属性测试')
	sleep(5)
	print('线程结束')

t = Thread(target =fun )
print(t.isDaemon())
t.setDaemon(True)
t.start()
t.join(2)
print('=====主线程结束=======')

