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
from tkinter import messagebox
from view.widgets_interface.my_widgets import *
# import tkinter.simpledialog as tkSimpleDialog   #askstring()
import re


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master)
        self.createNotebook()
        self.createLableFrame()
        self.createButton()
        self.createEntry()
        self.radioButtom()
        self.createChat()
        self.createImg()
        self.createMenu()
        self.createLabel()

    def createNotebook(self):
        self.top = self.winfo_toplevel()
        self.style = Style()
        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.03, rely=0.05,
                             relwidth=0.528, relheight=0.55)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        tmp_list = ["文件名", "文件大小", "储存路径", "修改时间", "创建时间"]

        
        for i in range(1, 9):
            for j in range(5):
                self.TabStrip1__Tab1Lbl = Label(
                    self.TabStrip1__Tab1, text=tmp_list[j]+str(i))
                self.TabStrip1__Tab1Lbl.place(
                    relx=0.2*j, rely=0.05+0.1*i, relwidth=0.15)

        self.TabStrip1.add(self.TabStrip1__Tab1, text='   服务器文件仓储   ')
        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        tmp_list = ["用户编号", "文件编号", "操作类型"]
        for i in range(1, 9):
            for j in range(3):
                self.TabStrip1__Tab2Lbl = Label(
                    self.TabStrip1__Tab2, text=tmp_list[j]+str(i))
                self.TabStrip1__Tab2Lbl.place(
                    relx=0.3*j, rely=0.05+0.1*i, relwidth=0.15)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='   用户操作记录   ')

    def createLableFrame(self):
        frame_dic = {
            '上传文件': {"relx": 0.03, "rely": 0.618, "relwidth": 0.314, "relheight": 0.369},
            '': {"relx": 0.063, "rely": 0.649, "relwidth": 0.204, "relheight": 0.061},
            '聊天区': {"relx": 0.603, "rely": 0.02, "relwidth": 0.382, "relheight": 0.967}
        }

        for k, v in frame_dic.items():
            fr = LabelFrame(self.top, text=k)
            fr.place(**v)

    def createButton(self):
        button_place = {
            '浏览 (L)': {"relx": 0.274, "rely": 0.666, "relwidth": 0.06, "relheight": 0.045},
            '上传 (U)': {"relx": 0.274, "rely": 0.927, "relwidth": 0.06, "relheight": 0.045},
            '撤回(Z)': {"relx": 0.83, "rely": 0.927, "relwidth": 0.06, "relheight": 0.045},
            '发送(S)': {"relx": 0.91, "rely": 0.927, "relwidth": 0.06, "relheight": 0.045}
        }
        button_fun = {'浏览 (L)': show_up_filedialog, '上传 (U)': hellou,
                      '撤回(Z)': helloz, '发送(S)': hellos}

        for k, v in button_place.items():
            self.button = Mybutton(self.top, button_fun[k], text=k)
            self.button.place(**v)

    def createEntry(self):
        e = Myentry(self.top)
        e.place(relx=0.33, rely=0.028, relwidth=0.228, relheight=0.048)

    def createChat(self):
        var = tk.Variable()
        chat = tk.Text(self.top)
        chat.config(font=("微软雅黑", 15), borderwidth=3, highlightcolor="#32CD32", highlightthickness=2,
                    relief=tk.FLAT, highlightbackground='#CCCCCC')
        # var.set("请输入聊天内容")
        chat.place(relx=0.618, rely=0.65, relwidth=0.352, relheight=0.264)

    def createImg(self):
        l5 = Label(self.top, text="图")
        l5.place(relx=0.036, rely=0.666, relwidth=0.015, relheight=0.029)

    def radioButtom(self):
        v = IntVar()
        v.set(1)
        r1 = Radiobutton(self.top, variable=v, text="显示所有", value=1)
        r1.place(relx=0.23, rely=0.028, relwidth=0.068, relheight=0.048)
        r2 = Radiobutton(self.top, variable=v, text="模糊匹配", value=2)
        r2.place(relx=0.28, rely=0.028, relwidth=0.068, relheight=0.048)

    def createLabel(self):

        b_filename = "哈哈哈哈哈哈哈哈"
        print(b_filename)

        l13 = Label(self.top, text="在线用户列表")
        l13.place(relx=0.367, rely=0.614, relwidth=0.15, relheight=0.029)

        l6 = Label(self.top, text=b_filename)
        l6.place(relx=0.065, rely=0.665, relwidth=0.142, relheight=0.040)
        l7 = Label(self.top, text="正在上传:  "+b_filename)
        l7.place(relx=0.035, rely=0.725, relwidth=0.242, relheight=0.040)
        l8 = Label(self.top, text="正在上传:  "+b_filename)
        l8.place(relx=0.035, rely=0.765, relwidth=0.242, relheight=0.040)
        l9 = Label(self.top, text="正在上传:  "+b_filename)
        l9.place(relx=0.035, rely=0.805, relwidth=0.242, relheight=0.040)
        l10 = Label(self.top, text=chr(9989)+chr(9993) +
                    "进度条进度条进度条进度条进度条进度条进度条进20%")
        l10.place(relx=0.035, rely=0.855, relwidth=0.242, relheight=0.040)
        l11 = Label(self.top, text="上传完毕")
        l11.place(relx=0.035, rely=0.915, relwidth=0.142, relheight=0.040)

    def createMenu(self):
        menubar = Mymenu(self.top)
        menu_dic = {
            "文件(F)": {'上传本地文件  (Upload)': hellou,
                      '下载文件到本地  (Dwload)':show_dw_filedialog, "退出  (Quit)": helloq},
            "查看(V)": {"查看用户信息  (Info))": helloi,
                      "查看用户登录日志  (Log)": hellol, '查看文件详情  (Content)': helloc},
            "界面设置(S)": {"更换壁纸  (W)": show_ask_filedialog, "字体设置  (P)": hellop,
                        "进度条样式(Y)": hello, "关于 (A)": help_about}
        }

        for k, v in menu_dic.items():
            menubar.add_menu(v, k)
        self.top['menu'] = menubar


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None, **kwargs):
        Application_ui.__init__(self, master, **kwargs)


