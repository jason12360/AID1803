import threading
from time import sleep

def music():
	while True:
		sleep(2)
		print('播放葫芦娃')

#创建线程和函数
t = threading.Thread(target = music)

#启动线程
t.start()

while True:
	sleep(1.5)
	print('想听灌篮高手')
#等待回收线程
t.join()

print('+++++++++++++++')