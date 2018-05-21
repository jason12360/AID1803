# 练习：
#     实现有序集合类 OrderSet(),能实现两个集合的交集&，并集|
# ，补集~,对称补集^,==,!=等操作（写集合相同）
# 要求：
#     集合内部用list存储
# 测试用例：
#     s1 = OrderSet([1,2,3,4])
#     s2 = OrderSet([3,4,5])
#     print(s1 & s2)  OrderSet([3,4])
#     print(s1 | s2)  OrderSet([1,2,3,4,5])
#     print(s1 ^ s2)  OrderSet([1,2,5])
#     if OrderSet([1,2,3]) != OrderSet([1,2,3,4]):
#         print('不相同')
#     其他自己测试...


class OrderSet:
    def __init__(self, iterable):
        self.data = []
        for x in iterable:
            if x not in self.data:
                self.data.append(x)
        sorted(self.data)

    def __repr__(self):
        return 'OrderSet(%r)' % self.data

    def __or__(self, rhs):
        result = self.data.copy()
        for e in rhs.data:
            if e not in result:
                result.append(e)
        return OrderSet(result)

    def __and__(self, rhs):
        result = []
        for e in rhs.data:
            if e in self.data:
                result.append(e)
        return OrderSet(result)

    def __xor__(self, rhs):
        return (self | rhs)-(self & rhs)

    def __sub__(self, rhs):
        result = self.data.copy()
        for e in rhs.data:
            if e in result:
                result.remove(e)
        return OrderSet(result)

    def __ne__(self,rhs):
        return self.data != rhs.data

s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)

if OrderSet([1,2,3,4]) != OrderSet([1,2,3,4]):
    print('不相同')
