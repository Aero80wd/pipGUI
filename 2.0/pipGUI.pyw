import os
from tkinter import Tk,Button,Label,messagebox,simpledialog,Scrollbar,RIGHT,Y,YView,Menu,OptionMenu,ttk
from bs4 import BeautifulSoup
from urllib import request
root = Tk()
root.title('pipGUI')
root.geometry('800x500')
root.config(bg='#66ccff')
ver = 2.0
def help():
    win = Tk()
    win.title('关于')
    win.geometry('400x200')
    win.config(bg="#66ccff")
    ht = Label(win,text="pipGUI",font=('微软雅黑 Light',30),bg="#66ccff")
    ht.pack()
    v = Label(win,text="版本2.0",font=('微软雅黑 Light',20),bg="#66ccff")
    v.pack()
    v = Label(win,text="Powered By Aero8小小",font=('微软雅黑 Light',17),bg="#66ccff")
    v.pack()
    e = Button(win,text='关闭',font=('微软雅黑 Light',20),command=win.withdraw,width=15,height=1,bd=0,bg="#ffffff")
    e.pack()
def command(event):
    # 使用 post()在指定的位置显示弹出菜单
    menu2.post(event.x_root, event.y_root)
main_menu = Menu (root)
main_menu.add_command(label="关于",command=help,font=('微软雅黑 Light',20))
main_menu.add_command(label="退出",command=root.quit,font=('微软雅黑 Light',20))
root.config(menu=main_menu)
menu2 = Menu(root, tearoff=False)
menu2.add_command(label="关于", command=help)
menu2.add_command(label="退出", command=root.quit)
root.bind("<Button-3>", command)
if os.path.exists('list.cmd') == False:
    with open('list.cmd','a') as pip:
        pip.write('@echo off\ntitle 所有模块\npip list\npause\nexit')
html = request.urlopen("https://aero80wd.github.io/pipGUI.html")
bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
nver = bs_obj.div['id']
def pip_install():
    py = simpledialog.askstring('提示','请输入模块名：')
    if py != None:

        a = messagebox.askquestion('提示','请问需要输入版本号吗？')
        if a == 'yes':
            all = '请输入' + py + '模块的版本号：'
            py = simpledialog.askstring('提示',all)
            os.system('start pip install -U' + py)
        if a == 'no':
            os.system('start pip install ' + py)
def pip_uninstall():
    unpy = simpledialog.askstring('提示','请输入模块名：')
    if unpy != None:
        os.system('start pip uninstall ' + unpy)
def pip_list():
    os.system('start list.cmd')
def pipu():
    os.system('start pip install --upgrade pip')
def upg():
    os.system('start https://github.com/aero80wd/pipGUI')
if float(nver) > ver:
    messagebox.showinfo('提示','此pipGUI不是最新版，请下载最新版')


title = Label(text="欢迎使用pipGUI!",font=("微软雅黑 Light",40),bg='#66ccff')
title.pack()

b1 = Button(text="安装模块",font=("微软雅黑 Light",25),command=pip_install,width=17,height=1,bg='#ffffff',bd=0)

b1.pack()

b2 = Button(text="查看已安装的模块",font=("微软雅黑 Light",25),command=pip_list,width=17,height=1,bg='#ffffff',bd=0)

b2.pack()

b3 = Button(text="卸载模块",font=("微软雅黑 Light",25),command=pip_uninstall,width=17,height=1,bg='#ffffff',bd=0)

b3.pack()

b4 = Button(text="升级pip",font=("微软雅黑 Light",25),command=pipu,width=17,height=1,bg='#ffffff',bd=0)
b4.pack()

if ver < float(nver):
    b4 = Button(text="升级pipGUI",font=("微软雅黑 Light",25),command=upg,width=17,height=1)
    b4.pack()
root.mainloop()
