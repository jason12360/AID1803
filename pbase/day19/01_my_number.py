#此示例示意str(x)函数和repr(x)函数的重写方法
class MyNumber:
    def __init__(self,value):
        self.data = value
    # def __repr__(self):
    #     return 'aaa'
    def __str__(self):
        print('__str__方法被调用')
        return '数字：%d' %self.data
n1 = MyNumber(100)
n2 = repr(n1) +'n' #它会调用n1.__repr__（）方法
print(str(n1))
print(n2)
