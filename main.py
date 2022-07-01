import tkinter
from tkinter import *
from tkinter.filedialog import *
import time
from threading import Timer
from tkinter.messagebox import *
import random
root = Tk()
root.title("随机点名")
root.geometry('800x400')
name1_list = Listbox(font=(10))
name1_list.place(x=500, y=40, width=110, height=300)
sc = Scrollbar(master=name1_list)
sc.pack(side=RIGHT, fill=Y)
name1_list.config(yscrollcommand=sc.set)
sc.config(command=name1_list.yview)   #定义列表框
name_text = Text()
name_text.insert(1.0,"请选择随机名单....")
name_text.config(foreground="grey")
name_text.place(x=600, y=10, width=130, height=20)
name2_list = Listbox(font=10)
name2_list.place(x=690, y=40, width=110, height=300)
sc2 = Scrollbar(master=name2_list)
sc2.pack(side=RIGHT, fill=Y)
name2_list.config(yscrollcommand=sc2.set)
sc2.config(command=name2_list.yview)#定义列表框2
la_nu=StringVar()
la_nu.set(f"备选名单：{name1_list.size()}")
la1 = Label(textvariable=la_nu, font=('黑体', 12, "bold"),foreground="green")
la1.place(x=490,y=350)
la2 = Label(text=f"排除人数:{str(name2_list.size())}", font=('黑体', 12, "bold"),foreground="orange")
la2.place(x=690, y=350)
name_la = Label(text="姓名", font=('黑体', 90, "bold"))
name_la.place(x=110, y=60)
namester_list = []
namester2_list = []
timela=Label(text="111",font=('黑体', 18, "bold"))
timela.place(x=200,y=300)


def timework():
    week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    a=int(time.strftime('%w'))-1
    timela.config(text=time.strftime(f'%Y年%m月%d日 {week_list[a]}\n%H:%M:%S '))
    global tim
    tim=Timer(1,timework)
    tim.start()


tim=Timer(1,timework)
timework()
ster = StringVar()
ster.set("开始")


def fil_get():
    with open(askopenfilename(), encoding='utf-8') as file:  # 选择要打开的文件
        file_name = file.name[file.name.rfind('/') + 1:]  # 获取文件名称
        name_text.delete(1.0,END)
        name_text.insert(1.0, file_name)
        name_text.config(foreground="black")
        for i in file.readlines():
            name1_list.insert(END, i)
            namester_list.append(i)
    la_nu.set(f"备选名单：{name1_list.size()}")


def st_timer():
    global st
    st=random.choice(namester_list)
    name_la.config(text=st)
    global stim
    stim=Timer(0.05,st_timer)
    stim.start()


def move_name():
    n=0
    for i in namester_list:
        if st==i:
            name2_list.insert(END,st)
            print(n)
            name1_list.delete(n)
            namester_list.pop(n)
            namester2_list.append(st)
        n+=1


def st_bth():
    if name1_list.size()==0 and name2_list.size()==0:
        print(showerror("错误","请先导入数据"))
        fil_get()
    if ster.get()=="开始":
        ster.set("停止")
        s_bth.config(foreground="orange")
        st_timer()
        print(namester_list)
        la_nu.set(f"备选名单：{name1_list.size()}")
        la2.config(text="排除人数："+str(name2_list.size()))
        name_la.config(text=random.choice(namester_list))
    else:
        ster.set("开始")
        s_bth.config(foreground="green")
        stim.cancel()
        move_name()
        print(str(name1_list.size()))
        la_nu.set(f"备选名单：{name1_list.size()}")
        la2.config(text="排除人数："+str(name2_list.size()))


s_bth = Button(textvariable=ster, command=st_bth, width=8, height=1, font=("仿宋",22,'bold'),foreground="green")

s_bth.place(x=50, y=300)


def lef_bthf():
    n=name2_list.curselection()
    for a in n:
        st=namester2_list[a]
        name1_list.insert(END,st)
        name2_list.delete(a)
        namester2_list.pop(a)
        namester_list.append(st)
        print(name1_list.size())
        la_nu.set(f"备选名单：{name1_list.size()}")
        la2.config(text="排除人数："+str(name2_list.size()))


def rig_bthf():
    n=name1_list.curselection()
    for a in n:
        # print(a)
        st=namester_list[a]
        # print(st)
        name2_list.insert(END,st)
        name1_list.delete(a)
        namester_list.pop(a)
        namester2_list.append(st)

    la2.config(text=f"排除人数：{str(name2_list.size())}")
    print(name1_list.size())
    la_nu.set(f"备选名单：{name1_list.size()}")


fil_bth=Button(text='浏览文件',command=fil_get).pack(anchor='ne')


lef_bth=Button(text="<<",font=("red"),command=lef_bthf,foreground="green").place(x=635,y=150)


rig_bth=Button(text=">>",font=("red"),command=rig_bthf,foreground="orange").place(x=635,y=200)
root.mainloop()
tim.cancel()