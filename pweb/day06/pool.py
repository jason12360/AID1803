from multiprocessing import Pool
from time import sleep
import os

def worker(msg):
	sleep(2)
	print(msg)
	return msg + 'over'
result= []
#创建进程池
my_process_poll = Pool(processes = 4)
#放入事件
for i in range(10):
	msg = 'hello %d'%i
	#加入事件后进程就会立即操作事件运行
	#apply_async的方绘制对象，该对象可以获取work返回结果
	r = my_process_poll.apply_async(func = worker,args = (msg,))
	result.append(r)
sleep(2.1)
print('++++++++++++++++++++++++++')
#关闭进程池
sleep(2.1)
my_process_poll.close()
print('**************************')
#主进程阻塞等待进程退出
my_process_poll.join()
print('==========================')

for r in result:
	print(r.get())