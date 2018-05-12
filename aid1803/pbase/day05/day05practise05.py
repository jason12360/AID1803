# 练习：写一个程序，输入数字，用while循环来判断此数字是否为素数

# n = int(input('请输入一个数字'))
# i = 2
# while i < n:
#     if n % i == 0:
#         print(n,'不是素数')
#         break
#     i += 1
# else:
#     print(n,'是素数')

l = []
for n in range(2,101):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1
    else:
        l.append(n)
print(l)