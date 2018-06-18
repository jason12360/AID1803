import re
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont 


class Mybutton(tk.Label):
	def __init__(self,master,fun,**kwargs):
		super().__init__(master,kwargs)
		self.fun = fun
		self.config(fg = '#555555')
		self.config(bg = '#F8F8FF')
		self.bind('<Button-1>',self.fun_button1)
		self.bind('<ButtonRelease-1>',self.fun_br1)
		self.bind('<Enter>',self.fun_enter)
		self.bind('<Leave>',self.fun_leave)
	def fun_enter(self,event):
		self.config(bg = '#32CD32')
		self.config(fg = '#FFFFFF')
	def fun_leave(self,event):
		self.config(bg = '#F8F8FF')
		self.config(fg = '#555555')
	def fun_button1(self,event):
		self.config(relief = tk.SUNKEN)
		self.fun()
	def fun_br1(self,event):
		self.config(relief = tk.FLAT)

class Myentry(tk.Entry):
	def __init__(self,master,**kwargs):
		super().__init__(master,kwargs)
		self.config(highlightcolor = '#32CD32',highlightthickness = 2,bd = 0.5,relief = tk.FLAT,highlightbackground='#CCCCCC')
class MyPasswordEntry(Myentry):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.config(show='*')
#继承此类,复写key方法,完成相应处理
class MySearchEntry(Myentry):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.bind('<Key>',self.key)
	def key(self,event):
		pass

class Mybubble(tk.Frame):
	def __init__(self,master,text,**kwargs):
		super().__init__(master,height=80,width=350)
		# self.pack_propagate(0)
		self.text = text
		self.pack(fill=tk.X)
		#用于测试,如果主函数调用则,使用下方图片路径,非主函数条用使用上方图片路径
		if __name__ !='__main__':
			photo = tk.PhotoImage(file='widgets_interface/resources/bubble.gif')
		else:
			photo = tk.PhotoImage(file='resources/bubble.gif')
		self.image_lable = tk.Label(self,image = photo,anchor=tk.W)
		self.image_lable.image = photo
		self.image_lable.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
		self.text_lable = tk.Label(self,anchor=tk.W,width=40)
		self.text_lable.config(bg='#FFFFFF',text = self.text)
		self.text_lable.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

class Scrollabe_Frame(tk.Canvas):
	def __init__(self,master,_width=1200,_height=20000,**kwargs):
		super().__init__(master,kwargs,width=_width)
		self.pack_propagate(0)
		self.frame=tk.Frame(self,width=_width,height=_height)
		self.frame.pack_propagate(0) 
		self.bar=tk.Scrollbar(self,orient=tk.VERTICAL) #竖直滚动条
		self.bar.config(command=self.yview)
		self.config(yscrollcommand=self.bar.set) 	
		self.create_window((0,0), window=self.frame,anchor=tk.NW)  #create_window

	def flush(self):
		self.delete(self.frame)
		self.frame=tk.Frame(self,width =1200)
		self.bar.config(command=self.yview)
		self.create_window((0,0), window=self.frame,anchor=tk.NW)

class Mymenu(tk.Menu):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)

    def hotkey(self, whole):
        d = {}
        d[whole] = "Alt+"+re.findall("[A-Z]", whole)[0]
        return d

    def add_menu(self, cas_dic, menu_name):
        self.cascade = tk.Menu(self, tearoff=0)
        m = menu_name
        for k, v in cas_dic.items():
            self.cascade.add_separator()
            h = self.hotkey(k)[k]
            self.cascade.add_command(label=k, command=v, accelerator=h)
        self.add_cascade(label=m, menu=self.cascade,accelerator=self.hotkey(m)[m])



class ListItems(Frame):
	def __init__(self,master,color,widths,textlist):
		super().__init__(master)
		self.color=color
		self.config(width=1000,height=50,bg=color)
		self.config(highlightbackground='#CCCCCC',highlightthickness=1)
		self.pack_propagate(0)
		self.pack(anchor=W)
		self.textlist=textlist
		self.labels=[]
		self.widths=iter(widths)
		self.create_labels()
		self.file_name = textlist[0]

	def bind_label(self,label):
		self.dwlabel = label
		self.bind('<Button-1>',self.dw)

	def dw(self,event):
		self.dwlabel.config(text=self.file_name)
		print(self.file_name)
		
	def actions(self):
		self.bind('<Enter>',self.selected)
		self.bind('<Leave>',self.leaved)
	def selected(self,event):
		self.config(bg='#EEEEEE')
		for label in self.labels:
			label.config(bg='#EEEEEE')
	def leaved(self,event):
		self.config(bg=self.color)
		for label in self.labels:
			label.config(bg=self.color)
	def create_labels(self):		
		for t in self.textlist:
			self.labels.append(Label(self,text=t,width=next(self.widths)))
		for label in self.labels:
			label.config(anchor=W)
			label.config(bg=self.color)
			label.pack(side=LEFT,padx=10)
			label.bind('<Button-1>',self.dw)


def fun1():
	print('hahahhah')
def main():
	top = tk.Tk()
	top.geometry('400x500')
	BIG_FONT = tkFont.Font(size = 20)
	se = MySearchEntry(top)
	se.pack()
	l = tk.Label(top,text = '用户名:',anchor = tk.W,width = 20,height =1,fg = '#555555')
	l.pack()
	e = Myentry(top)
	e.pack()
	e.focus_set()
	l = tk.Label(top,text = '密码:',anchor = tk.W,width = 20,height =1,fg = '#555555')
	l.pack()
	e = MyPasswordEntry(top)
	e.pack()
	b = Mybutton(top,fun1,text = '登录',width = 15,height =2)
	b.pack(pady = 10)
	# frame = tk.Frame(top)
	# frame.pack(fill=tk.X)
	# bubble = Mybubble(frame,'sajkd')
	# bubble.pack()
	s = Scrollabe_Frame(top,_width=400,_height=500
		,scrollregion=(0,0,400,2500))
	s.pack()
	s.bar.pack(side=tk.RIGHT, fill=tk.Y)
	text_list = ['python.py','4kb','/tarena/home/aid1803/tt/s','2018-9-14 23:00:00','2018-9-14 23:00:00']

	for i in range(100):

		file_displayer.ListItems(s.frame,text_list)
	


	top.wm_title('菜单')
	top.mainloop()

if __name__ == '__main__':
	main()