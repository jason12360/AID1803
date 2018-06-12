#这是一个文件夹类，用来保存文件夹内文件的相关属性，以便未来调用
#1.在服务器端，将通过读取数据库获取filefolder,并由网络端调用pack方法发送给客户端
#2.客户端收到消息后,通过unpack方法将数据解析生成fileforlder
import os
import sys
from file import File

class Filefolder:

	def __init__(self):
		#由客户端创建的实例时
		self.file_list = []
        
    #myfile是一个文件实例
	def add_file(self,myfile):
		self.file_list.append(myfile)

	def get_file_list(self):
		return self.file_list

	def pack(self):
		result = ''
		for file in self.file_list:
			result+=file.pack()
			result+=result+','
		if not result:
			return '{}'
		result ='{'+result[:-1] + '}'
		return result

	def unpack(self,string):
		file_list_string = string[1:-1].split(',')
		for file_string in file_list_string:
			file = File()
			file.unpack(file_string)
			self.add_file(file)

	def to_list(self):
		result = []
		for file in self.file_list:
			result.append(file.get_info())
		return result

#以下是一个测试
def main():
    f=File()
    f.create_file('/Users/liwenhui/Desktop/my_ftp/file.py')
    f.set_last_mtime('2108-01-01 07:22:22')
    f.set_file_create_time('2108-01-01 07:22:22')
    f.set_server_path('')
    f1=Filefolder()
    f1.add_file(f)
    print(f1.to_list())

if __name__=='__main__':
	main()

