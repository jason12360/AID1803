def my_yeild():
    print('即将生成2')
    yield 2
    print('即将生成3')
    yield 2 + 1 #等同于 yield 3
    print('即将生成5')
    yield 5
    print('即将生成7')
    yield 7
    print('生成函数调用结束')

gen = my_yeild()
it = iter(gen) #用gen返回一个迭代器
#myyeild 将从上一次停止的位置开始执行