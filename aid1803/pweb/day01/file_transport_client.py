from socket import *
# TCP客户端
# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
# 发起连接
sockfd.connect(('176.122.16.186', 9999))
# 发送消息


filename_ = sockfd.recv(1024).decode()
filename = input('请输入问件保存的位置:')
_filename = filename + filename_
with open(_filename, 'ab') as file_obj:
    while True:
        data = sockfd.recv(1024)
        if not data:
            break
        file_obj.write(data)
        # print(data)

sockfd.close()
