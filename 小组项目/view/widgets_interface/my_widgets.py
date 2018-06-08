import tkinter as tk
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
class Mybubble(tk.Frame):
	def __init__(self,master,text,**kwargs):
		super().__init__(master,height=80,width=350)
		# self.pack_propagate(0)
		self.text = text
		self.pack(fill=tk.X)
		photo = tk.PhotoImage(file='widgets_interface/resources/bubble.gif')
		#photo = tk.PhotoImage(file='resources/bubble.gif')
		self.image_lable = tk.Label(self,image = photo,anchor=tk.W)
		self.image_lable.image = photo
		self.image_lable.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
		self.text_lable = tk.Label(self,anchor=tk.W,width=40)
		self.text_lable.config(bg='#FFFFFF',text = self.text)
		self.text_lable.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

class Scrollabe_Frame(tk.Canvas):
	def __init__(self,master,_width,_height,**kwargs):
		super().__init__(master,kwargs,width = _width,height=_height)
		self.pack_propagate(0)
		self.pack()
		self.width = _width
		frame=tk.Frame(self,height=2000,width=_width)
		frame.pack_propagate(0) 
		vbar=tk.Scrollbar(self,orient=tk.VERTICAL) #竖直滚动条
		vbar.pack(side=tk.RIGHT, fill=tk.Y)
		vbar.config(command=self.yview)
		self.config(yscrollcommand=vbar.set) #设置  
		
		self.create_window((0,0), window=frame,anchor=tk.NW)  #create_window
		self.frame =frame
		self.bar = vbar
	def flush(self):
		self.delete(self.frame)
		self.frame=tk.Frame(self,width =self.width)
		self.create_window((0,0), window=self.frame,anchor=tk.NW)

		


def fun1():
	print('hahahhah')
def main():
	top = tk.Tk()
	top.geometry('400x500')
	BIG_FONT = tkFont.Font(size = 20)
	l = tk.Label(top,text = '用户名:',anchor = tk.W,width = 20,height =1,fg = '#555555')
	l.pack()
	e = Myentry(top)
	e.pack()
	e.focus_set()
	l = tk.Label(top,text = '密码:',anchor = tk.W,width = 20,height =1,fg = '#555555')
	l.pack()
	e = Myentry(top)
	e.pack()
	b = Mybutton(top,fun1,text = '登录',width = 15,height =2)
	b.pack(pady = 10)
	# frame = tk.Frame(top)
	# frame.pack(fill=tk.X)
	# bubble = Mybubble(frame,'sajkd')
	# bubble.pack()
	s = Scrollabe_Frame(top,_width=400,_height=500
		,scrollregion=(0,0,400,2500))


	for i in range(100):

		Mybubble(s.frame,text='测试').pack(fill=tk.X)
	


	top.wm_title('菜单')
	top.mainloop()

if __name__ == '__main__':
	main()