#此示意__slots__属性的用法

class Student():
    """docstring for Student"""
    __slots__=['name','age']
    def __init__(self, n,a):
        self.name = n
        self.age = a

s1= Student('小张',20)
# s1.Age = 21 #可以吗？此时错写了age为Age
print(s1.__dict__) #出错，因为没有这个__dict__字典
@classmethod