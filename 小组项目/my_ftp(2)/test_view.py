from tkinter import *
import client_class
import sys
class view():
    def __init__(self,server):
        self.server = server
        self.root = Tk()
        l = Label(self.root,text = '协议结构：请求类别 + 属性 + 内容 + 结束符')
        l.pack()
        e = Entry(self.root)
        self.e = e
        e.pack()
        b = Button(self.root,text = '提交',command=self.start)
        b.pack()
    def run(self):
        self.root.mainloop()

    def start(self):
        judge=client_class.comment_handler(self.e.get(),self.server)
        if judge==0:
            sys.exit(0)


            
