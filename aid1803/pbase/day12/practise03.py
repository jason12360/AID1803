# 练习：
#     请编写函数fun其功能是计算并输出下列多项式的和
#     Sn = 1 + 1/1! +1/2! + ...+1/n!

#     请编写函数fun,他的功能是计算下列多项式的和并返回：
#     s = 1 + x + x**2/2! + x**3/3! +...+x**n/n!

#     print(fun(10))
from math import factorial as fact,e,inf
def q1(n):
    sum = 0
    for i in range(n+1):
        sum += 1/fact(i)
    return sum

def q2(x,n):
    sum = 0
    for i in range(n+1):
        
        sum += x **i/fact(i)

    return sum

print(q1(100))
print(e)

print(q2(3.1,10))