# 此示例示意以二进制模式读取mynote.py文件
    
try:
    f = open('mynote.txt','rb')
    print('打开文件成功')
    b = f.read()
    print(b)
    s = b.decode('utf-8')
    print(s)
except IOError:
    print('打开文件失败')