v = 100 #G
def fun1():
	v = 200 # E
	print('fun1.v',v)
	def fun2():
		v =300 # L
		print('fun2.v',v)
	fun2()

fun1()
print('v =',v)
