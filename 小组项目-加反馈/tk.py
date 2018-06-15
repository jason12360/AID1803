from tkinter import *
t=Tk()

t.title("哈哈")
t.geometry("500x500")
Label(t, text="计算器", bg="green", 
      font=("Arial", 12), 
      width=50, height=5).pack()


Label(t, text="参数１").pack()
e1 = Entry(t)
e1.pack()

Label(t, text="参数２").pack()
e2 = Entry(t)
e2.pack()

Label(t, text="和").pack()
e3 = Entry(t)
e3.pack()

def cal():
    a=int(e1.get())
    b=int(e2.get())
    print(a,"+",b,end="")
    c=a+b
    e3.insert( "insert",str(c))
    print('=',c)


b=Button(t,text="结果",command=cal)
b.pack()


t.mainloop()

