from socket import *
from multiprocessing  import Process,Queue


def tcp_handler():
    PORT=18297
    HOST='127.0.0.1'
    ADDR=(HOST,PORT)
    s=socket(AF_INET,SOCK_STREAM,0)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    print ("waiting")
    c,addr=s.accept()
    data=c.recv(2048).decode()
    print(data)
    
    q.put(data)
    s.close()
    	

def udp_handler():
    PORT=18294
    HOST='127.0.0.1'
    ADDR=(HOST,PORT)
    s=socket(AF_INET,SOCK_DGRAM,0)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    data=q.get()
    # c_addr=data.split(',')[0]
    # c_port=data.split(',')[1]
    # addr=(c_addr,int(c_port))
    # print (addr)
    data,addr=s.recvfrom(2048)
    print(data,addr)
    s.sendto(b'hello',addr)
    s.close()



q=Queue()
th1=Process(target=tcp_handler)
th2=Process(target=udp_handler)

th1.start()
th2.start()

th1.join()
th2.join()