class Student():
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


