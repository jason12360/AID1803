# 3.用while语句实现打印n~1之间的偶数
n= int(input('请输入一个数n: '))
i = 1
while(i < n):
    if i % 2 == 0:
        print(i)
    i += 1
