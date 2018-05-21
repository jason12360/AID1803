
class A:
    v = 0
    @classmethod
    def get_v(cls):
        return cls.v
    @classmethod
    def set_v(cls,n):
        cls.v = n
    def print_text(self,t):
        print(t)
print(A.get_v())
A.v = 1
print(A.get_v())
A.set_v(100)
print(A.get_v())
a = A()#创建一个实例
a.set_v(200)
print(a.get_v())
b = A()
print(b.get_v())
A.print_text(b,'aa')
b.print_text('aaa')