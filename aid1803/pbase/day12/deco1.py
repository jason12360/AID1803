def mydeco(fn): #装饰器函数
    def fx():
        print('+++++++++++')
        fn()
        print('-----------')
    return fx
@mydeco #装饰器可以使用@语法解决
def hello(): #被装饰函数
    print('hello tarena')

# hello = mydeco(hello) #此

hello()