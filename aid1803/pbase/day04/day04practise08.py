# 2.写程序，输入一个正整数，判断之个数是否为质数 
# n = int(input('请输入一个正整数'))
# zhishu = True
# for i in range(2,n+1):
#     if n % i == 0 and i != n:
#         zhishu = False
#         break
# if zhishu:
#     print('这是一个质数')
# else:
#     print('这不是一个质数')

# 其他方法：
n = int(input('请输入一个正整数'))
for i in range(2,n):
    if n % i == 0:
        print('这不是一个质数')
        break
else:
    print('这是一个质数')