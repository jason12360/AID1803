'''
文件传输协议
包头关键字 list  upld  dwld  quit  chat
结构：请求类别+属性+内容+结束符
list +null+foldername+@end  
dwld+size+filename+@end
upld + size +filename+@end
chat+null+message+@end
quit+null+null+@end
'''
BUFFERSIZE=4096

from socket import *
#打包TCP
def list_bale_TCP(conn,foldername):
    s='list+'+' '+'+'+foldername+'+@end'
    conn.send(s.encode())

def upld_bale_TCP(conn,filename):
    s='upld+'+' '+'+'+filename+'+@end'
    print(s)
    conn.send(s.encode())

def dwld_bale_TCP(conn,filename):
    s='dwld+'+' '+'+'+filename+'+@end'
    conn.send(s.encode())

def chat_bale_TCP(conn,message):
    s='chat+'+' '+'+'+message+'+@end'
    conn.send(s.encode())

def login_request(conn,admin,password):
    s='login+'+admin+'+'+password+'+@end'
    conn.send(s.encode())

def quit_bale_TCP(conn):
    s='quit+'+' '+'+'+' '+'+@end'
    # print(s)
    conn.send(s.encode())

#TCP解包
def unpake_TCP(connfd):
    #接收数据包
    data=connfd.recv(BUFFERSIZE).decode()
    #解释
    x=data.split('+')
    print(x)
    #判断头尾是否完整，不完整，则为丢包,完整就返回list
    if x[0] in ['list','upld','dwld','chat','quit','login','reg']:
        if x[3]=='@end':
            return x
        else:
            print('数据丢包')
            connfd.send("请求失败，数据包丢失".encode())
            #不再往下选择功能
            return -1            
    else:
        print('数据丢包')
        connfd.send("请求失败，数据包丢失".encode())
        return -1

#------------------------------------
#打包UDP
# def _bale_UDP(conn,data,addr):
#     s='list+'+str(len(data))+'+'+str(data)+'+@end'
#     conn.sendto(s.encode(),addr)

# #UDP解包
# def unpake_UDP(connfd):
#     #接收数据包
#     data,addr=connfd.recvfrom(BUFFERSIZE).decode()
#     #解释
#     x=data.split('+')
#     print(x)
#     #判断头尾是否完整，不完整，则为丢包,完整就返回list
#     if x[0] in ['list','upld','dwld','chat','quit']:
#         if x[3]=='@end':
#             #判断数据是否完整
#             if len(x[2])==int(x[1]):
#                 return x,addr
#             else:
#                 print('数据丢包')
#                 return -1
#         else:
#             print('数据丢包')
#             connfd.send("请求失败，数据包丢失".encode())
#             #不再往下选择功能
#             return -1            
#     else:
#         print('数据丢包')
#         connfd.send("请求失败，数据包丢失".encode())
#         return -1

