def input_student(lst):
    i = 1
    while True:
        print('请输入第', i ,'个学生信息，输入“回车”返回上级菜单。')
        name = input('请输入学生姓名：')
        if not name:
            break
        age = input('请输入学生年龄：')
        score = input('请输入学生成绩：')
        lst.append({'name':name,
                    'age':age,
                    'score':score})
        print('已成功添加学生。')
        i += 1
    return lst

def output_student(lst):
    display_data(lst)
    while True:
        command = input('输入“回车”返回上级菜单。')
        if not command:
            break

def display_data(lst):
    print('+----------+-------+---------+')
    print('|  name    |  age  |  score  |') 
    print('+----------+-------+---------+')
    for student in lst:
        print('|'+student['name'].center(10)+'|'+student['age'].center(7)+'|'+student['score'].center(9)+'|')
            
    print('+----------+-------+---------+')

def remove_student(lst):
    while True:
        display_data(lst)
        student_name = input('请输入您要删除学生的姓名，输入“回车”返回上级菜单：')
        if not student_name:
            break
        for student in lst:
            if student['name'] == student_name:
                lst.remove(student)
                print('已经成功删除姓名为', student_name,'的学生')
                break
        else:
            print('查无此学生')



def modify_student(lst):
    while True:
        display_data(lst)
        student_name = input('请输入您要修改学生的姓名，输入“回车”返回上级菜单：')
        student_score = input('请输入您要修改学生的分数：')
        if not student_name:
            break
        for student in lst:
            if student['name'] == student_name:
                student['score'] = student_score
                print('已经成功修改姓名为', student_name,'的学生的分数')
                break
        else:
            print('查无此学生')

def sort_student(lst,*,list_key,high2low):
    sorted_list = lst.copy()
    sorted_list = sorted(sorted_list,key = lambda x: int(x[list_key]),reverse = high2low)
    output_student(sorted_list)

def string2model(saved_string):
    studentlist = []
    for student_string in saved_string:
        student_string = student_string[0:-1]
        temp = student_string.split(',')
        student_dict = {}
        for item in temp:
            temp2 = item.split(':')
            student_dict[temp2[0]] = temp2[1]
        studentlist.append(student_dict)
    return studentlist

def model2string(student_list):
    student_string_list = []
    for student in student_list:
        temp = ''
        for k in student:
            temp += (k + ':'+ student[k]+',')
        student_string_list.append(temp[0:-1])
    return student_string_list

def load_student_list():
    try:
        filename = 'si.txt'
        with open(filename) as file_obj:
            student_string_list = file_obj.readlines()
            print(student_string_list)
        return string2model(student_string_list)
    except:
        return []

def save_students_list(lst):
    filename = 'si.txt'
    with open(filename,'w') as file_obj:
        for line in model2string(lst):
            print(line,file = file_obj)