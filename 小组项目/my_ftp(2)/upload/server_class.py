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
from database_handler import *
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
            #先发属性
            f_property=Q.get()
            if f_property=='None':
                s.sendto(b'None',addr)
            else:
                s.sendto(f_property.encode(),addr)
                #再发文件
                while True:
                    text=Q.get()   
                    s.sendto(text,addr)
                    time.sleep(0.1)
                    if not text:
                        break     
                time.sleep(0.1)
                s.sendto(b'@end',addr)
                # 等待客户端10s，返回是否下载完成
                ask,addr=s.recvfrom(1024,10)
                if ask==b'ok':
                    print('用户接受完毕') 
                else:
                    print('用户接受失败') 
                print('-------')
         
        elif T=='u':
            #接收上传文件,先判断文件是否同名
            filename=Q.get()
            print(filename)
            #获取地址，且判断文件是否重名
            ms=My_Mysql()
            result=ms.select_file_by_filename(filename)
            print(result)
            d,addr=s.recvfrom(1024)
            #接收文件到服务器
            if result==None:
                print('none')         
                s.sendto(b'go',addr)
                time.sleep(0.1)               
                op_file=file_path_u+filename
                with open(op_file,'wb') as f:
                    while True:
                        data,addr=s.recvfrom(1024)
                        if data==b'@end':
                            break
                        f.write(data)
                time.sleep(0.1)
                s.sendto(b'ok',addr)
                #编写属性
                print("编写属性")
                up=File(filename,
                        os.path.getsize(op_file),
                        op_file,
                        time.strftime('%Y-%m-%d %H:%M:%S'),
                        time.strftime('%Y-%m-%d %H:%M:%S'))

                #添加到mysql
                print("添加到mysql")
                ms.add_file(up)
                print('+++++')

            else:
                s.sendto(b'ojbk',addr)
                print('end')

#系统初始化，获取文件夹里的文件，生成file类，比添加到file_list          
# def server_file_init():
#     f=File()
#     FL=Filefolder()
#     filelist = os.listdir(FIlE_PATH)
#     #创建文件实例,加入Filefolder的self.file_list = []
#     for file in filelist:
#        FL.add_file(f.create_file(file))
#     return FL.file_list


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
    #把系统里的文件加入file_list
    # file_shili=server_file_init()
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
        self.ms=My_Mysql()
        self.file_all=self.ms.select_all_files()
    #获取list
    def list(self,foldername):
        #请求服务器内的文件，整理和文件列表和属性列表
        #op_file 是路径
        op_file=FIlE_PATH+foldername
        # if foldername==' ':
        #     fn=File_Folder(FIlE_PATH)
        # else:
        #     fn=File_Folder(FIlE_PATH+foldername+'/')
        data=self.file_all.to_list()
        #--------------------------------------------
        Q.put('l')
        Q.put(str(data).encode())
        # print(fn.get_file_list())
        

    #接受客户端下载请求，发送文件
    def send(self,filename):
        op_file=FIlE_PATH+filename
        print(op_file)
        #搜索系统是否有这个文件
        fd=self.ms.select_file_by_filename(filename)
        if fd==None:
            Q.put('d')
            Q.put('None')#不存在
        else:
            Q.put('d')
            #找到文件，并返回属性,以字符串形式
            f_property=fd.pack()
            Q.put(f_property)       
            with open(op_file,'rb') as f:
                while True:
                    data=f.read(2048)
                    # print(data)
                    Q.put(data)
                    if not data:
                        break    
            
    #接受客户端上传请求，接收文件
    def receive(self,filename):
        Q.put('u')
        Q.put(filename)
   
    #聊天
    def chat(self,message):
        #转发给其他客户端
        pass

    #登录
    def chat(self,message):
        #和mysql比对后返回
        pass


    #退出
    def quit(self):
        print("客户端退出")
        sys.exit(0)


