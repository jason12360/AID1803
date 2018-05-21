import sys

def fun():
    print('进入函数')
    sys.exit() #直接退出到命令行（退出程序）
    print('退出函数')

fun()
print('程序结束')

#结果为：进入函数

