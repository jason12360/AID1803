class Human:
    total_count = 0 #类变量，用于记录对象的个数
    def __init__(self,name):
        self.name = name
        self.__class__.total_count += 1 #人数加人
        print(name,'对象创建')

    def __del__(self):
        self.__class__.total_count -= 1

# print(Human.total_count)
# h1 = Human()
# print(h1.total_count) #0 #不会出错
# Human.total_count = 1
# human.total_count = 2 创建一个实例变量
# h1.__class__.total_count = 3 间接修改类变量
# 见：class_variable.py
print ('当前对象的个数是：',Human.total_count)
h1 = Human('张飞')
h2 = Human('赵云')

print('当前对象的个数是：',Human.total_count)
del h2
print('当前对象的个数是：',Human.total_count)