from tkinter import *
import login_handler
import tkinter.messagebox
from widgets_interface.dialog import Dialog
from view_exception import *


class Register_View(Dialog):
	def buttonbox(self):
		box = Frame(self)
		w = Button(box,text= '确认注册',width =10,command=self.register,default = ACTIVE)
		w.pack(side=LEFT,padx = 5,pady = 5)
		w = Button(box,text= '放弃注册',width =10,command=self.cancel)
		w.pack(side = LEFT,padx =5,pady = 5)

		self.bind('<Return>',self.register)
		self.bind('<Escape>',self.cancel)
		box.pack()

	def body(self,master):
		Label(master,text='用户名：').grid(row = 0)
		Label(master,text='密码：').grid(row = 1)
		Label(master,text='确认密码：').grid(row = 2)

		self.e1 = Entry(master)
		self.e2 = Entry(master)
		self.e3 = Entry(master)

		self.e1.grid(row = 0,column =1)
		self.e2.grid(row = 1,column = 1)
		self.e3.grid(row = 2,column = 1)
		return self.e1

	def register(self,event = None):
		register_handler.do_register(self)
		
	def cancel(self,event = None):
		self.destroy()
		self.parent.destroy()