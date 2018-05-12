#此程序示意标准输出sys.stdout和标准错误输出sys.stderr
import sys #导入sys模块
sys.stdout.write('hello world\n')
sys.stderr.write('我的出现是个错误！\n')

# #以下程序会出错
# sys.stdout.close()
# print('程序结束')