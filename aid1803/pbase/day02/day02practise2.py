#输入一个数字，打印这个数字的绝对值（要求用条件表达式，不允许用abs函数）
a = int(input('请输入一个整数'))
b = a if a > 0 else -a
print(a,'绝对值是',b)