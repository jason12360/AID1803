from tkinter import *
import login_handler
import tkinter.messagebox
from widgets_interface.view_block import Block
from widgets_interface.my_widgets import Mybutton,Myentry
from view_exception import *


class Register_View(Block):
	def __init__(self,parent,font):
		self.font = font
		super().__init__(parent)
	def buttonbox(self):
		box = Frame(self)
		w = Mybutton(box,font = self.font,text= '确认注册',width =20,fun=self.register)
		w.pack(side=TOP,padx = 5,pady = 5)
		w = Mybutton(box,font = self.font,text= '放弃注册',width =20,fun=self.cancel)
		w.pack(side = BOTTOM,padx =5,pady = 5)

		self.bind('<Return>',self.register)
		self.bind('<Escape>',self.cancel)
		box.place(relx=0.5,rely =0.85,anchor=CENTER)

	def body(self):
		body = Frame(self)
		Label(body,font = self.font,text='用户名：',fg = '#555555',anchor = W,width = 20).grid(row = 0)
		Label(body,font = self.font,text='密码：',fg = '#555555',anchor = W,width = 20).grid(row = 2)
		Label(body,font = self.font,text='确认密码：',fg = '#555555',anchor = W,width = 20).grid(row = 4)

		self.e1 = Myentry(body,font = self.font)
		self.e2 = Myentry(body,font = self.font)
		self.e3 = Myentry(body,font = self.font)

		self.e1.grid(row = 1,column = 0)
		self.e2.grid(row = 3,column = 0)
		self.e3.grid(row = 5,column = 0)
		body.place(relx=0.5,rely =0.35,anchor=CENTER)

	def register(self,event = None):
		register_handler.do_register(self)
		
	def cancel(self,event = None):
		self.destroy()
		self.parent.destroy()