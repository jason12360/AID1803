n = int(input("请输入一个整数"))
if n > 0:
    if n % 2 == 1:
        print(n,'是一个大于0的奇数')
    else:
        print(n,'是一个大于0的偶数')
else:
    if n % 2 == 1:
        print(n,'是一个小于0的奇数')
    else:
        print(n,'是一个小于0的偶数')