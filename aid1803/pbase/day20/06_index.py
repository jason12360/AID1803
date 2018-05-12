class MyList:
	def __init__(self,iterable):
		self.data = [x for x in iterable]
	def __repr__(self):
		return 'MyList(%r)'% self.data
	def __neg__(self):
		print('__neg__方法被调用')
		L = [-x for x in self.data]
		return MyList(L)
	def __getitem__(self,index):
		print('__getitem__方法被调用')
		return self.data[index]
	def __setitem__(self,index,value):
		print('__setitem__方法被调用')
		self.data[index] = value
	def __delitem__(self,index):
		print('__defitem__方法被调用')
		del self.data[index]

L1 = MyList([1,-2,3,-4,5])
L1[2] = 100
del L1[2]
print(L1[2])
print(L1[::2])
