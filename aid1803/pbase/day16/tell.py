#此示例示意tell方法的用法

f = open('alpha_number.bin','rb')
print('刚打开的文件流位置为：',f.tell())
b = f.read(5)
print('读出五个字节后的文件流位置为：',f.tell())
f.close()