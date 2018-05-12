#请输入一个整数判断这个数字是正数还是负数还是0
n = int(input('请输入一个整数'))
if n > 0:
    print(n,'这个数字是正数')
elif n < 0:
    print(n,'这个数字是负数')
else:
    print(n,'这个数字是0')