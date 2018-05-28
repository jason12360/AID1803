from tkinter import *
import tkinter.messagebox
from widgets_interface.dialog import Dialog
import login_handler
from view_exception import *


class Login_View(Dialog):
	def buttonbox(self):
		box = Frame(self)
		w = Button(box,text= '登录',width =10,command=self.login,default = ACTIVE)
		w.pack(side=TOP,padx = 5,pady = 5)
		w = Button(box,text= '注册',width =10,command=self.register)
		w.pack(side = BOTTOM,padx =5,pady = 5)

		self.bind('<Return>',self.login)
		self.bind('<Escape>',self.register)
		box.pack()

	def body(self,master):
		Label(master,text='用户名：').grid(row = 0)
		Label(master,text='密码：').grid(row = 2)

		self.e1 = Entry(master)
		self.e2 = Entry(master)

		self.e1.grid(row = 1)
		self.e2.grid(row = 3)
		return self.e1

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
	Button(root, text="Hello!").pack()
	root.update()

	d = Login_View(root) 
	root.wait_window(d.parent)

if __name__=='__main__':
	main()