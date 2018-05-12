class student_controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
        self.studentlist = []

    def add_student(self):
        i = 1 
        while True:
            self.__display_data()
            _ =self.view.IO_add(i)
            if not _:
                break  
            student = self.model(*_)
            i += 1
            self.studentlist.append(student)

    def list_student(self):
        self.__display_data()
        

    def __display_data(self,*args):
        self.view.draw_table_head()
        if args == ():
            for student in self.studentlist:
                 self.view.display_student_info(student)
        else:
            for student in args:
                 self.view.display_student_info(student)

    def remove_student(self):
        while True:
            self.__display_data()
            name = input('请输入您要删除学生的姓名，输入“回车”返回上级菜单：')
            if not name:
                break
            for student in self.studentlist:
                if student.get_name() == name:
                    self.studentlist.remove(student)
                    print('已经成功删除姓名为', name,'的学生')
                    break
            else:
                print('查无此学生')



    def modify_student(self):
        while True:
            self.__display_data()
            name = input('请输入您要修改学生的姓名，输入“回车”返回上级菜单：')
            if not name:
                break
            score = input('请输入您要修改学生的分数：')
            for student in self.studentlist:
                if student.get_name() == name:
                    student.set_score(score)
                    print('已经成功修改姓名为', name,'的学生的分数')
                    break
            else:
                print('查无此学生')

    def sort_student(self,*,list_key,high2low):
        sorted_list = sorted(self.studentlist,key = lambda x: int(x.__dict__[list_key]),reverse = high2low)
        self.__display_data(*sorted_list)

    def string2model(saved_string):
        studentlist = []
        for student_string in saved_string:
            student_string = student_string[0:-1] #去除后面的换行符
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
            student_string = 'name:%s,age:%s,score:%s'%student.get_info()
            student_string_list.append(student_string)
        return student_string_list

    def load_student_list():
        try:
            filename = 'si.txt'
            with open(filename) as file_obj:
                student_string_list = file_obj.readlines()
            return string2model(student_string_list)
        except:
            return []

    def save_students_list():
        filename = 'si.txt'
        with open(filename,'w') as file_obj:
            for line in model2string(lst):
                print(line,file = file_obj)