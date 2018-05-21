# 输入一个Unicode的开始值 用变量begin绑定
# 输入一个。。。。。结束值，用变量stop绑定
# 打印开始值至结束值之间的所有对应文字
begin = int(input('请输入开始值： '))
stop = int(input('请输入结束值： '))
for i in range(begin,stop+1):
    print(chr(i),end = ' ')