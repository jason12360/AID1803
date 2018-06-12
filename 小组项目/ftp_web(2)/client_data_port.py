import time
import file
import sys,os
from socket import *
DATA_HOST = ''
DATA_PORT = 18528
DATA_ADDR = (DATA_HOST, DATA_PORT)
SYS_FIlE_PATH= "/home/tarena/ftp_web/op/"

def run(op,_socket,filename):
    _socket.listen(10)
    #等待服务端连接
    s,addr = _socket.accept()
    #通过套接字做相应处理
    if op=='u':
        #路径选择
        op_path=SYS_FIlE_PATH+filename      
        with open(op_path,'rb') as f:
            while True:
                data=f.read(2048)
                if not data:
                    break 
                s.send(data)
        time.sleep(0.1)
        s.send(b'@end')
        if ask==b'ok':
            print('上传成功') 
        else:
            print('上传失败')
    elif op=='d': 
        #接收文件(用户的下载)
        #路径选择
        op_path=SYS_FIlE_PATH+filename      
        with open(op_path,'wb') as f:
            while True:
                data=s.recv(1024)
                if data==b'@end':
                    break
                f.write(data)
        time.sleep(0.1)
        #下载完成发送ok
        s.send(b'ok')
        print('下载完成')
    # #关闭套接字
    s.close()
    
  



