"""
Myftp 类
数据端，聊天和数据传输
"""
import my_protocol
from socket import *
import sys,os
from file_folder import *
import signal
from multiprocessing import Queue
import time
from database_handler import My_Mysql
#服务器文件夹
FIlE_PATH="/home/tarena/lwh/my_ftp/"
file_path_u="/home/tarena/lwh/my_ftp/upload/"


#创建队列
Q=Queue(2)


# 数据端——进程
def data_port():
    '''
    UDP套接字
    数据端口开启
    '''
    HOST='0.0.0.0'
    PORT=18528
    ADDR=(HOST,PORT)
    s=socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    while True:
        T=Q.get()
        print(T)
        #按请求发送内容
        if T == 'l':
            print('recvfrom...')
            d,addr=s.recvfrom(1024)
            print(d,addr)
            data=Q.get()
            print(data)            
            print('ok')
            #让data传进来时是bytes
            # print(data.decode())
            s.sendto(data,addr)
           
        elif T=='d':
            print('recvfrom...')
            d,addr=s.recvfrom(1024)
            text=Q.get()        
            s.sendto(text,addr)
            time.sleep(0.5)
            s.sendto(b'@end',addr)       
            print('-------')
         
        elif T=='u':
            #接收上传文件
            filename=Q.get()
            print(filename)
            op_file=file_path_u+filename
            with open(op_file,'wb') as f:
                while True:
                    data,addr=s.recvfrom(1024)
                    if data==b'@end':
                        break
                    f.write(data)
            print('+++++')
          
    
# 命令端——进程
def control_port():
    # 参数
    ctrl_HOST='0.0.0.0'
    ctrl_PORT=18527
    ctrl_ADDR=(ctrl_HOST,ctrl_PORT)
    BUFFERSIZE=4096
    #创建套字节
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ctrl_ADDR)
    s.listen(10)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("等待连接")
    #等待客户端连接
    while True:
        try:
            connfd,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit(0)
        except Exception:
            continue
        print("客户登录",addr)
        # 创建新的进程和客户通讯
        pid=os.fork()
        if pid<0:
            print("命令端子进程创建失败")
            connfd.close()
            continue
        elif pid==0:
            #客户端里不需要服务端套接子
            s.close()
            #创建客户端通信对象
            c_ftp=MyFtp_Server(connfd)
            while True:
                    #接受完的data判断是否丢包,进行解包处理
                    l=my_protocol.unpake_TCP(connfd)
                    # 客户端功能选择
                    if l != -1:
                        #l返回的结构：请求类别 + 属性 + 内容 + 结束符
                        #             l[0]   l[1]   l[2]   l[3]
                        if l[0]=='list':
                            c_ftp.list(l[2])
                        elif l[0]=='upld':
                            c_ftp.receive(l[2])
                        elif l[0]=='dwld':    
                            c_ftp.send(l[2])
                        elif l[0]=='chat':
                            # l[2] ismessage
                            c_ftp.chat(l[2])
                        elif l[0]=='login':
                            #l[1] 是账号
                            #l[2] 是密码
                            c_ftp.login(l[1],l[2])
                        elif l[0]=='reg':
                            c_ftp.register(l[1],l[2])

                        elif l[0]=='quit':
                            c_ftp.quit()
        #父进程关闭已经在新进程里引用的客户套接子
        #继续监听
        else:
            connfd.close()
            continue


class MyFtp_Server():
    '''
    MyFtp_server 有五个函数
    '''
    def __init__(self,conn):
        self.client= conn
        self.database_handler = My_Mysql()
    
    #获取list
    def list(self,foldername):
        #创建file_folder实例
        if foldername==' ':
            fn=File_Folder(FIlE_PATH)
        else:
            fn=File_Folder(FIlE_PATH+foldername+'/')
        data=fn.get_file_list()
        Q.put('l')
        Q.put(str(data).encode())
        # print(fn.get_file_list())
        return 

    #接受客户端下载请求，发送文件
    def send(self,filename):
        op_file=FIlE_PATH+filename
        print(op_file)
        text=b''
        with open(op_file,'rb') as f:
            while True:
                data=f.read(2048)
                if not data:
                    break
                #不考虑文件大小
                text+=data
        # print(text)
        Q.put('d')
        Q.put(text)
        return 
    #接受客户端上传请求，接收文件
    def receive(self,filename):
        Q.put('u')
        Q.put(filename)
   
    #聊天
    def chat(self,message):
        #转发给其他客户端
        pass

    def login(self,username,password):

        result = self.database_handler.select_user(username)
        if password == result[0][2]:
            self.client.send(b'Y')
        else:
            self.client.send(b'N')


    def register(self,username,password):
        print(username,password)
        result = self.database_handler.select_user(username)
        if not result:
            self.database_handler.add_user(username,password)
            self.client.send(b'Y')
        else:
            self.client.send(b'N')
    #退出
    def quit(self):
        print("客户端退出")
        self.client.close()
        sys.exit(0)


