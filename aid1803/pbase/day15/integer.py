def my_integer(n):
    for i in range(1,n+1):
        yield i

num = int(input('请输入一个n: '))
gen = my_integer(num)
it  = iter(gen)
# for i in range(num):
print(next(it))
print(next(it))
print(next(it))