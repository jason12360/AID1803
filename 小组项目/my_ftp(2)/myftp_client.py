'''
客户端
'''
from client_class import *
import sys
import multiprocessing as mp

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

    sys.exit("主程序退出")

    
if __name__=="__main__":
    main()






