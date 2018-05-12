# 此程序示意闭包用法
# 1.fn为内嵌函数
# 2.fn用到了fn外部的变量y
# 3.make_power将fn绑定的函数对象返回给调用者
def make_power(y):
    def fn(x):
        print(id(y))
        return x**y
    return fn





print('5的平方是：',pow2(5))

pow4 = make_power(4)
print('5的四次方是：',pow4(5))

pow1000 = make_power(1000)
print('5的四次方是：',pow1000(5))
     
