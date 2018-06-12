"""
基于TCP的局域网文件服务器
18527端口是命令端口
18528端口是数据聊天端口
功能：聊天，上传文件，下载文件

"""
from server_class import *
import multiprocessing as mp 
import sys,os
# from database_handler import *
# from file_folder import *

# 主函数  命令端——进程
def main():
    #创建三个进程，控制端，数据端
    ctrl_p=mp.Process(target=control_port)
    data_p=mp.Process(target=data_port)

    #开启进程
    ctrl_p.start()
    data_p.start()

    #回收
    ctrl_p.join()
    data_p.join()

if __name__ == '__main__':
 	main()

