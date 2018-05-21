# 客户端
# 	1.查看文件库中有那些文件
# 	2.选择其中的文件下载到本地
# 	3.将本地的文件上传到文件库
# 	4.多客户端同时操作
# tcp协议

from socket import *
import sys
import time


class TftpClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def list_file(self):
        # 发送请求类别
        self.sockfd.send(b'L')
        data = self.sockfd.recv(1024).decode()
        # 获取服务端回应
        if data == 'Y':
       		file_string = self.sockfd.recv(4096).decode()
        	files = file_string.split('#')
        	for file in files:
        		print(file)
        	print('文件列表展示完毕')
        else:
            print('请求文件列表失败')
        

    def get_file(self):
        self.sockfd.send(b'U')
        filename = input('请输入您要上传的文件')
        self.sockfd.send(filename.encode())

    def put_file(self):
        pass

    def quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit(0)


def show_menu():
    print('1.上传文件')
    print('2.下载文件')
    print('3.查看已有文件')
    print('4.退出程序')


def main():
    if len(sys.argv) < 3:
        print('argv is error')
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(ADDR)
    tftpclient = TftpClient(s)

    while True:
        show_menu()
        command = input('请输入你需要的操作：')
        if command == '1':
            tftpclient.put_file()
        elif command == '2':
            s.send(b'D')
            filename = input('请输入您要下载的文件')
            tftpclient.get_file()
        elif command == '3':
            tftpclient.list_file()

        elif command == '4':
            tftpclient.quit()



if __name__ == '__main__':
    main()
