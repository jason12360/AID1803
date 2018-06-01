import gevent

def foo(a):
	print('Running in foo',a)
	gevent.sleep(2)
	print('switch to foo again')

def bar():
	print('Running in bar')
	gevent.sleep(3)
	print('switch to bar again')

f = gevent.spawn(foo,1)
b = gevent.spawn(bar)

gevent.joinall([f,b])


