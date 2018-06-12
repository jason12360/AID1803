from tkinter import *


class ListItems(Frame):
	def __init__(self,master,textlist):
		super().__init__(master)
		self.config(width = 800,height=50,bg='#FFFFFF',highlightbackground='#CCCCCC',highlightthickness=1)
		self.bind('<Enter>',self.selected)
		self.bind('<Leave>',self.leaved)
		self.pack_propagate(0)
		self.pack()
		self.textlist=textlist
		self.labels=[]
		self.create_labels()

	def selected(self,event):
		self.config(bg='#EEEEEE')
		for label in self.labels:
			label.config(bg='#EEEEEE')
	def leaved(self,event):
		self.config(bg='#FFFFFF')
		for label in self.labels:
			label.config(bg='#FFFFFF')
	def create_labels(self):
		self.labels.append(Label(self,text=self.textlist[0],anchor=W,bg='#FFFFFF',width=10))
		self.labels.append(Label(self,text=self.textlist[1],anchor=W,bg='#FFFFFF',width=5))
		self.labels.append(Label(self,text=self.textlist[2],anchor=W,bg='#FFFFFF',width=30))
		self.labels.append(Label(self,text=self.textlist[3],anchor=W,bg='#FFFFFF',width=20))
		self.labels.append(Label(self,text=self.textlist[4],anchor=W,bg='#FFFFFF',width=20))
		for label in self.labels:
			label.pack(side=LEFT,padx=10)


# text_list = ['python.py','4kb','/tarena/home/aid1803/tt/s','2018-9-14 23:00:00','2018-9-14 23:00:00']
# first = ListItems(top,text_list)
# second = ListItems(top,text_list)
# third = ListItems(top,text_list)


