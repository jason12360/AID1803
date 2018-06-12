from database_handler import *
import os

#系统初始化，获取文件夹里的文件，生成file类，比添加到file_list          
FIlE_PATH="/home/tarena/lwh/my_ftp/"
f=File()
FL=Filefolder()
db=My_Mysql
filelist = os.listdir(FIlE_PATH)
print(filelist)
#创建文件实例,加入Filefolder的self.file_list = []
for file in filelist:
   f=File(file)
   # print(f)
   db.add_file(f)


