# 练习：
#     输入两个整数，分别用x和y来绑定
#     100
#     200
#     1)计算这两个数字的和，并打印为（100+200=300）
#     2）计算这两个数字的乘积，并打印为（100*200=20000）
#     3）计算x的y次方并打印

x = input('请给x赋值: ')
y = input('请给y赋值: ')
if x.isdigit() and y.isdigit():
    print(x ,'+', y ,'=',int(x) + int(y));
    print(x ,'×', y ,'=',int(x) * int(y));
    print(x + '的' + y + '次方是:',int(x) ** int(y));
else:
    print('您的输入有误')
    