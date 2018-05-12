# 1.定义一个类human（人类）
# 有三个属性：
#     姓名：name
#     年龄:age
#     家庭住址：adress(可省略没有)
# 有如下方法：
#     show_info(self)用来显示人的信息
#     update_age(self)用来让这个人的年龄增加一岁
#     def input_human():
#         输入一些人的信息，姓名为空结束
#     def main():
#         docs = input_human()
#         for h in docs:
#             h.show_info()   #列出所有人信息
#         for h in docs:
#             h.update_age()
#         for h in docs:
#             h.show_info
#     main()

class Human():
    human_count = 0

    def __init__(self,name,age,address='不详'):
        self.name = name
        self.age = age
        self.address = address
        self.__class__.human_count += 1
        self.number = self.__class__.human_count

    def show_info(self):
        print('----------------')
        print('号码：',self.number)
        print('姓名：',self.name)
        print('年龄：',self.age)
        print('地址：', self.address)
        print('----------------')

    def update_age(self):
        self.age += 1

    @classmethod
    def get_human_count(cls):
        return cls.human_count

    def __del__(self):
        self.__class__.human_count -=1

def input_human():
    human_list = []
    while True:
        name = input('请输入姓名：')
        if not name:
            return human_list
        age = int(input('请输入年龄：'))
        address = input('请输入地址：')
        if not address:
            human = Human(name,age)
        else: 
            human = Human(name,age,address)
        human_list.append(human)
    
def main():
        docs = input_human()
        for h in docs:
            h.show_info()   #列出所有人信息
        for h in docs:
            h.update_age()
        for h in docs:
            h.show_info()

main()


