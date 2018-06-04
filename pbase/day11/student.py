
# 练习：
# 	写一个函数，在函数内部读取学生姓名，并存入列表中，通过两种方式返回学生姓名数据，并打印出来
# 	方式1，通过返回值返回数据
# 	方式2，通过参数返回数据

# def get_names(x = []):
# 	L = []
# 	while True:
# 		name = input('请输入姓名：')
# 		if not name:
# 			break
# 		L.append(name)
# 	x[:] = L
# 	return L

# n = get_names()
# print(n)

n = []
get_names(n)
print(n)

def get_names(L = []):
	while True:
		name = input('请输入姓名：')
		if not name:
			break
		L.append(name)
	return L