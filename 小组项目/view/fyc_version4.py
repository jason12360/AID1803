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
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter.ttk import *
import tkinter.filedialog
from tkinter.messagebox import *
from widgets_interface.my_widgets import *
# import tkinter.simpledialog as tkSimpleDialog   #askstring()

import re


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None,**kwargs):
        Frame.__init__(self, master)
        self.createNotebook()
        #self.createButton(button_place,button_fun)
        self.createEntry()
        self.createChat()
        self.createImg()


    def createNotebook(self):
        self.top = self.winfo_toplevel()
        self.style = Style()

        #两个标签页，我还没来得及,抽出来当类，这个我自己来

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.03, rely=0.05,relwidth=0.528, relheight=0.55)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
    

        #这个列表到时候替换成 File类 select结果    动态更新！！
        tmp_list=["文件名","文件大小","储存路径","修改时间","创建时间"]
        for i in range(1,9):
            for j in range(5):
                self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, text=tmp_list[j-1]+str(i))
                self.TabStrip1__Tab1Lbl.place(relx=0.2*j, rely=0.05+0.1*i,relwidth=0.15)

        self.TabStrip1.add(self.TabStrip1__Tab1, text='   服务器文件仓储   ')


        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        tmp_list=["用户编号","文件编号","操作类型"]
        for i in range(1,9):
            for j in range(3):
                self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text=tmp_list[j-1]+str(i))
                self.TabStrip1__Tab2Lbl.place(relx=0.2*j, rely=0.05+0.1*i,relwidth=0.15)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='   用户操作记录   ')

    def createButton(self,button_place,button_fun):
        for k,v in button_place:
            self.button=Mybutton(self.top,button_fun[k],text=k)
            self.button.place(**v)
    def createEntry(self):
        e=Myentry(self.top)
        e.place(relx=0.33, rely=0.028, relwidth=0.228, relheight=0.048)
    def createChat(self):
        var = tk.Variable() 
        chat = tk.Text(self.top)
        chat.config(font=("微软雅黑", 15),borderwidth=3,highlightcolor="#32CD32", highlightthickness=2,
        relief=tk.FLAT, highlightbackground='#CCCCCC')
        # var.set("请输入聊天内容")
        chat.place(relx=0.618, rely=0.65, relwidth=0.352, relheight=0.264)
    def createImg(self):
        l5=Label(self.top,text="图")
        l5.place(relx=0.036, rely=0.666, relwidth=0.015, relheight=0.029)





class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)




#我在张晋的Mybotton类下添加了一个 def Uploadfile

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

    def Uploadfile(self):
        self.filename=tkinter.filedialog.askopenfilename(filetypes=[("py格式", "py")])
        print(self.filename)
        return self.filename


# 菜单栏 已经快捷键设置

class Mymenu(tk.Menu):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)

    def hotkey(self, whole):
        d = {}
        d[whole] = "Alt+"+re.findall("[A-Z]", whole)[0]
        return d

    def add_menu(self, cas_dic,menu_name):
        self.cascade = tk.Menu(self, tearoff=0)
        m = menu_name
        for k,v in cas_dic.items():
            self.cascade.add_separator()
            h=self.hotkey(k)[k]
            print(k,v,h)
            self.cascade.add_command(label=k, command=v, accelerator=h)

        self.add_cascade(label=m, menu=self.cascade,
                         accelerator=self.hotkey(m)[m])




#菜单栏 / 按钮 绑定的一大堆测试函数，到时候替换成你们的接口


def hellou():
    print("hellou")
def hellod():
    print("hellod")
def helloq():
    print("helloq")
def hellof():
    print("hellof")
def helloi():
    print("helloi")
def hellol():
    print("hellol")
def helloc():
    print("helloc")
def hellov():
    print("hellov")
def hellow():
    print("hellow")
def hellop():
    print("hellop")
def helloa():
    print("helloa")
def hello():
    print("hello")
def hellou():
    print("hellou")
def helloz():
    print("helloz")
def hellos():
    print("hellos")
def helloo():
    print("helloo")



