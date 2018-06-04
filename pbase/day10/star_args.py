def myfun(*args):
	print('实参个数是',len(args))
	print(args)

myfun(1,2)
myfun('100',200,'three hundreds',4.4)
myfun()