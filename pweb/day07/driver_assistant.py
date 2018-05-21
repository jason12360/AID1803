# 作业：
# 	信号通信
# 	司机和售票员
# 	1.创建父子进程，分别表示司机和售票员
# 	2.当售票员捕捉到SIGINT信号时，给司机发送SIGUSR1信号，此时司机打印'老司机开车了'
# 	3.当售票员捕捉到SIGQUIT时，给司机发送SIGUSR2信号，此时司机打印'寄好安全带，车速有点快'
# 	4.当司机捕捉到SIGSTP时，发送SIGUSR1 给售票员，售票员打印"到站了，请下车"
# 	5.到站后，售票员先下车，然后司机下车

# 	温馨提示：键盘发送信号时，信号会发送给终端的每一个进程

from multiprocessing import Process,Event
import signal
import os
from time import sleep


def assistant():
	signal.signal(signal.SIGINT,action_assistant)
	signal.signal(signal.SIGQUIT,action_assistant)
	signal.signal(signal.SIGUSR1,action_assistant)
	signal.signal(signal.SIGTSTP,signal.SIG_IGN)
	while True:
		sleep(2)
		print('呜呜呜')
def driver():
	signal.signal(signal.SIGINT,signal.SIG_IGN)
	signal.signal(signal.SIGQUIT,signal.SIG_IGN)
	signal.signal(signal.SIGUSR1,action_driver)
	signal.signal(signal.SIGUSR2,action_driver)
	signal.signal(signal.SIGTSTP,action_driver)
	signal.signal(signal.SIGCHLD,action_driver)


	while True:
		sleep(2)
		print('呜呜呜')
def action_assistant(sig,frame):
	if sig == signal.SIGINT:
		os.kill(os.getppid(),signal.SIGUSR1)
	elif sig == signal.SIGQUIT:
		os.kill(os.getppid(),signal.SIGUSR2)
	elif sig == signal.SIGUSR1:
		print('售票员：到站了，请下车')
		print('售票员下车了！')
		os._exit(1)


def action_driver(sig,frame):
	if sig == signal.SIGTSTP:
		os.kill(p.pid,signal.SIGUSR1)
	elif sig == signal.SIGUSR2:
		print('司机：系好安全带，车速有点快')
	elif sig == signal.SIGUSR1:
		print('司机：老司机开车了')
	elif sig == signal.SIGCHLD:
		print('司机下车了')
		os._exit(1)



p = Process(target = assistant)
p.start()

driver()
p.join()
