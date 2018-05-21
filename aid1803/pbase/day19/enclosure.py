class A:
    def __init__(self):
        self.__p1 = 100 #创建私有属性
    def test(self):
        print(self.__p1)
a = A()
print(a.__p1) #出错，不可以访问


