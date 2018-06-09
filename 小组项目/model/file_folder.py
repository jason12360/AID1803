#这是一个文件夹类，用来保存文件夹内文件的相关属性，以便未来调用
#1.在客户端文件将有类中的unpack方法传入
#2.在服务器端，将在初始化方法中通过遍历文件的方式加入
import os
import sys
from file import File

class Filefolder:

	def __init__(self,resource='C'):
		#由客户端创建的实例时
		self.file_list = []
		if resource == 'C':
			pass
		# #由服务端创建实例时，需要遍历文件夹路径中非文件夹或非隐藏的文件
		# else:
		# 	file_list = os.listdir(resource)
		# 	for filename in file_list:
		# 		if filename[0] != '.' and os.path.isfile(resource + filename):
		# 			self.file_list.append(File(resource+filename))

	def add_file(self,myfile):
		self.file_list.append(myfile)

	def get_file_list(self):
		return self.file_list
	def pack(self):
		result = ''
		for file in self.file_list:
			result+='['
			result+=list(file.get_info()).join(',')
			result+='],'
		if not result:
			return '{}'
		result ='{'+result[:-1] + '}'
		return result

	def unpack(self):
		pass

#以下是一个测试
def main():

	print(ff.pack())

if __name__=='__main__':
	main()

