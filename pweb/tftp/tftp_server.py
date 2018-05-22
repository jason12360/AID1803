from socket import *
import os
import sys
import signal
import time

# 文件库位置
FILE_PATH = '/home/tarena/'


class TftpServer:
    def __init__(self, sockfd):
        self.conn = sockfd

    def list_file(self):
        file_list = os.listdir(FILE_PATH)
        if not file_list:
        	self.conn.send(b'N')
        	return
        else:
        	self.conn.send(b'Y')
        time.sleep(0.1)
        files = ''
        for filename in file_list:
        	#除去隐藏文件和文件夹
        	if filename[0] != '.' and os.path.isfile(FILE_PATH+filename):
        		files += filename + '#'
        self.conn.send(files.encode()) 

       #下载功能
    def download_file(self):
        filename = self.conn.recv(1024).decode()
        try:
        	with open(FILE_PATH + filename,'rb') as fileobj:
        		file_size = os.path.getsize(FILE_PATH + filename)
        		self.conn.send(('Y '+str(file_size)).encode())
        		time.sleep(0.1)
        		while True:
        			data = fileobj.read(1024)
        			if not data:
        				break
        			self.conn.send(data)

        except:
        	self.conn.send(b'N 0')
        	return

    def put_file(self, filename):
        file_info = self.conn.recv(1024).decode().split(' ')
        filename = file_info[0]
        file_size = file_info[1]
        with open(filename,'wb') as fileobj:
        	recved_size = 0
            while True:
                data = self.conn.recv(1024)
                fileobj.write(data)
                recved_size += 1024
                if recved_size >= file_size:
                    break
           



def main():
    if len(sys.argv) < 3:
        print('argv is error')
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024
    mysocket = socket()
    mysocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    mysocket.bind(ADDR)
    mysocket.listen(5)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        try:
            myconnection, addr = mysocket.accept()
        except KeyboardInterrupt:
            mysocket.close()
            sys.exit(0)
        except Exception:
            continue
        print('客户端登录：', addr)

        childpid = os.fork()
        if childpid < 0:
            print('创建子进程失败')
            myconnection.close()
            continue
        elif childpid == 0:
            mysocket.close()
            # 创建客户端通信对象
            tftp_server = TftpServer(myconnection)
            while True:
            	#接收客户端的请求类型
                data = myconnection.recv(BUFFERSIZE).decode()
                if data == 'L':
                    tftp_server.list_file()
                elif data == 'D':
                    tftp_server.download_file()
                elif data == 'U':
                    tftp_server.put_file()
                elif data == 'Q':
                    print('客户端退出：',myconnection.getpeername())
                    sys.exit(0)
        else:
            myconnection.close()
            continue


if __name__ == '__main__':
    main()
