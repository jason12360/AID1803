#本示例示意with语句的使用方法

#打开文件读取文件数据

#以前

# try:
# 	f = open('abcd.txt')
# 	try:
# 		while True:
# 			s = f.readline()
# 			if not s:
# 				break
# 			int(input('请输入任意数字打印下一行：'))
# 			print(s[:-1])
# 	finally:
# 		print('文件已经关闭')
# 		f.close()
# except IOError:
# 	print('出现异常已经捕获')
# except ValueError:
# 	print('程序已转为正常状态')

# print('程序结束')

#with语句来实现

try:
	with open('abcd.txt') as f:
		s_list = f.readlines()
		for s in s_list:
			int(input('请输入任意数字打印下一行：'))
			print(s)
except IOError:
	print('出现异常已经捕获')
except ValueError:
	print('程序已转为正常状态')

print('程序结束')



