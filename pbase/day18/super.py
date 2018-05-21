#此示例示意 super函数访问父类的覆盖方法
class A:
    def work(self):
        print('A类的work方法被调用')

class B(A):
    def work(self):
        print('B类的work方法被调用')
    def doworks(self):
        self.work() #调用B类的  
        print('----------------')
        super(__class__,self).work() #调用超类的方法
        print('----------------')
        super().work() #一样会调用超类的方法


b =B()
b.work() #子类已经覆盖了父类的方法
print('-----以下用b调用覆盖版本的方法-----')
A.work(b) #A类的work方法被调用
super(B,b).work()
b.doworks()