'''
客户端
'''
import sys
import os
import my_protocol
from socket import *
from test_view import *
from multiprocessing import Queue
import time
import file
from file_folder import *
from database_handler import *
#创建队列
Q=Queue(2)

# 用户路径
file_path='/home/tarena/lwh/my_ftp/'
#download路径
file_path_d='/home/tarena/lwh/my_ftp/download/'

#控制端ｉｐ　和端口
ctrl_HOST='127.0.0.1'
ctrl_PORT=18527
ctrl_ADDR=(ctrl_HOST,ctrl_PORT)

#请求的服务器地址
server_addr=('127.0.0.1',18528)


#控制端
def control_port():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.connect(ctrl_ADDR)
    #创建客户端请求对象
    c_ftp=MyFtp_Client(s)
    while True:
        #界面
        #协议结构：请求类别 + 属性 + 内容 + 结束符
        # print('请求类别 + 属性 + 内容 + 结束符'
        # comment='list+'+str(client_add)+'+'+''+'+@end'
        view1 = view(c_ftp)
        view1.run()

#控制端--功能选择界面调用函数
def comment_handler(comment,c_ftp):  
    data=comment.split('+')
    if data[0]=="list":
        if not data[2]:
            #判断有没文件夹，没有，就发送list
            c_ftp.list_request()
        else:
            #data[2]is 文件夹,有酒发送list data[2]
            c_ftp.list_request(data[2])
        Q.put('l')
    elif data[0]=="upld":
        c_ftp.upload_request(data[2])
        Q.put('u')
        Q.put(data[2])
    elif data[0]=="dwld":
        c_ftp.download_request(data[2])
        Q.put('d')
        Q.put(data[2])
        #这两个功能只靠tcp---------------------------
    elif data[0]=='chat':
        #data[2]是聊天内容
        c_ftp.chat_request(data[2])
        #登录
    elif data[0]=="login":
        #data[1] 是账号
        #data[2] 是密码
        c_ftp.login_request(data[1],data[2])
        #---------------------------------------------
    
    elif data[0]=="quit":
        c_ftp.quit_request()
        return 0

    else:
        print("commond is not defined")



#数据端
def data_port():
    s= socket(AF_INET,SOCK_DGRAM)
    while True:
        T=Q.get()
        print(T)
        #继续监听，选择（数据端收）
        if T=='l':
            a=s.sendto(b'hello',server_addr)
            print(a)
            data,addr=s.recvfrom(1024)
            print(data.decode())
        
        elif T=='d':
            s.sendto(b'hello',server_addr)
            filename=Q.get()
            #接收属性
            f_property,addr=s.recvfrom(2048)
            print(f_property.decode())
            if f_property.decode()=='None':
                print("文件不存在")
            else:
                # 用户路径,下载，写入文件
                op_file=file_path_d+filename
                with open(op_file,'wb') as f:
                    while True:
                        data,addr=s.recvfrom(1024)
                        # print(data.decode())
                        if data==b'@end':
                            break
                        f.write(data)
                #--------接收完毕酒发送ｏｋ------
                s.sendto(b'ok',addr)
                print('下载成功')
                print("++++++++")


        #数据端发送
        elif T=='u':
            filename=Q.get()
            # print(filename)
            op_file=file_path+filename
            # 先判断文件名是否重名
            s.sendto(b'ok???',server_addr)
            ask,addr=s.recvfrom(1024)
            print(ask)
            if ask==b'go':
                with open(op_file,'rb') as f:
                    while True:
                        data=f.read(1024)
                        s.sendto(data,server_addr)
                        if not data:
                            break
                        # time.sleep(0.1)
                time.sleep(0.5)
                s.sendto(b'@end',server_addr)
                #------等待服务器回复----
                ask,addr=s.recvfrom(1024,10)
                if ask==b'ok':
                    print('上传完毕') 
                else:
                    print('上传失败') 
                print('------')
            else:
                print("文件在服务器上已存在(重名)")

        elif T=='q':
            sys.exit('数据端退出')
        
    

class  MyFtp_Client():
    def __init__(self,s):
        self.s=s

    def list_request(self,foldername=''):
        my_protocol.list_bale_TCP(self.s,foldername)

    def upload_request(self,filename):
        op_file=file_path+filename
        #打包发送
        my_protocol.upld_bale_TCP(self.s,filename)

    def download_request(self,filename):
        my_protocol.dwld_bale_TCP(self.s,filename)

    def chat_request(self,message):
        my_protocol.chat_bale_TCP(self.s,message)
  
    def login_request(self,admin,password):
        #tcp通信传给服务端数据库中的用户表比对,成功则登录
        #注：admin,password:必须为字符串
        my_protocol.login_request(self.s,admin,password)

    def quit_request(self):
        #通过协议打包发送
        my_protocol.quit_bale_TCP(self.s)
        Q.put('q')
        self.s.close()
        print("已退出")
  

def main():
    control_port()

if __name__ == '__main__':
    main()