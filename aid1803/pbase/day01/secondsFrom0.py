# 2.分三次输入当前的小时，分钟，秒数，在终端打印此时间距离0:0：0过了多少秒

hours = int(input('请输入小时数: '))
minutes = int(input('请输入分钟数: '))
seconds = int(input('请输入秒数: '))

print('此时间距离0:0：0过了',3600*hours + 60*minutes +seconds,'秒')