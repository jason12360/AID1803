import threading
from time import sleep

s = None

#创建线程事件对象
e = threading.Event()

def bar():
	print(threading.currentThread().name,'呼叫foo')
	global s
	s = '天王盖地虎'
	print(threading.currentThread().name,'发出呼叫',s)
	
def foo():
	print(threading.currentThread().name,'等待口令')
	sleep(2)
	print(threading.currentThread().name,'收到呼叫',s)
	if s == '天王盖地虎':
		print('foo收到:',s)
	else:
		print('打死他')
	e.set()

#fun会在中途篡改口令,需要加入event进行控制
def fun():
	sleep(1)
	print(threading.currentThread().name,'呵呵...')
	e.wait()
	global s
	s = '小鸡炖蘑菇'
	print(threading.currentThread().name,'修改呼叫',s)

t1 = threading.Thread(name = 'bar',target = bar)
t2 = threading.Thread(name = 'foo',target = foo)
t3 = threading.Thread(name = 'fun',target = fun)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()


