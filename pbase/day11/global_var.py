v =  100  #<<--此为全局变量
def fn():
	v = 1 #<<--此为局部变量
	print(v)

fn()
print(v)