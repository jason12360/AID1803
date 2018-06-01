from tkinter import *
import tkinter.font as tkFont  
import tkinter.messagebox
from widgets_interface.view_block import Block
from widgets_interface.my_widgets import Mybutton,Myentry
import login_handler
from view_exception import *


class Login_View(Block):
	def __init__(self,parent,font):
		self.font = font
		super().__init__(parent)
	def buttonbox(self):
		box = Frame(self)
		w = Mybutton(box,text= '登录',width =20,fun=self.login,font = self.font)
		w.pack(side=TOP,padx = 5,pady = 5)
		w = Mybutton(box,text= '注册',width =20,fun=self.register,font = self.font)
		w.pack(side = BOTTOM,padx =5,pady = 5)

		self.bind('<Return>',self.login)
		self.bind('<Escape>',self.register)
		box.place(relx=0.5,rely =0.8,anchor=CENTER)

	def body(self):
		body = Frame(self)
		Label(body,font = self.font,text='用户名：',fg = '#555555',anchor = W,width = 20).grid(row = 0)
		Label(body,font = self.font,text='密码：',fg = '#555555',anchor = W,width = 20).grid(row = 2)

		self.e1 = Myentry(body,font = self.font)
		self.e2 = Myentry(body,font = self.font)

		self.e1.grid(row = 1)
		self.e2.grid(row = 3)
		body.place(relx=0.5,rely =0.3,anchor=CENTER)

	def login(self,event = None):
		login_handler.do_login(self)
		
	def register(self,event = None):
		login_handler.do_register(self)
	def cancel(self,event = None):
		pass

#用来测试：
def main():
	root = Tk()
	root.geometry('800x600')
	root.resizable(width=False,height=True)
	root.config(bg = '#333333')
	ftext = Frame(root)
	ftext.config(bg = '#333333')
	ft_header = tkFont.Font(size = 60,weight=tkFont.BOLD)
	ft_text = tkFont.Font(size = 15)
	l = Label(ftext,text = '疯狂码头',fg = '#EEEEEE',bg='#333333',font = ft_header)
	l.pack()
	l1 = Label(ftext,justify = LEFT,text = '一个简易的中期项目，在这里你可以上传\n下载你上课的笔记和代码，并可以和你的\n组员一起聊天',font = ft_text,fg = '#EEEEEE',bg='#333333')
	l1.pack()
	ftext.place(relx=0.3,rely =0.45,anchor=CENTER)
	d = Login_View(root,ft_text) 
	d.config(height = 300,width =300)
	d.place(relx=0.75,rely =0.5, anchor=CENTER)
	root.mainloop()


if __name__=='__main__':
	main()