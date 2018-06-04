def myfun(**kwargs):
	print('参数个数：',len(kwargs))
	for k,v in kwargs.items():
		print(k,'->>',v)
	
myfun(name = 'tarena',age = 15)
myfun(a = 1,b ='bbb',c=[1,2,3],d = True)