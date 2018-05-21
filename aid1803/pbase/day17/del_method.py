class Filemanage:
    """定义一个文件管理员类"""
    def __init__(self,filename = 'a.txt'):
        self.file = open(filename,'w')

    def write_line(self,string):
        self.file.write(string)
        self.file.write('\n')
    def __del__(self):
        self.file.close()
        print('文件已关闭')


fm = Filemanage()
fm.write_line('hello world')
fm.write_line('这是中文写的第二行')
fm = 1
#del fm
while True:
    pass
print('程序结束')