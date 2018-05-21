
class A:
    def work(self):
        print('A类的work方法被调用')

class B(A):
    def work(self):
        print('B类的work方法被调用')


b =B()
b.work() #子类已经覆盖了父类的方法

