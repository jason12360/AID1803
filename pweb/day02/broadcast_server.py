from socket import *
from time import sleep

HOST = '<broadcast>'#或'<broadcast>'
PORT = 9999
ADDR = (HOST,PORT)

mysocket = socket(AF_INET,SOCK_DGRAM)
mysocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
mysocket.bind(('',9996))

while True:
    sleep(1)
    mysocket.sendto('坚决拥护习大大'.encode(),ADDR)
    print(mysocket.getsockname())
    data,addr = mysocket.recvfrom(1024)
    print('Received from %s:%s'%(addr,data.decode())) 