def my_yeild():
    yield 2
    yield 2 + 1 #等同于 yield 3
    yield 5
    yield 7
    print('生成函数调用结束')

gen = my_yeild()
it = iter(gen) #用gen返回一个迭代器


