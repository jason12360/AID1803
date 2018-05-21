# 3.给一个年份，判断是否是闰年并打印
#         每四年一闰，每百年不闰，每四百年又闰

year = int(input('请输入一个年份'))
run = False
if year % 4 == 0 and year % 100 != 0:
    run = True
if year % 400 == 0:
    run = True
if run:
    print(year,'是一个闰年')
else:
    print(year,'不是一个闰年')