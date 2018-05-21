# 示意反向算术运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data
    # def __add__(self,other):
    # 	return MyList(self.data + other.data)

    def __mul__(self, n):
        return MyList(self.data * n)

    def __rmul__(self, lhs):
        print('__rmul__被调用,lhs', lhs)
        return MyList(self.data * lhs)


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
# L3 = L1 + L2
# print('L3 =',L3)
L4 = L1 * 2
print('L4 =', L4)
L5 = 2 * L1
print('L5 =', L5)
