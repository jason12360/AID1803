from socket import *

s = socket()
#套接字描述符
print(s.fileno())
#套接字类型
print(s.type)
s.bind(('127.0.0.1',8888))
#获取套接字绑定的地址
print(s.getsockname())
s.listen(5)
conn,addr = s.accept()
print(conn.getpeername())
