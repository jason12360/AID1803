import os

pid = os.fork()

if pid < 0:
	print('创建进程失败')
elif pid ==0:
	print('创建了一个新的进程')
else:
	print('这是原有的进程')

print('进程执行完毕')