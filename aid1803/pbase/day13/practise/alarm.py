# 1.编写一个闹钟，启动时设置定时时间（小时和分钟）：
#     到时间后打印‘时间到’，然后退出程序
import time
set_time = input('请输入您的预定时间(格式为19:30)：')
set_time_list = set_time.split(':')
set_time_list = tuple([int(x) for x in set_time_list])
while True:    
    current_time_tuple =time.localtime()
    current_time_list = current_time_tuple[3:5]
    print ('%02d:%02d'% current_time_list[0:2],end = '\r')
    if current_time_list == set_time_list:
        print('时间到')
        break