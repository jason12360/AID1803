#此示例示意单继承的语法及使用方法
class Human: #人
    def say(self,what):
        print('说',what)
    def walk(self,distance):
        print('走了',distance,'公里')

h1 = Human()
h1.say('今天天气不错')
h1.walk(5)


class Student(Human):
    def study(self,subject):
        print('学习了',subject,'科目')

class Teacher(Human):
    def teach(self,subject):
        print('正在教',subject)

s1 = Student()
s1.say('今天晚饭吃什么')
s1.walk(3)
s1.study('python')