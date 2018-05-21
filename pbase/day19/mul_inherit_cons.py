#小张写了一个类A
class A:
    def m(self):
        print('A.m()被调用')
#小李写了一个类B
class B:
    def m(self):
        print('B.m()被调用')
#小王写了一个类C，多继承了A和B
class AB(B,A):
    pass
ab = AB()
ab.m() #请问调用谁？
