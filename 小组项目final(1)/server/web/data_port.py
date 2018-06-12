import time
import sys,os
from socket import *
if __name__=='main':
    import file
else:
    import model.file
# 服务器文件夹
SYS_FIlE_PATH= "/home/tarena/ftp_web(2)/"
#上传路径
SYS_FIlE_PATH_O= "/home/tarena/ftp_web(2)/op/"

def run(op,addr,filename):
    DATA_HOST = addr[0]
    print(DATA_HOST)
    DATA_PORT = 18528
    DATA_ADDR = (DATA_HOST, DATA_PORT)
    conn = socket()
    conn.connect(DATA_ADDR)
    #等待客户端的数据段请求过来
    # conn,addr=s.accept()
	#通过套接字做相应处理
    if op=='d':
        #路径选择
        op_path=SYS_FIlE_PATH+filename      
        with open(op_path,'rb') as f:
            while True:
                data=f.read(1024)
                if not data:
                    break 
                conn.send(data)
        time.sleep(0.1)
        conn.send(b'@end')
        ask=conn.recv(1024,10)
        if ask==b'ok':
            print('用户接受完毕') 
        else:
            print('用户接受失败')
    elif op=='u': 
        #接收文件到服务器
        #路径选择
        op_path=SYS_FIlE_PATH_O+filename      
        with open(op_path,'wb') as f:
            while True:
                data=conn.recv(1024)
                if data==b'@end':
                    break
                f.write(data)
        time.sleep(0.1)
        #接收完成发送ok
        conn.send(b'ok')
        print('用户上传完成')

    # #关闭套接字
    conn.close()
