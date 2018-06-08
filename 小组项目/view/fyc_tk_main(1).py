import os
import sys
# if sys.version_info[0] == 2:
#     from Tkinter import *
#     from tkFont import Font
#     from ttk import *
#     #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
#     from tkMessageBox import *
#     #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
#     #import tkFileDialog
#     #import tkSimpleDialog
# else:  #Python 3.x
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
#import tkinter.filedialog as tkFileDialog
# import tkinter.simpledialog as tkSimpleDialog   #askstring()

import re


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Crazy Code")
        self.master.geometry('1280x800')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()
        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.03, rely=0.02,
                             relwidth=0.528, relheight=0.58)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, text='当前文件夹接口')
        self.TabStrip1__Tab1Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='文件列表')

        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text='用户操作记录接口.')
        self.TabStrip1__Tab2Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='用户操作记录')


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)


class Mybutton(tk.Label):
    def __init__(self, master, fun, **kwargs):
        super().__init__(master, kwargs)
        self.fun = fun
        self.config(fg='#555555')
        self.config(bg='#F8F8FF')
        self.config(takefocus=True)
        self.bind('<Button-1>', self.fun_button1)
        self.bind('<ButtonRelease-1>', self.fun_br1)
        self.bind('<Enter>', self.fun_enter)
        self.bind('<Leave>', self.fun_leave)


    def fun_enter(self, event):
        self.config(bg='#32CD32')
        self.config(fg='#FFFFFF')

    def fun_leave(self, event):
        self.config(bg='#F8F8FF')
        self.config(fg='#555555')

    def fun_button1(self, event):
        self.config(relief=tk.SUNKEN)
        self.fun()

    def fun_br1(self, event):
        self.config(relief=tk.FLAT)


class Myentry(tk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)
        self.config(highlightcolor='#32CD32', highlightthickness=2,
                    bd=0.5, relief=tk.FLAT, highlightbackground='#CCCCCC')


class Mybubble(tk.Frame):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, kwargs)
        self.text = text
        self.pack(fill=tk.BOTH, expand=1)
        imagefile = Image.open('resources/bubble_left.png')
        img = ImageTk.PhotoImage(imagefile)
        self.image_lable = tk.Label(self, image=img)
        self.image_lable.image = img
        self.image_lable.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.text_lable = tk.Label(self, text=self.text)
        self.text_lable.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class Mymenu(tk.Menu):
    def __init__(self, master, fun, **kwargs):
        super().__init__(master, kwargs)
        self.fun = fun

    # 	self.bind('<Button-1>',self.fun_button1)
    # 	self.bind('<ButtonRelease-1>',self.fun_br1)
    # 	self.bind('<Enter>',self.fun_enter)
    # 	self.bind('<Leave>',self.fun_leave)

    # def fun_button1(self,event):
    # 	self.config(relief = tk.SUNKEN)
    # 	self.fun()
    # def fun_br1(self,event):
    # 	self.config(relief = tk.FLAT)
    def hotkey(self, whole):
        d = {}
        d[whole] = "Alt+"+re.findall("[A-Z]", whole)[0]
        return d

    def add_menu(self, cascade, menu_name):
        self.filemenu = tk.Menu(self, tearoff=0)
        m = menu_name
        for k in cascade[:-1]:
            self.filemenu.add_command(
                label=k, command=self.fun, accelerator=self.hotkey(k)[k])
            self.filemenu.add_separator()
        j = cascade[-1]
        self.filemenu.add_command(
            label=j, command=self.fun, accelerator=self.hotkey(j)[j])
        self.add_cascade(label=m, menu=self.filemenu,
                         accelerator=self.hotkey(m)[m])


def hello():
    print("hello")


def main():

    # 画布
    root = tk.Tk()
    root.geometry("1280x800")
    root.resizable(width=True, height=True)

    menubar = Mymenu(root, hello)
    menubar.add_menu(
        ['上传本地文件  (Upload)', '下载文件到本地  (Dwload)', "退出  (Quit)"], "文件(F)")
    menubar.add_menu(["查看用户信息  (Info))",
                      "查看用户登录日志  (Log)", '查看文件详情  (Content)'], "查看(V)")
    menubar.add_menu(["更换壁纸  (W)", "字体设置  (P)"], "设置(S)")
    root['menu'] = menubar

    fr1 = LabelFrame(root, text='文件区')
    fr1.place(relx=0.03, rely=0.618, relwidth=0.528, relheight=0.369)

    # chat_input = tk.Text(root, borderwidth=3,highlightcolor="#32CD32", takefocus=False)
    # var.set("请输入聊天内容")
    #chat_input.place(relx=0.035, rely=0.65,relwidth=0.518, relheight=0.31)

    fr2 = LabelFrame(root, text='聊天区',takefocus=False)
    fr2.place(relx=0.603, rely=0.02, relwidth=0.382, relheight=0.967)

    # 聊天大厅
    histroy_talk = tk.Listbox(root)
    histroy_talk.place(relx=0.618, rely=0.06, relwidth=0.352, relheight=0.54)

    # l = tk.Label(root,text = '聊天',anchor = tk.W)
    # l.config(fg = '#555555')
    # l.config(font=("微软雅黑",15))
    # l.place(relx=0.61, rely=0.6,relheight=0.1,relwidth=0.1)
    # 当前活跃用户

    var = tk.Variable()
    chat = tk.Text(root)
    chat.config(font=("微软雅黑", 15),borderwidth=3,highlightcolor="#32CD32", highlightthickness=2,
        takefocus=False,relief=tk.FLAT, highlightbackground='#CCCCCC')

    # var.set("请输入聊天内容")
    chat.place(relx=0.618, rely=0.65, relwidth=0.352, relheight=0.264)

    b_withdraw = Mybutton(root, hello, text='撤回(Z)')
    b_withdraw.place(relx=0.83, rely=0.927, relwidth=0.06, relheight=0.045)

    b_send = Mybutton(root, hello, text='发送(S)')
    b_send.place(relx=0.91, rely=0.927, relwidth=0.06, relheight=0.045)

    Application(root).mainloop()
    root.mainloop()


if __name__ == "__main__":
    main()
