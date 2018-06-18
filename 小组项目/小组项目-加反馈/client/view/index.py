from tkinter import *
from widgets_interface.my_widgets import Scrollabe_Frame,Mybubble


class ChatView(Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.config(width=400, height=900, bd=1)
        self.pack(side=LEFT)
        self.pack_propagate(0)
        self.display()
        self.words = []

    def display(self):
        '''
        用来画聊天试图
        '''
        self.s = Scrollabe_Frame(self,_width=400,_height =500,scrollregion=(0,0,400,2000))
        self.t = Text(self)
        self.t.pack()
        # self.s.yview_moveto(1.0)
        b = Button(self,text = '发送',command=self.launch)
        b.pack()
    def launch(self):
        if len(self.words)>19:
            self.words.pop(0)
        self.words.append(self.t.get(1.0,END))
        self.s.flush()
        self.position = 0
        step = 0.05
        for word in self.words:
            Mybubble(self.s.frame,text=word).pack(pady=10)
            self.position+=step
        if self.position/step >5:
            self.s.yview_moveto(self.position-5*step)
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
