class student_view:
	
	def __init__(self,model):
		self.view_elements = model.elements
	def show_menu(self):
	    print('+-----------------------------------+')
	    print('| 1)  添加学生信息                  |')
	    print('| 2)  显示所有学生的信息            |')
	    print('| 3)  删除学生信息                  |')
	    print('| 4)  修改学生成绩                  |')
	    print('| 5)  按学生成绩高-低显示学生信息   |')
	    print('| 6)  按学生成绩低-高显示学生信息   |')
	    print('| 7)  按学生年龄高-低显示学生信息   |')
	    print('| 8)  按学生年龄低-高显示学生信息   |')
	    print('| 9)  保存学生信息                  |')
	    print('|10)  读取学生信息                  |')
	    print('| q)  退出                          |')
	    print('+-----------------------------------+')

	def display_student_info(self,student):
		s = '|'
		for e in self.view_elements:
			s += student.__dict__[e[0]].center(e[1]) + '|'
		print(s)
		self.__add_line()

	def __add_line(self):
		s1 = '+'
		for e in self.view_elements:
			s1 += '-' * e[1] + '+'
		print(s1)

	def draw_table_head(self):
		s2 = '|'
		for e in self.view_elements:
			s2 += e[0].center(e[1]) + '|'
		self.__add_line()
		print(s2)
		self.__add_line()

	def IO_add(self,i):
		result = []
		print('请输入第', i ,'个学生信息，输入“回车”返回上级菜单。')
		for e in self.view_elements:
			_ = '请输入学生'+ e[2] + ': '
			a = input(_)
			if not a:
				return None
			result.append(a)
		return result
		
