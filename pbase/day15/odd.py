# 练习：
# 写一个函数myodd(start,stop)
# 用于生成start开始到stop结束的所有奇数，不包含stop

def myodd(start,stop):
    i = start
    while i < stop:
        if i % 2 ==1:
            yield i
        i += 1

L = [x for x in myodd(1,10)]
print(L)
for x in myodd(10,20):
    print(x)
