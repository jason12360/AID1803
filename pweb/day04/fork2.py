import os
from time import sleep

pid = os.fork()

if pid < 0:
	print('创建进程失败')
elif pid == 0:
	# #父进程已经退出，打印的将是新进程的PID
	# sleep(1)
	# print('我爸是',os.getppid())
	print('我是儿子，我的ID是',os.getpid())
else:
	sleep(1)
	while True:
		pass
