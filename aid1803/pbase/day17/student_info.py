# 练习：
#     自己写一个Student类，此类的对象有属性name,age,score,用来保存学生的姓名，年龄，成绩
#         1）写一个函数 input_student 读入n 个学生的信息，用对象来存储这些信息（不用字典），并返回对象的列表
#         2）写一个函数output_student 打印这些学生的信息（格式不限）
#     示意：
class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def input_student():
    student_list = []
    while True:
        name = input('请输入学生姓名：')
        if not name:
            return student_list
        age = input('请输入学生年龄：')
        score = input('请输入学生分数：')
        student = Student(name,age,score)
        student_list.append(student)


def output_student(student_list):
    for student in student_list:
        print('姓名：%s,年龄：%s,分数：%s'%(student.name,student.age,student.score))

def main():
    L = input_student()
    output_student(L)
main()