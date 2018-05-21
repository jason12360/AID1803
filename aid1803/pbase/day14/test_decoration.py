def dec(f): 
    n = 3 
    print('jjj')
    def wrapper(*args, **kw): 
        return f(*args, **kw) * n 
    return wrapper 

@dec 
def foo(n): 
    return n * 2

# print(foo(3))