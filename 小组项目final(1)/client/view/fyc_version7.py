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
from view.widgets_interface.file_displayer import *
# import tkinter.simpledialog as tkSimpleDialog   #askstring()
import re


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master)
        self.top = self.winfo_toplevel()


        self.dic={
            "TabStrip":{"relx":0.03, "rely":0.05,"relwidth":0.528, "relheight":0.55},
            "Tab1_title":{"relx":0.04, "rely":0.005, "relwidth":1, "relheight":0.19},
            "Tab1_fr":{"relx":0.2, "rely":0.893, "relwidth":0.6, "relheight":0.1},
            "Tab1_lb1":{"relx":0.035, "rely":0.884, "relwidth":0.16, "relheight":0.12},
            "Tab1_bt":{"relx":0.85, "rely":0.89, "relwidth":0.12, "relheight":0.1},
            "Tab2_bt":{"relx":0.29, "rely":0.89, "relwidth":0.22, "relheight":0.09},
            "Tab2_title":{"relx":0.031, "rely":0.003, "relwidth":1, "relheight":0.19},
            "Listbox1":{"relx":0.003,"rely":0.175,"relwidth":0.95,"relheight":0.7},
            "Scroll1":{"relx":0.99, "rely":0, "relwidth":0.025, "relheight":1},
            "Listbox2":{"relx":0.37,"rely":0.65,"relwidth":0.188,"relheight":0.337},
            "Scroll2":{"relx":0.93, "rely":0, "relwidth":0.068, "relheight":1},
            "Combox":{"relx":0.03, "rely":0.9, "relwidth":0.25, "relheight":0.07},

            "Frame":{
                '上传文件': {"relx": 0.03, "rely": 0.618, "relwidth": 0.314, "relheight": 0.369},
                '': {"relx": 0.063, "rely": 0.649, "relwidth": 0.204, "relheight": 0.061},
                '聊天区': {"relx": 0.603, "rely": 0.02, "relwidth": 0.382, "relheight": 0.967}
                },
            "Button":{
                '浏览 (L)': {"relx": 0.274, "rely": 0.666, "relwidth": 0.06, "relheight": 0.045},
                '上传 (U)': {"relx": 0.274, "rely": 0.927, "relwidth": 0.06, "relheight": 0.045},
                '撤回(Z)': {"relx": 0.83, "rely": 0.927, "relwidth": 0.06, "relheight": 0.045},
                '发送(S)': {"relx": 0.91, "rely": 0.927, "relwidth": 0.06, "relheight": 0.045}
                },
            "Search":{"relx":0.368, "rely":0.028, "relwidth":0.19, "relheight":0.046},
            "Chat":{"relx":0.618, "rely":0.65, "relwidth":0.352, "relheight":0.264},
            "Radio":{
                "显示所有":{"relx":0.23, "rely":0.028, "relwidth":0.064, "relheight":0.042},
                "模糊匹配":{"relx":0.3,"rely":0.029, "relwidth":0.064, "relheight":0.042}
                },
            "Img1":{"relx":0.036, "rely":0.666, "relwidth":0.015, "relheight":0.029},
            "Label3":{"relx":0.367, "rely":0.614, "relwidth":0.15, "relheight":0.029},
            "Up_Label":{"relx":0.065, "rely":0.665, "relwidth":0.185, "relheight":0.040},
            "Dw_Label":{"relx":0.21, "rely":0.91, "relwidth":0.55, "relheight":0.07},
            "Logout_Label":{"relx":0.55, "rely":0.884, "relwidth":0.4, "relheight":0.12},
            "Label4":{"relx":0.035, "rely":0.725, "relwidth":0.242, "relheight":0.040},
            "Label5":{"relx":0.035, "rely":0.768, "relwidth":0.242, "relheight":0.040},
            "Label6":{"relx":0.035, "rely":0.811, "relwidth":0.242, "relheight":0.040},
            "Label7":{"relx":0.035, "rely":0.865, "relwidth":0.242, "relheight":0.040},
            "Label8":{"relx":0.035, "rely":0.925, "relwidth":0.142, "relheight":0.040},


            "Button_fun":{'浏览 (L)': show_up_filedialog, '上传 (U)': hellou,
                    '撤回(Z)': helloz, '发送(S)': hellos},
            "Menu": {
                "文件(F)": {'上传本地文件  (Upload)': hellou,
                      '下载文件到本地  (Dwload)':show_dw_filedialog, "退出  (Quit)": helloq},
                "查看(V)": {"查看用户信息  (Info))": helloi,
                      "查看用户登录日志  (Log)": hellol, '查看文件详情  (Content)': helloc},
                "界面设置(S)": {"更换壁纸  (W)": show_ask_filedialog, "字体设置  (P)": hellop,
                        "进度条样式(Y)": hello, "关于 (A)": help_about}
                }

        }

        self.createNotebook()      
        self.createTab1(self.Tab1)
        self.createTab2(self.Tab2)
        self.createLableFrame()
        self.createButton()
        self.createSearch()
        self.createRadio()
        self.createOnline()
        self.createChat()
        self.createImg()
        self.createMenu()
        self.createLabel()
        #chat_view = ChatView(self.top)


    def createNotebook(self):
        self.style = Style()
        self.TabStrip = Notebook(self.top)
        self.TabStrip.place(**self.dic["TabStrip"])

        self.Tab1 = Frame(self.TabStrip)
        self.TabStrip.add(self.Tab1, text='   服务器文件仓储   ')
        self.Tab2 = Frame(self.TabStrip)
        self.TabStrip.add(self.Tab2, text='   用户操作记录   ')
    

    def createTab1(self,master):
        
        title1="-"*181+"\n|{0:^30}｜{1:^4}｜{2:^70}|{3:^40}｜{4:^40}|\n".format("文件名","大小","储存路径","修改时间","创建时间")+"-"*181
        self.Tab1.title = Label(master, text=title1)
        self.Tab1.title.place(**self.dic["Tab1_title"])
        self.lbox1=Scrollabe_Frame(master,scrollregion=(0,0,900,2500))
        self.lbox1.place(**self.dic["Listbox1"])
        self.lbox1.bar.place(**self.dic["Scroll1"])
        self.Tab1.fr = LabelFrame(master,text="")
        self.Tab1.fr.place(**self.dic["Tab1_fr"])
        self.down = Label(master,text="我要下载我要下载我要下载我要下载我要下载我要下载我要下载我要下载我要下载我要下载.py")
        self.down.place(**self.dic["Dw_Label"])
        self.Tab1.lb2 = Label(master,text="已选择文件：")
        self.Tab1.lb2.place(**self.dic["Tab1_lb1"])
        self.Tab1.bt = Mybutton(master,fun=show_dw_filedialog,text="下载(D)")
        self.Tab1.bt.place(**self.dic["Tab1_bt"])
        


    def createTab2(self,master):    
        tmp_list = ["用户编号", "文件编号", "操作类型"]
        title2="-"*101+"\n| 用户编号｜文件编号｜操作类型｜       储存路径　       |　　 操作时间  　｜\n"+"-"*101
        self.Tab2Lbl=Scrollabe_Frame(master)
        self.Tab2.title = Label(master, text=title2)
        self.Tab2.title.place(**self.dic["Tab2_title"])
        self.lbox2=Scrollabe_Frame(master,scrollregion=(0,0,900,2500))
        self.lbox2.place(**self.dic["Listbox1"])
        self.lbox2.bar.place(**self.dic["Scroll1"])

        self.Tab2.bt = Mybutton(master,fun=show_dw_filedialog,text="导出选中日志…")
        self.Tab2.bt.place(**self.dic["Tab2_bt"])
        self.combox=self.createCombox(master)
        self.combox.place(**self.dic["Combox"])
        self.logout = Label(master,text="导出日志导出日志导出日志导出日志导出日志导出日志导出日志导出日志导出日志导出日志.py")
        self.logout.place(**self.dic["Logout_Label"])

        for i in range(1, 6):
            for j in range(3):
                self.Tab2Lbl = Label(master, text=tmp_list[j]+str(i))
                self.Tab2Lbl.place(relx=0.05+0.2*j, rely=0.2+0.1*i, relwidth=0.15)
        
        

    def createLableFrame(self):
        for k, v in self.dic["Frame"].items():
            fr = LabelFrame(self.top, text=k)
            fr.place(**v)

    def createButton(self):
        for k, v in self.dic["Button"].items():
            self.button = Mybutton(self.top, self.dic["Button_fun"][k], text=k)
            self.button.place(**v)

    def createSearch(self):
        self.search = Myentry(self.top)
        self.search.place(**self.dic["Search"])

    def createChat(self):
        self.var = tk.Variable()
        self.chat = tk.Text(self.top)
        self.chat.config(font=("微软雅黑", 15), borderwidth=3, highlightcolor="#32CD32", highlightthickness=2,
                    relief=tk.FLAT, highlightbackground='#CCCCCC')
        self.var.set("请输入聊天内容")
        self.chat.place(**self.dic["Chat"])

    def createImg(self):
        self.img1 = Label(self.top, text="图")
        self.img1.place(**self.dic["Img1"])

    def createRadio(self):
        v = IntVar()
        v.set(1)
        self.r1 = Radiobutton(self.top, variable=v, text="显示所有", value=1)
        self.r1.place(**self.dic["Radio"]["显示所有"])
        self.r2 = Radiobutton(self.top, variable=v, text="模糊匹配", value=2)
        self.r2.place(**self.dic["Radio"]["模糊匹配"])


        
    def createOnline(self):
        self.lbox2=self.createScrollbox(self.top)
        self.lbox2.place(**self.dic["Listbox2"])
        self.lbox2.scrollbar.place(**self.dic["Scroll2"])


    def createLabel(self):

        b_filename = "我的上传我的上传我的上传我的上传我的上传我的上传我的上传我的上传我的上传我的上传我的上传我的上传我的上传"

        l3 = Label(self.top, text="在线用户列表")
        l3.place(**self.dic["Label3"])
        self.up = Label(self.top, text=b_filename)
        self.up.place(**self.dic["Up_Label"])
        l4 = Label(self.top, text="正在上传:  "+b_filename)
        l4.place(**self.dic["Label4"])
        l5 = Label(self.top, text="正在上传:  "+b_filename)
        l5.place(**self.dic["Label5"])
        l6 = Label(self.top, text="正在上传:  "+b_filename)
        l6.place(**self.dic["Label6"])
        l7 = Label(self.top, text=chr(9989)+chr(9993) +
                    "进度条进度条进度条进度条进度条进度条进度条进20%")
        l7.place(**self.dic["Label7"])
        l8 = Label(self.top, text="上传完毕!")
        l8.place(**self.dic["Label8"])


    def createScrollbox(self,master):
        listbox=Listbox(master, selectmode=EXTENDED)
        listbox.scrollbar = Scrollbar(listbox, orient=VERTICAL)
        listbox.config(yscrollcommand=listbox.scrollbar.set)
        listbox.scrollbar.config(command=listbox.yview)
        return listbox
    
    def createCombox(self,master):
        comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值  
        comboxlist=tkinter.ttk.Combobox(master,textvariable=comvalue) #初始化  
        comboxlist["values"]=("     以  .py  格式文件","     以  .txt  格式文件")  
        comboxlist.current(0)  #选择第一个  
        comboxlist.bind("<<ComboboxSelected>>",hellou)  #绑定事件,(下拉列表框被选中时，绑定go()函数)  
        return comboxlist

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

        self.add_cascade(label=m, menu=self.cascade,accelerator=self.hotkey(m)[m])



