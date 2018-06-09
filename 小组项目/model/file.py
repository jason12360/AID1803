import os
from time import *

class File(object):
    def __init__(self,file_path):
        self.filename = os.path.split(file_path)[-1]
        self.filesize = os.path.getsize(file_path)
        self.filelocal_path = os.path.split(file_path)[0]
        self.filetype = None
        self.usrid = None

    def get_info(self):
        return (self.filename,self.filesize,self.filelocal_path,self.file_last_mtime,self.file_create_time)

    def get_name(self):
        return self.filename

    def get_size(self):
        return self.filesize


    def get_local_path(self):
        return self.filelocal_path

    def get_type(self):
        pass

    def get_usrid(self):
        pass

    def set_server_path(self,serverPath):
        self.server_path = serverPath
        # self.server_path = os.path.split(serverPath)[0]P
    
    def get_server_path(self):
        return self.server_path

    def set_last_mtime(self,last_mtime):
        self.file_last_mtime = last_mtime

    def get_last_mtime(self):
        return self.file_last_mtime

    def set_file_create_time(self,create_time):
        self.file_create_time = create_time

    def get_creat_time(self):
        return self.file_create_time
    def pack(self):
        result = ','.join(list(self.get_info()))
        result ='['+result+']'
        return result









# self.mtime = ctime(os.path.getmtime(file_path))


# File_Path = '/home/tarena/OO/user.txt'
# serverPath = '/home/tarena/day01.txt' 
# file1 = File(File_Path)
# name = file1.get_name()
# print('文件名',name)
# size =file1.get_size()
# print('文件大小',size)
# lo_path = file1.get_local_path()
# print('本地文件路径',lo_path)
# file2 = File(File_Path)
# file2.set_server_path(serverPath)
# spath = file2.get_server_path()
# print('服务器路径',spath)
# file2.set_last_mtime(serverPath)
# lastmtime = file2.get_last_mtime()
# print('服务器文件时间',lastmtime)
# file2.set_file_create_time(serverPath)
# creatime = file2.get_creat_time()
# print('文件创建时间',creatime)


