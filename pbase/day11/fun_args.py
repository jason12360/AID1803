def goodbye(L):
	for x in L:
		print('再见:', x)
def hello(L):
	for x in L:
		print('你好:',x)
def operator(fn,L):
	fn(L)

operator(goodbye,['张三','李四'])
