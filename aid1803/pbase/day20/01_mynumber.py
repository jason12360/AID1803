class MyNumber:
	def __init__(self,v):
		self.__data = v
	def __repr__(self):
		return 'MyNumber(%d)'%self.__data
	def __add__(self,other):
		return MyNumber(self.__data + other.__data)
	def __sub__(self,other):
		return MyNumber(self.__data - other.__data)

n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1 + n2
n4 = n3 - n1
print(n4)