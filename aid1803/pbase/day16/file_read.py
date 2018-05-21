#此程序示意文件打开时的错误处理

try:
    file = open('mynote.txt','br')
    print('打开文件成功')

    #通常在此进行读写文件内容
    s = file.readlines(20)
    print('第一行内容是：',s)

    #关闭文件
    file.close()
    print('文件已关闭')
except IOError:
    print('文件打开失败')