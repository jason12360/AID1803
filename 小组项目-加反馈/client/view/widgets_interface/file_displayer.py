from tkinter import *

class ListItems(Frame):
	def __init__(self,master,color,textlist):
		super().__init__(master)
		self.color=color
		self.config(width =700,height=50,bg=color,highlightbackground='#CCCCCC',highlightthickness=1)
		self.pack_propagate(0)
		self.pack(anchor=W)
		self.textlist=textlist
		self.labels=[]
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
		#for t in self.textlist:
			#self.labels.append(Label(self,text=t,width=next(self.widths)))
		self.labels.append(Label(self,text=self.textlist[0],width=15))
		self.labels.append(Label(self,text=self.textlist[1],width=5))
		self.labels.append(Label(self,text=self.textlist[2],width=20))
		self.labels.append(Label(self,text=self.textlist[3],width=20))
		self.labels.append(Label(self,text=self.textlist[4],width=40))
		for label in self.labels:
			label.config(anchor=W)
			label.config(bg=self.color)
			label.pack(side=LEFT,padx=10)

