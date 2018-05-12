#此程序示意以二进制方式打开文件后进行写操作

f = open('mydata.bin','wb')
print('打开文件成功')

s = '我是汉字'
r = f.write(s.encode('utf-8'))

f.close()