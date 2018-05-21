import os,sys
from time import sleep

pid = os.fork()

if pid < 0:
	print('创建进程失败')
elif pid == 0:
	sleep(2)
	print('我爸是',os.getppid())
	print('我是儿子，我的ID是',os.getpid())
	sys.exit(3)
else:
	p,status = os.wait()
	print(p,status)
	print(os.WEXITSTATUS(status))
	while True:
		pass