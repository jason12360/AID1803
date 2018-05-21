#此示例示意数值类型转换函数重写
class MyNumber:
    '''此类是自定义的类，用于表示自定义数字的类型'''
    def __init__(self,v):
        self.data = v 
    def __repr__(self):
        return 'MyNumber(%d)'%self.data
    def __int__(self):
        return int(self.data)
    def __float__(self):
        return float(self.data)
n1 = MyNumber('100')
print(int(n1))###?
print(float(n1))