class Human:
    def __init__(self,n,a):
        self.name = n
        self.age = a
        print('Human类的__init__被调用')
    def show_info(self):
        print('姓名', self.name)
        print('年龄',self.age)

class Student(Human):
    def __init__(self,n,a,s=0):
        super().__init__(n,a)
        self.score = s
        print('Student类的__init__被调用')
    def show_info(self):
        super().show_info()
        print('成绩',self.score)

s1 = Student('张学友',40)
s1.show_info()