def main():

    # 画布
    root = tk.Tk()
    root.geometry("1280x800")
    root.resizable(width=True, height=True)
    #root.attributes("-alpha",0.9)

    #  画布可以插底图， 我先注释掉
    # img=PhotoImage(file="E:\\Fäniz\\小组项目\\marong.png")
    # w=Label(root,text="abc",image=img)
    # w.place(relx=0,rely=0,relwidth=0.02,relheight=1)



    menubar = Mymenu(root)
    #生成菜单栏，后面我会抽成 字典嵌套

    fmenu={'上传本地文件  (Upload)':hellou,'下载文件到本地  (Dwload)':hellod,"退出  (Quit)":helloq}
    vmenu={"查看用户信息  (Info))":helloi,"查看用户登录日志  (Log)":hellol,'查看文件详情  (Content)':helloc}
    smenu={"更换壁纸  (W)":hellow,"字体设置  (P)":hellop,"进度条样式(Y)":hello,"关于 (A)":helloa}
    menubar.add_menu(fmenu, "文件(F)")
    menubar.add_menu(vmenu, "查看(V)")
    menubar.add_menu(smenu, "界面设置(S)")
    root['menu'] = menubar


    #命名有点乱，明天我会统一对控件进行编号，  这里面是有堆叠顺序的
    #你们暂时需要哪个控件的接口，先按照功能 Ctrl+F5 查找



    #各种框，不需要接口
    fr1 = LabelFrame(root, text='上传文件')
    fr1.place(relx=0.03, rely=0.618, relwidth=0.314, relheight=0.369)

    fr6 = LabelFrame(root, text='')
    fr6.place(relx=0.063, rely=0.649, relwidth=0.204, relheight=0.061)

    fr2 = LabelFrame(root, text='聊天区')
    #fr2.config(font=("微软雅黑",15))　　　　,takefocus=False
    fr2.place(relx=0.603, rely=0.02, relwidth=0.382, relheight=0.967)



    # 当前活跃用户
    l13=Label(root,text="在线用户列表")
    l13.place(relx=0.367, rely=0.614, relwidth=0.15, relheight=0.029)

    lb4 = Listbox(root)
    lb4.place(relx=0.37, rely=0.65, relwidth=0.188, relheight=0.337)    
    



    # 聊天大厅， 替换成张晋的气泡滚动条
    histroy_talk = tk.Listbox(root)
    histroy_talk.place(relx=0.618, rely=0.06, relwidth=0.352, relheight=0.54)



    #聊天输入框

   



    #  各种按钮     等你们的接口~
    aAAAAA='''
    button_dic={

        '浏览 (L)':{relx:0.274, rely:0.666, relwidth:0.06, relheight:0.045},
        '上传 (U)':{relx:0.274, rely:0.927, relwidth:0.06, relheight:0.045},
        '撤回(Z)':{relx:0.83, rely:0.927, relwidth:0.06, relheight:0.045},
        '发送(S)':{relx:0.91, rely:0.927, relwidth:0.06, relheight:0.045}

    }
    button_fun={
        '浏览 (L)':hellol,
        '上传 (U)':hellou,
        '撤回(Z)':helloz,
        '发送(S)':hellos,
    }
    '''


    b_overlook=Mybutton(root,helloo,text='浏览 (L)')
    b_overlook.place(relx=0.274, rely=0.666, relwidth=0.06, relheight=0.045)

    b_upload = Mybutton(root, hello, text='上传 (U)')
    b_upload.place(relx=0.274, rely=0.927, relwidth=0.06, relheight=0.045)
    
    b_withdraw = Mybutton(root, hello, text='撤回(Z)')
    b_withdraw.place(relx=0.83, rely=0.927, relwidth=0.06, relheight=0.045)

    b_send = Mybutton(root, hello, text='发送(S)')
    b_send.place(relx=0.91, rely=0.927, relwidth=0.06, relheight=0.045)



    b_filename="哈哈哈哈哈哈哈哈"
    print(b_filename)
   #下面全是占位符，我们确定好上传文件个数，就可以抽成动态循环


    l6=Label(root,text=b_filename)
    l6.place(relx=0.065, rely=0.665, relwidth=0.142, relheight=0.040)
    l7=Label(root,text="正在上传:  "+b_filename)
    l7.place(relx=0.035, rely=0.725, relwidth=0.242, relheight=0.040)
    l8=Label(root,text="正在上传:  "+b_filename)
    l8.place(relx=0.035, rely=0.765, relwidth=0.242, relheight=0.040)
    l9=Label(root,text="正在上传:  "+b_filename)
    l9.place(relx=0.035, rely=0.805, relwidth=0.242, relheight=0.040)
    l10=Label(root,text=chr(9989)+chr(9993)+"进度条进度条进度条进度条进度条进度条进度条进20%")
    l10.place(relx=0.035, rely=0.855, relwidth=0.242, relheight=0.040)
    l11=Label(root,text="上传完毕")
    l11.place(relx=0.035, rely=0.915, relwidth=0.142, relheight=0.040)

    Application(root).mainloop()
    root.mainloop()


if __name__ == "__main__":
    main()
