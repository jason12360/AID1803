# 练习：已知有一个集合：
#  s= {'工商银行'，'建设银行','中国银行','农业银行'}
#  用for来遍历
#  用while来遍历
s= {'工商银行','建设银行','中国银行','农业银行'}
it = iter(s)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break