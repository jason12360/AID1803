# 客户端
#     1.查看文件库中有那些文件
#     2.选择其中的文件下载到本地
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
        

    def download_file(self):
        self.sockfd.send(b'D')
        filename = input('请输入您要下载的文件')
        self.sockfd.send(filename.encode())
        data = self.sockfd.recv(1024).decode().split(' ')
        sent_able = data[0]
        file_size = int(data[1])
        time.sleep(0.1)
        if sent_able == 'Y':
            with open(filename,'wb') as fileobj:
                recved_size = 0
                while True:
                    data = self.sockfd.recv(1024)
                    fileobj.write(data)
                    recved_size += 1024
                    print('已下载%.2f%%'%((recved_size/file_size)*100),end = '\r')
                    if recved_size >= file_size:
                        break
                print('\n%s下载接收完毕'%filename)

        else:
            print('下载文件失败')


    def put_file(self):
        self.sockfd.send(b'U')
        filename = input('请输入您要上传的文件')
        try:
        	with open(filename,'rb') as fileobj:
        		file_size = os.path.getsize(filename)
        		file_info = filename +' ' + str(filesize)
        		self.sockfd.send(fileinfo.encode())
        		time.sleep(0.1)
        		while True:
        			data = fileobj.read(1024)
        			if not data:
        				break
        			self.sockfd.send(data)
        		 print('\n%s上传完毕'%filename)
        except:
        	print('上传文件失败')
        


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
           
            tftpclient.download_file()
        elif command == '3':
            tftpclient.list_file()

        elif command == '4':
            tftpclient.quit()



if __name__ == '__main__':
    main()
