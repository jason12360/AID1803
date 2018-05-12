# 实现两个定义列表的相加
class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __add__(self, other):
        return MyList(self.data + other.data)

    def __mul__(self, n):
        return MyList(self.data * n)


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L3 = L1 + L2
print('L3 =', L3)
L4 = L1 * 2
print('L4 =', L4)
