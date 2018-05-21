# 客户端 
# 	1.查看文件库中有那些文件
# 	2.选择其中的文件下载到本地
# 	3.将本地的文件上传到文件库
# 	4.多客户端同时操作
# tcp协议

from socket import *
import sys

def show_menu():
	print('1.上传文件')
	print('2.下载文件')
	print('3.查看已有文件')
	print('4.退出程序')
def list_file(socket):
	socket.send(b'L')
	file_string = socket.recv(1024)
	print(file_string.decode())


def main():
	if len(sys.argv) < 3:
		print('argv is error')
		return
	HOST = sys.argv[1]
	PORT = int(sys.argv[2])
	ADDR = (HOST,PORT)
	s = socket(AF_INET,SOCK_STREAM)
	s.connect(ADDR)
	show_menu()
	while True:
		command = input('请输入你需要的操作：')
		if command == '1':
			s.send(b'U')
		elif command == '2':
			s.send(b'D')
		elif command == '3':
			list_file(s)

		elif command == '4':
			s.send(b'Q')
			break

if __name__ == '__main__':
	main()
