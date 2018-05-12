#静态网页处理器
#采用循环的模式，无法满足客户端长连接
from socket import *

HOST = ''
PORT = 9999
ADDR = (HOST,PORT)
def handler(_socket):
    request = _socket.recv(2048)
    # print(request)
    request_container = request.splitlines()
    for line in request_container:
        print (line)

    try:
        with open('示例.html','r') as file_obj:
            response = 'HTTP/1.1 200 OK\r\n'
            response += '\r\n'
            for i in file_obj:
                response += i
    except IOError:
        response = 'HTTP/1.1 404 not found\r\n'
        response += '\r\n'
        response += '====sory,file not find'
    finally:
        _socket.send(response.encode())
        _socket.close()


        
def main():  
    mysocket = socket()
    mysocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    mysocket.bind(ADDR)
    mysocket.listen(5)
    # while True:
    #     socket1,addr = mysocket.accept()
    #     handler(socket1)
    socket1,addr = mysocket.accept()
    handler(socket1)    


if __name__ == '__main__':
    main()