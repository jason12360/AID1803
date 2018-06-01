class CallTest:
	def __call__(self,a,b):
		print('This is call test',a,b)

c = CallTest()
c(1,2)