# 我在张晋的Mybotton类下添加了一个 def Uploadfile

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
        self.filename = tkinter.filedialog.askopenfilename(
            filetypes=[("py格式", "*.py*")])
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

    def add_menu(self, cas_dic, menu_name):
        self.cascade = tk.Menu(self, tearoff=0)
        m = menu_name
        for k, v in cas_dic.items():
            self.cascade.add_separator()
            h = self.hotkey(k)[k]
            print(k, v, h)
            self.cascade.add_command(label=k, command=v, accelerator=h)

        self.add_cascade(label=m, menu=self.cascade,
                         accelerator=self.hotkey(m)[m])


# 菜单栏 / 按钮 绑定的一大堆测试函数，到时候替换成你们的接口

def show_up_filedialog():
    fileN = tkinter.filedialog.askopenfilename(initialdir=os.path.abspath("fyc_version5"),
        filetypes=[("py格式", ".py")])
    print(fileN)
    return fileN

def show_dw_filedialog():
    fileN = tkinter.filedialog.asksaveasfilename(
        filetypes=[("py格式", ".py")])
    print(fileN)
    return fileN
def show_ask_filedialog():
    fileN = tkinter.filedialog.askdirectory(filetypes=[("py格式", ".py")])
    print(fileN)
    return fileN
# def show_error(string)

def help_about():
    messagebox.showinfo('关于', ' 团队：疯狂码头 \n 成员:张晋 李文辉 方毅超 刘章杰 谭锐锋 谭永权 杨凌枫 \n verion 1.0 \n 感谢您的使用！ \n @2018 ')  # 弹出消息提示框
        
    










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
    # root.attributes("-alpha",0.9)

    #  画布可以插底图， 我先注释掉
    # img=PhotoImage(file="E:\\Fäniz\\小组项目\\marong.png")
    # w=Label(root,text="abc",image=img)
    # w.place(relx=0,rely=0,relwidth=0.02,relheight=1)


    user_test=["用户"+str(iii) for iii in range(1,20)]
    
    scrollbar_online = Scrollbar(root, orient=VERTICAL)
    listbox_online=Listbox(root, yscrollcommand=scrollbar_online.set, selectmode=EXTENDED)
    scrollbar_online.config(command=listbox_online.yview)
    scrollbar_online.pack(side=RIGHT, expand=True, fill=Y)
    listbox_online.place(relx=0.37, rely=0.65, relwidth=0.188, relheight=0.337)
    #scrollbar_online.place(relx=0.57, rely=0.65, relwidth=0.088, relheight=0.337)

    for fs in user_test:
        listbox_online.insert(END, fs)
        #listbox_online.bind("<Double-Button-1>", selectFontsize)
        listbox_online.select_set(user_test.index("用户1"))
        listbox_online.see(user_test.index("用户1"))
        #listbox_online.grid(row=0, column=2, sticky=NE, padx=10, pady=10)





    # 聊天大厅， 替换成张晋的气泡滚动条
    histroy_talk = Listbox(root)
    histroy_talk.place(relx=0.618, rely=0.06, relwidth=0.352, relheight=0.54)

    Application(root).mainloop()

    root.mainloop()


if __name__ == "__main__":
    main()
