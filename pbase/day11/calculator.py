# 写一个函数，此函数传一个参数(op):
# 		def get_op(op):
# 		   ...
# 	此函数在传入字符串'加'，返回+操作的函数myadd(x,y)，return x+y
# 	此函数在传入字符串'乘'，返回+操作的函数myadd(x,y)，return x*y
# 	在主函数中程序如下：
# 	a =int(input('请输入第一个数：'))
# 	b =int(input('请输入第二个数：'))
# 	operator = input('请输入操作方式')
# 	fn = get_op(operator)
# 	print('结果是',fn(a+b))

def get_op(op):
	def myadd(x,y):
		return x + y
	def mymul(x,y):
		return x * y

	if op == '加':
		return myadd
	elif op == '乘':
		return mymul
a =int(input('请输入第一个数：'))
b =int(input('请输入第二个数：'))
operator = input('请输入操作方式：')
fn = get_op(operator)
print('结果是',fn(a,b))
