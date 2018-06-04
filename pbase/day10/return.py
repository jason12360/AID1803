def fun1():
	print('fun1被调用！')
	return 12
	print('这是fun1的最后一行')
f = fun1()
print(f) #None

def fun2():
	return 
	print('此行不会打印')

r = fun2
print('r=',r)

def fun3():
	
	return [1,2,3]

x,y,z = fun3()
print(x,y,z)