# 示意反向算术运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __add__(self, other):
        return MyList(self.data + other.data)

    def __iadd__(self, rhs):
        print('__iadd__方法被调用')
        self.data.extend(rhs.data)
        return self


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L1 += L2
print('L1 =', L1)
