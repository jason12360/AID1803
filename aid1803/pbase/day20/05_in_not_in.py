# 此示例示意in/ not in 运算符的重载

class MyList:
	def __init__(self,iterable):
		self.data = [x for x in iterable]
	def __repr__(self):
		return 'MyList(%r)'% self.data
	def __contains__(self,e):
		return e in self.data



L1 = MyList([1,-2,3,-4,5])
if 2 in L1:
	print('2在L1中')
else:
	print('2不在L1中')