class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None, **kwargs):
        Application_ui.__init__(self, master, **kwargs)
    
        file_str=[
            ["file.py","2048","/home/tarena/lwh/my_ftp/file.py","2018-01-01 07:22:22","2018-01-01 07:22:22"],
            ["mysql_test.py","196","/home/tarena/lwh/my_ftp/mysql_test.py","2018-03-06 11:42:13","2018-01-01 07:22:22"],
            ["my_protocol.py","744","/home/tarena/lwh/my_ftp/my_protocol.py","2018-02-27 22:20:37","2018-01-01 07:22:22"],
            ["test_view.py","611","/home/tarena/lwh/my_ftp/upload/test_view.py","2018-05-06 01:02:58","2018-01-01 07:22:22"],
            ["server_class.py","690","/home/tarena/lwh/my_ftp/upload/server_class.py","2018-01-31 19:54:02","2018-01-01 07:22:22"],
            ["filefolder.py","387","/home/tarena/lwh/my_ftp/upload/filefolder.py","2018-03-14 15:19:26","2018-01-01 07:22:22"]
        ]
        for filestr in file_str:
            ListItems(self.lbox1.frame,filestr)
        #for filestr in file_str:
        #    ListItems(self.lbox2.frame,filestr)
        
        user_online=[["用户"+str(iii),"172.16.122."+str(iii)] for iii in range(1,100)]
        self.user_display(self.lbox2,user_online)

    def createMenu(self):
        menubar = Mymenu(self.top)
        for k, v in self.dic["Menu"].items():
            menubar.add_menu(v, k)
        self.top['menu'] = menubar

    
    def user_display(self,lbox,onlinelist):
        for fs in onlinelist:
            fs="{0}   ({1})".format(*fs)            
            #fs="|{0:<20}{sp}｜{1}｜{2:<}|{3:^}｜{4!s:^}|".format(Wi=qqq,sp="*"*20,*fs)
            lbox.insert(END,fs)
            lbox.bind("<Double-Button-1>", hellou) #list_fun
            lbox.select_set(onlinelist.index(onlinelist[0]))
            lbox.see(onlinelist.index(onlinelist[0]))


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
    messagebox.showinfo('关于', ' 团队：疯狂码头 \n 成员: 张晋 李文辉 方毅超 刘章杰\n             谭锐锋 谭永权 杨凌枫 \n verion 1.0 \n 感谢您的使用！ \n ©2018 ')  # 弹出消息提示框

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
def hellou(x):
    print("hellou"+str(x))
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
    root.title("疯狂码头")
    root.resizable(width=True, height=True)
    # root.attributes("-alpha",0.9)

    #  画布可以插底图， 我先注释掉
    # img=PhotoImage(file="E:\\Fäniz\\小组项目\\marong.png")
    # w=Label(root,text="abc",image=img)
    # w.place(relx=0,rely=0,relwidth=0.02,relheight=1)



    # 聊天大厅， 替换成张晋的气泡滚动条
    #histroy_talk = Listbox(root)
    #histroy_talk.place(relx=0.618, rely=0.06, relwidth=0.352, relheight=0.54)
    

    Application(root).mainloop()
    
    root.mainloop()


if __name__ == "__main__":
    main()
