# def fibonacci(n):
#      ...
#      yield..
#     1)输入前20个数
#     2）求前30个数的和

def fibonacci(n):
    
    pre = 1
    _pre = 1
    if n <= 0:
        return
    yield pre
    if n <= 1:
        return
    yield _pre
    for i in range(n-2):
        pre,_pre =_pre ,_pre + pre
        yield _pre
        
  

def main():
    n = int(input('请输入n：'))
    gen = fibonacci(n)
    _sum = 0
    for i in gen:
        print(i,end = ' ')
        _sum += i
    print()
    print ('前20个数的和为',_sum)

main()


