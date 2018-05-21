 # 写一个程序，输入你的生日
 #    1.计算出你出生那天是星期几？
 #    2.计算出你已经出生多少天
import time

birthday = input('请输入您的生日，格式如1990-09-10：')
birthday_list = birthday.split('-')
birthday_seconds = time.mktime((int(birthday_list[0]),int(birthday_list[1]),int(birthday_list[2]),0,0,0,0,0,0))
birthday_tuple = time.localtime(birthday_seconds)
date_reference = {0:"星期一",
                  1:"星期二",
                  2:"星期三",
                  3:"星期四",
                  4:"星期五",
                  5:"星期六",
                  6:"星期天"}
print('您出生在',date_reference[birthday_tuple[6]])


recent_seconds = time.time()
living_days = (int(recent_seconds - birthday_seconds))//(3600*24) 
print('您已经出生了',living_days,'天')
