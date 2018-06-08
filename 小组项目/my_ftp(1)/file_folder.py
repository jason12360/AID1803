import os
from time import *        
from file import File



class File_Folder():
    def __init__(self,path):
        
        self.dir_name = os.path.split(path)[-1]
        self.filelist = os.listdir(path)
        self.num = len(os.listdir(path))
        self.serverposition = None

    
    #获得文件夹名字
    def get_name(self):
        return self.dir_name

    #获得文件夹内的文件目录列表
    def get_file_list(self):
        return self.filelist

    #创建文件实例
    def file_property(self):
        L = []
        l = self.filelist
        for i in l:
            file_pro = File()
            L.append(file_pro)
        return L


    # #文件目录列表的增加
    # def add_file_list(self,new_filename):
    #     global l
    #     l = self.filelist
    #     if new_filename not in l:
    #         l.append(new_filename)
    #     return l



    # #文件目录列表的删除
    # def drop_file_liset(self,filename):
    #     l = self.filelist
    #     l.remove(filename)
    #     return l



# A = '/home/tarena/aid1803/'
# C = File_Folder(A)
# # kj = C.get_name()
# kj = C.get_file_list()
# # kj = C.file_property()

# # for a in kj:
# #     print(i)
# print(C)
# print(kj)








        


