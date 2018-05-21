# 3.用while循环生成一个字符串：
#     1.生成'ABCDEFG...XYZ'并打印
#     2.生成'AaBbCcDdEeFf...XxYyZz'并打印
#     提示：chr和ord函数

a = ord('a')
A = ord('A')
i = 0
s1 = ''
s2 = ''
while i <= 25:
    s1 += chr(a + i)
    s2 += chr(A + i) + chr(a + i)
    i += 1
print(s1)
print(s2)
