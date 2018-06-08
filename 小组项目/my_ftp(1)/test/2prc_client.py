from socket import *
from multiprocessing  import Process,Queue


def tcp_handler():
    PORT=18297
    HOST='0.0.0.0'
    ADDR=(HOST,PORT)
    client='0.0.0.0,18294'
    s=socket(AF_INET,SOCK_STREAM,0)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.connect(ADDR)
    s.send(client.encode())


def udp_handler():
    s=socket(AF_INET,SOCK_DGRAM,0)
    s.sendto(b'hello',('127.0.0.1',18294))
    print ('wating.....')
    data,addr=s.recvfrom(2048)
    print(data.decode())



th1=Process(target=tcp_handler)
th2=Process(target=udp_handler)

th1.start()
th2.start()

th1.join()
th2.join()