#此示例示意abs(obj)函数重写方法obj.__abs__()方法的使用
class MyInteger:
    def __init__(self,value):
        self.data = value
    def __repr__(self):
        return 'MyInteger(%d)'%self.data
    def __abs__(self):
        return MyInteger(self.data) if self.data >= 0 else MyInteger(-self.data)
    def __len__(self):
        """len(x)函数规定只能返回整数值"""
        return 100
I1 = MyInteger(-10)
print(I1)
print(abs(I1))
print(len(I1))