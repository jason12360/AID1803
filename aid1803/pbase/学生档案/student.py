class student():
    elements = [('name',10,'姓名'),
                ('age',7,'年龄'),
                ('score',9,'成绩')]
    def __init__(self,name = '',age = '',score = ''):
        self.name = name
        self.age  = age
        self.score = score

    # def show_info(self):
    #     print('|'+self.name.center(10)+
    #           '|'+self.age.center(7)+
    #           '|'+self.score.center(9)+'|')

    # def show_info_in_string(self):
    #     return ('name:%s,age:%s,score:%s'%(self.name,self.age,self.score))

    def get_info(self):
        return (self.name,self.age,self.score)

    def get_age(self):
        return self.age

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name
    def set_score(self,score):
        self.score = score
    



