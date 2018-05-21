
class MyList:
    '''定义一个容器类，用于存储任意类型的数据，其内部的存储方式用list实现'''
    def __init__(self,iterable):
        self.data = [x for x in iterable]
    def __repr__(self):
        return 'MyList(%s)'%self.data
    def __len__(self):
        print('__len__方法被调用。')
        return len(self.data) #返回列表长度
    def __iter__(self):
        '''此方法把MyList类型的对象做为可迭代对象使用
            此方法需要返回迭代器'''
        self.cur_pos = 0
        return self
    def __next__(self):
        if self.cur_pos < len(self.data):
            result = self.data[self.cur_pos]
            self.cur_pos += 1
        else:
            raise StopIteration()
        return result
    # def __bool__(self):
    #     '''此方法用于bool(obj)函数取值，优先取此函数的返回值
    #        此方法用于定义bool(obj)的取值规则'''
    #     #规则：所有元素的和为0，则返回False否则返回True
    #     return sum(self.data) != 0

# class MyListIterator:
#     '''此类定义一个迭代器类，用于生成能够访问MyList对象的迭代器'''
#     def __init__(self,lst_data):
#         self.data = lst_data
#         self.cur_pos = 0 #设置迭代器的其实位置是0
#     def __next__(self):
#         if self.cur_pos < len(self.data):
#             result = self.data[self.cur_pos]
#             self.cur_pos += 1
#         else:
#             raise StopIteration()
#         return result

myl = MyList([1,-2,5,-4])
it = iter(myl)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

