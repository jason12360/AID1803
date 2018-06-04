from tkinter import *
from widgets_interface.my_widgets import Scrollabe_Frame


class ChatView(Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.config(width=400, height=900, bd=1)
        self.pack(side=LEFT)
        self.pack_propagate(0)
        self.display()

    def display(self):
        '''
        用来画聊天试图
        '''
        self.s = Scrollabe_Frame(self,_width=400,_height =500,scrollregion=(0,0,520,520))
        self.s.pack()
        l = Label(self, text='这是一个聊天视图')
        l.pack()
        self.t = Text(self)
        self.t.pack()
        b = Button(self,text = '发送',command=self.launch)
        b.pack()
    def launch(self):
    	Label(self.s.frame,text = self.t.get(1.0,END),width=400,anchor=W).pack()
    	self.t.delete(1.0,END)


class MainView(Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.config(width=800, height=900, bd=1, bg='#FFFFFF')
        self.pack(side=RIGHT)
        self.pack_propagate(0)
        self.display()

    def display(self):
        '''
        用来画聊天试图
        '''
        l = Label(self, text='这是主视图')
        l.pack()


root = Tk()
root.geometry('1200x900')
root.resizable(width=False, height=True)
main_view = MainView(root)


chat_view = ChatView(root)

root.mainloop()
