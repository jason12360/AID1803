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
if __name__=='__main__':
    from widgets_interface.my_widgets import *
    from widgets_interface.file_displayer import *
else:
    from view.widgets_interface.my_widgets import *
    from view.widgets_interface.file_displayer import *
# import tkinter.simpledialog as tkSimpleDialog   #askstring()
import re






def show_ask_filedialog():
    fileN = tkinter.filedialog.askdirectory(filetypes=[("py格式", ".py")])
    print(fileN)
    return fileN
# def show_error(string)

def help_about():
    messagebox.showinfo('关于', ' 团队：疯狂码头 \n 成员: 张晋 李文辉 方毅超 刘章杰\n             谭锐锋 谭永权 杨凌枫 \n verion 1.0 \n 感谢您的使用！ \n ©2018 ')  # 弹出消息提示框

def hellou(x):
    print("hellou")
def hellod():
    print("hellod")
def helloq():
    print("helloq")
def hellof():
    print("hellof")
def helloi():
    print("helloi")
def hellol(x):
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
def helloz(x):
    print("helloz")
def hellos(x):
    print("hellos")
def helloo():
    print("helloo")


place_json={
    "TabStrip":{"relx":0.03, "rely":0.05,"relwidth":0.528, "relheight":0.55},
    "Tab_title":{"relx":0.004, "rely":0, "relwidth":1, "relheight":0.19},
    "Tab_frame":{"relx":0.2, "rely":0.893, "relwidth":0.6, "relheight":0.1},
    "Tab_label":{"relx":0.035, "rely":0.884, "relwidth":0.16, "relheight":0.12},
    "Tab1_button":{"relx":0.85, "rely":0.89, "relwidth":0.12, "relheight":0.1},
    "Tab2_button":{"relx":0.29, "rely":0.89, "relwidth":0.22, "relheight":0.09},
    "Tab_listbox":{"relx":0.003,"rely":0.115,"relwidth":0.994,"relheight":0.7},
    "Tab_scroll":{"relx":0.978, "rely":0, "relwidth":0.023, "relheight":1},
    "Online_listbox":{"relx":0.37,"rely":0.65,"relwidth":0.188,"relheight":0.337},
    "Online_scroll":{"relx":0.93, "rely":0, "relwidth":0.068, "relheight":1},
    "Combox":{"relx":0.03, "rely":0.9, "relwidth":0.25, "relheight":0.07},
    "Frame":{
        '': {"relx": 0.063, "rely": 0.655, "relwidth": 0.804, "relheight": 0.065},
        '上传文件': {"relx": 0.03, "rely": 0.618, "relwidth": 0.314, "relheight": 0.369},
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
    "Up_Label":{"relx":0.065, "rely":0.665, "relwidth":0.185, "relheight":0.040},
    "Down_Label":{"relx":0.21, "rely":0.91, "relwidth":0.55, "relheight":0.07},
    "Logout_Label":{"relx":0.55, "rely":0.884, "relwidth":0.4, "relheight":0.12},
    "Up_line0":{"relx":0.367, "rely":0.614, "relwidth":0.15, "relheight":0.029},
    "Up_line1":{"relx":0.035, "rely":0.725, "relwidth":0.242, "relheight":0.040},
    "Up_line2":{"relx":0.035, "rely":0.768, "relwidth":0.242, "relheight":0.040},
    "Up_line3":{"relx":0.035, "rely":0.811, "relwidth":0.242, "relheight":0.040},
    "Up_line4":{"relx":0.035, "rely":0.865, "relwidth":0.242, "relheight":0.040},
    "Up_line5":{"relx":0.035, "rely":0.925, "relwidth":0.142, "relheight":0.040}
}



class MyGUI(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master,place_dic,**kwargs):
        Frame.__init__(self, master)
        self.top = self.winfo_toplevel()
        self.dic=place_dic
        self.button_dic={}
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
        self.createLabel()

    def createNotebook(self):
        self.style = Style()
        self.TabStrip = Notebook(self.top)
        self.TabStrip.place(**self.dic["TabStrip"])
        T=['      服务器文件仓储      ','      用户操作记录      ']
        Tabs=[]
        for t in range(len(T)):
            Tabs.append(Frame(self.TabStrip))
            self.TabStrip.add(Tabs[t], text=T[t])
            Tabs[t].title=Scrollabe_Frame(Tabs[t],scrollregion=(0,0,1200,2500))
            Tabs[t].title.place(**self.dic["Tab_title"])
            Tabs[t].lbox=Scrollabe_Frame(Tabs[t],scrollregion=(0,0,1200,2500))
            Tabs[t].lbox.place(**self.dic["Tab_listbox"])
            #Tabs[t].lbox.bar.place(**self.dic["Tab_scroll"])
        self.Tab1,self.Tab2=Tabs

 
    def createTab1(self,master):     
        self.Tab1.fr = LabelFrame(master)
        self.Tab1.fr.place(**self.dic["Tab_frame"])
        self.dwlabel = Label(master)
        self.dwlabel.place(**self.dic["Down_Label"])
        self.Tab1.lb = Label(master,text="已选择文件：")
        self.Tab1.lb.place(**self.dic["Tab_label"])
        self.Tab1.bt = Mybutton(master,self.undefined,text="下载(D)")
        self.button_dic["下载(D)"]=self.Tab1.bt
        self.Tab1.bt.place(**self.dic["Tab1_button"])
        
    def createTab2(self,master):    
        self.Tab2.bt=Mybutton(master,self.undefined,text="导出选中日志…")
        self.button_dic["导出选中日志…"]=self.Tab2.bt
        self.Tab2.bt.place(**self.dic["Tab2_button"])
        self.combox=self.createCombox(master)
        self.combox.place(**self.dic["Combox"])
        self.logout = Label(master)
        self.logout.place(**self.dic["Logout_Label"])
        
    def createLableFrame(self):
        for k, v in self.dic["Frame"].items():
            fr = LabelFrame(self.top, text=k)
            fr.place(**v)

    def createButton(self):
        for k, v in self.dic["Button"].items():
            self.button = Mybutton(self.top,self.undefined, text=k)
            self.button_dic[k]=self.button
            self.button.place(**v)

    def createSearch(self):
        self.search = Myentry(self.top)
        self.search.place(**self.dic["Search"])

    def createChat(self):
        self.var = tk.Variable()
        self.chat = tk.Text(self.top)
        self.chat.config(font=("微软雅黑", 15), borderwidth=3, 
              highlightcolor="#32CD32", highlightthickness=2,
              relief=tk.FLAT, highlightbackground='#CCCCCC')
        self.var.set("请输入聊天内容")
        self.chat.place(**self.dic["Chat"])

    def createImg(self):
        self.img1 = Label(self.top, text="图")
        self.img1.place(**self.dic["Img1"])

    def createRadio(self):
        self.v = IntVar()
        self.v.set(1)
        self.r1 = Radiobutton(self.top, 
            variable=self.v, text="显示所有", value=1)
        self.r1.place(**self.dic["Radio"]["显示所有"])
        self.r2 = Radiobutton(self.top, 
            variable=self.v, text="模糊匹配", value=2)
        self.r2.place(**self.dic["Radio"]["模糊匹配"])
    
    def createOnline(self):
        self.lbox2=self.createScrollbox(self.top)
        self.lbox2.place(**self.dic["Online_listbox"])
        self.lbox2.scrollbar.place(**self.dic["Online_scroll"])

    def createLabel(self):
        self.uplabel = Label(self.top)
        self.uplabel.place(**self.dic["Up_Label"])
        L=[]
        for i in range(6):
            L.append(Label(self.top))
            L[i].place(**self.dic["Up_line"+str(i)])
        self.upline0,self.upline1,self.upline2,\
            self.upline3,self.upline4,self.upline5=L

    def createScrollbox(self,master):
        listbox=Listbox(master, selectmode=EXTENDED)
        listbox.scrollbar = Scrollbar(listbox, orient=VERTICAL)
        listbox.config(yscrollcommand=listbox.scrollbar.set)
        listbox.scrollbar.config(command=listbox.yview)
        return listbox
    
    def createCombox(self,master):
        comvalue=tkinter.StringVar() 
        comboxlist=tkinter.ttk.Combobox(master,textvariable=comvalue)
        return comboxlist

    def undefined(self):
        print("undefined")


class Application(MyGUI):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, **kwargs):
        self.root = tk.Tk()
        self.root.geometry("1280x800")
        self.root.title("疯狂码头")
        self.root.resizable(True, True)
        MyGUI.__init__(self, self.root,place_json,**kwargs)
        Button_fun={'浏览 (L)': self.show_up_filedialog, 
                '上传 (U)': self.upload,'撤回(Z)': helloz, 
                '发送(S)': hellos,'下载(D)':self.download,
                "导出选中日志…":hellos }
        Menu_fun={
            "文件(F)": {'上传本地文件  (Upload)': hellou,
                  '下载文件到本地  (Dwload)':hellou, "退出  (Quit)": helloq},
            "查看(V)": {"查看用户信息  (Info))": helloi,
                  "查看用户登录日志  (Log)": hellol, '查看文件详情  (Content)': helloc},
            "界面设置(S)": {"更换壁纸  (W)": show_ask_filedialog, "字体设置  (P)": hellop,
                  "进度条样式(Y)": hello, "关于 (A)": help_about}
            }


        
        self.button_bind(Button_fun)
        self.menu_bind(Menu_fun)
        self.combox_bind()
        

        self.dwlabel.config(text="我要下载我要下载我要下载我要下载我要下载我要下载我要下载我要下载我要下载我要下载.py")
        

        self.uplabel.config(text="即将上传文件.py")
        self.upline0.config(text="在线用户列表")
        self.upline1.config(text="第1行")
        self.upline2.config(text="第2行")
        self.upline3.config(text="第三行")
        self.upline4.config(text=chr(9989)+chr(9993)+"bfdbdf进度条进度条进度条进度条进度条进度条进度条进20%")
        self.upline5.config(text="上传完毕!!!")
        self.logout.config(text="hfgdhgdf导出日志导出日志导出日志导出日志导出日志导出日志导出日志导出日志导出日志导出日志.py")
        

        file_SQL=[
            ["file.py","2048","2018-01-01 07:22:22","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/file.py"],
            ["mysql_test.py","196","2018-03-06 11:42:13","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/mysql_test.py"],
            ["my_protocol.py","744","2018-02-27 22:20:37","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/my_protocol.py"],
            ["test_view.py","611","2018-05-06 01:02:58","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/upload/test_view.py"],
            ["server_class.py","690","2018-01-31 19:54:02","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/upload/server_class.py"],
            ["filefolder.py","387","2018-03-14 15:19:26","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/upload/filefolder.py"]
        ]

        log_SQL=[
            ["3306","2048","up","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/file.py"],
            ["9999","196","down","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/mysql_test.py"],
            ["4444","744","down","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/my_protocol.py"],
            ["4156","611","up","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/upload/test_view.py"],
            ["8462","690","up","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/upload/server_class.py"],
            ["2983","387","down","2018-01-01 07:22:22","/home/tarena/lwh/my_ftp/upload/filefolder.py"]
        ]
        # self.files_display(file_SQL)
        self.logs_display(log_SQL)

        #title_str1={"文件名":15,"大小":5,"修改时间":20,"创建时间":20,"储存路径":40}

        title_str1=["文件名","大小","修改时间","创建时间","储存路径"]




        ListItems(self.Tab1.title.frame,"#DDDDDD",title_str1)
        title_str2=["用户编号","文件编号","操作类型","操作时间","储存路径"]
        ListItems(self.Tab2.title.frame,"#DDDDDD",title_str2)
      
        user_online=[["用户"+str(iii),"172.16.122."+str(iii)] for iii in range(1,100)]
        self.user_display(self.lbox2,user_online)

    def menu_bind(self,Menu_fun):
        menubar = Mymenu(self.top)
        for k, v in Menu_fun.items():
            menubar.add_menu(v, k)
        self.top['menu'] = menubar
    def button_bind(self,Button_fun):
        for k,v in Button_fun.items():
            self.button_dic[k].bind('<Button-1>',v)

    def combox_bind(self):
        self.combox["values"]=("       以  .py  格式文件","       以  .txt  格式文件","       以  .html  格式文件")  
        self.combox.current(0)  #选择第一个  
        self.combox.bind("<<ComboboxSelected>>",hellou)  #绑定事件,(下拉列表框被选中时，绑定go()函数)  

    def files_display(self,files_list):
        self.FL_list=[]
        #self.Tab1.lbox.frame.config(height=800)
        for file in files_list:
            self.FL_list.append(ListItems(self.Tab1.lbox.frame,'#FFFFFF',file))

      
        for _FL in self.FL_list:
            _FL.bind_label(self.dwlabel)
            _FL.actions()
        self.Tab1.lbox.flush()

        self.Tab1.lbox.bar.place(**self.dic["Tab_scroll"])
    def logs_display(self,logs_list):
        for log in logs_list:
            ListItems(self.Tab2.lbox.frame,'#DDDDDD',log).actions()
    def user_display(self,lbox,onlinelist):
        for fs in onlinelist:
            fs="{0:15}   ({1!s:^})".format(*fs)            
            lbox.insert(END,fs)
            lbox.bind("<Double-Button-1>", hellou) 
            lbox.select_set(onlinelist.index(onlinelist[0]))
            lbox.see(onlinelist.index(onlinelist[0]))

    def show_dw_filedialog(self):
        fileN = tkinter.filedialog.asksaveasfilename(
          filetypes=[("py格式", ".py")])
        print(fileN)
        return fileN
    def show_up_filedialog(self):
        fileN = tkinter.filedialog.askopenfilename(initialdir=os.path.abspath("fyc_version8"),
        filetypes=[("py格式", ".py")])
        print(fileN)
        return fileN
    def run(self):    
        self.root.mainloop()
    def close(self):
        pass
    def download(self,event):
        pass
    def upload(self,event):
        pass

# Application().run()

