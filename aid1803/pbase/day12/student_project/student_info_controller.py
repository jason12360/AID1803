from student import Student
lst = []


def input_student():
    i = 1
    while True:
        print('请输入第', i, '个学生信息，输入“回车”返回上级菜单。')
        name = input('请输入学生姓名：')
        if not name:
            break
        age = input('请输入学生年龄：')
        score = input('请输入学生成绩：')
        lst.append(Student(name, age, score))
        print('已成功添加学生。')
        i += 1
    return lst


def output_student():
    display_data(lst)


def display_data(lst):
    print('+----------+-------+---------+')
    print('|  name    |  age  |  score  |')
    print('+----------+-------+---------+')
    for student in lst:
        print('|%10s|%7s|%9s|' % student.get_info())
    print('+----------+-------+---------+')


def remove_student():
    while True:
        display_data(lst)
        name = input('请输入您要删除学生的姓名，输入“回车”返回上级菜单：')
        if not name:
            break
        for student in lst:
            if student.name == name:
                lst.remove(student)
                print('已经成功删除姓名为', name, '的学生')
                break
        else:
            print('查无此学生')


def modify_student():
    while True:
        display_data()
        name = input('请输入您要修改学生的姓名，输入“回车”返回上级菜单：')
        score = input('请输入您要修改学生的分数：')
        if not name:
            break
        for student in lst:
            if student.name == name:
                student.score = score
                print('已经成功修改姓名为', name, '的学生的分数')
                break
        else:
            print('查无此学生')


def sort_student(*, list_key, high2low):
    sorted_list = sorted(sorted_list, key=lambda x: int(
        x.__dict__[list_key]), reverse=high2low)
    output_student(sorted_list)


def string2model(saved_string):
    studentlist = []
    for student_string in saved_string:
        student_string = student_string[0:-1]  # 去除后面的换行符
        temp = student_string.split(',')
        student = Student()
        for item in temp:
            temp2 = item.split(':')
            student.__dict__[temp2[0]] = temp2[1]
        studentlist.append(student)
    return studentlist


def model2string(student_list):
    student_string_list = []
    for student in student_list:
        student_string = 'name:%s,age:%s,score:%s' % student.get_info()
        student_string_list.append(student_string)
    return student_string_list


def load_student_list():
    try:
        filename = 'si.txt'
        with open(filename) as file_obj:
            student_string_list = file_obj.readlines()
        return string2model(student_string_list)
    except Exception:
        return []


def save_students_list():
    filename = 'si.txt'
    with open(filename, 'w') as file_obj:
        for line in model2string(lst):
            print(line, file=file_obj)
