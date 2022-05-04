import os
from tkinter import Tk,Button,Label,messagebox,simpledialog,Scrollbar,RIGHT,Y,YView,Menu,OptionMenu,ttk,PhotoImage,filedialog
import urllib.request
root = Tk()
root.withdraw()
ver = 3.1
nver = None
root.resizable(False,False)
def update_path():
    try:
        url = 'https://aero80wd.github.io/ver.ini'
        r = urllib.request.urlopen(url)
        with open("ver.ini", "wb") as code:
            code.write(r.read())
        f = open('ver.ini','r')
        nver = f.read()
        f.close()
        os.remove('ver.ini')
        return nver
    except:
        messagebox.showinfo('提示','您未连接到网络，无法使用')
    
    

nver = update_path()

def help():
    win = Tk()
    win.title('关于')
    win.geometry('400x200')
    win.config(bg="#66ccff")

    win.resizable(False,False)
    ht = Label(win,text="pipGUI",font=('微软雅黑 Light',30),bg="#66ccff")
    ht.pack()
    v = Label(win,text="版本3.0",font=('微软雅黑 Light',20),bg="#66ccff")
    v.pack()
    v = Label(win,text="Powered By Aero8小小",font=('微软雅黑 Light',17),bg="#66ccff")
    v.pack()
    e = Button(win,text='关闭',font=('微软雅黑 Light',20),command=win.withdraw,width=15,height=1,bd=0,bg="#ffffff")
    e.pack()
def get_yn():
    new_yn = simpledialog.askstring('提示','请输入新源：')
    if (new_yn == None) or (new_yn == ''):
        return
    get = 'pip config set global.index-url ' + new_yn
    os.system(get)
    messagebox.showinfo('提示','修改默认源完成！')
def red():
    os.system('pip config set global.index-url https://pypi.python.org/simple')
    messagebox.showinfo('提示','恢复默认源完成！')
def get_dqy():
    dqy = Tk()
    dqy.geometry('1x1')
    dqy.withdraw()

def y():
    y = Tk()
    y.title('pipGUI设置源')
    y.config(bg='#66ccff')
    y.geometry('600x400')

    y.resizable(False,False)
    t = Label(y,text='设置源',font=('微软雅黑 Light',30),bg='#66ccff')
    t.pack()
    h = Button(y,text="设置默认源",font=("微软雅黑 Light",25),command=get_yn,width=17,height=1,bg='#ffffff',bd=0)
    h.pack()
    h = Button(y,text="恢复默认源",font=("微软雅黑 Light",25),command=red,width=17,height=1,bg='#ffffff',bd=0)
    h.pack()
def cheak_update():
    nver = update_path()
    if float(nver) > ver:
        ver_help = '发现新版本：' + nver + '。是否立即更新？'
        msg_update = messagebox.askyesno('提示',ver_help)
        if msg_update:
            os.system('start https://github.com/aero80wd/pipGUI')
        if not msg_update:
            return
    if float(nver) < ver:
        messagebox.showerror('提示','检测到盗版，即将退出')
        exit()
    if float(nver) == ver:
        messagebox.showinfo('提示','您的pipGUI为最新版，无需更新！')
def setting():
    seg = Tk()
    seg.title('pipGUI设置')
    seg.config(bg='#66ccff')
    seg.geometry('600x400')

    seg.resizable(False,False)
    t = Label(seg,text='设置',font=('微软雅黑 Light',30),bg='#66ccff')
    yu = Button(seg,text="设置安装源",font=("微软雅黑 Light",25),command=y,width=17,height=1,bg='#ffffff',bd=0)
    h = Button(seg,text="关于",font=("微软雅黑 Light",25),command=help,width=17,height=1,bg='#ffffff',bd=0)
    u = Button(seg,text="检查更新",font=("微软雅黑 Light",25),command=cheak_update,width=17,height=1,bg='#ffffff',bd=0)
    t.pack()
    yu.pack()
    h.pack()
    u.pack()
def upg():
    os.system('start https://github.com/aero80wd/pipGUI')
def command(event):
    # 使用 post()在指定的位置显示弹出菜单
    main_menu.post(event.x_root, event.y_root)
main_menu = Menu (root,tearoff=0)
main_menu.add_command(label="关于",command=help,font=('微软雅黑 Light',10))
main_menu.add_command(label="退出",command=root.quit,font=('微软雅黑 Light',10))
if ver < float(nver):
    main_menu.add_command(label="更新pipGUI",command=upg,font=('微软雅黑 Light',10))
main_menu.add_command(label="设置",command=setting,font=('微软雅黑 Light',10))
root.config(menu=main_menu)
root.bind("<Button-3>", command)
if os.path.exists('list.cmd') == False:
    with open('list.cmd','a') as pip:
        pip.write('@echo off\ntitle 所有模块\npip list\npause\nexit')
def pip_install_network():
    py = simpledialog.askstring('提示','请输入模块名或网络路径：')
    if (py == None) or (py == ''):
        return 
    a = messagebox.askyesnocancel('提示','请问需要输入版本号吗？')
    if a:
        all = '请输入' + py + '模块的版本号：'
        pyint = simpledialog.askstring('提示',all)
        os.system('start pip install ' + py + '==' + pyint)
    if not a:
        os.system('start pip install ' + py)
    if a == None:
        return
def pip_install_file():
    install_path = filedialog.askopenfilename(title = "选择whl文件",filetypes = (("Python模块文件","*.whl"),("Python Zip 模块文件","*.zip")))
    if install_path == '':
        return
    file_install_command = 'start pip install ' + str(install_path)
    os.system(file_install_command)
def pip_install():
    iw = Tk()
    iw.title('安装模块选项')
    iw.geometry('600x300')
    iw.config(bg='#66ccff')
    iw.resizable(False,False)
    title = Label(iw,text="安装模块选项",font=("微软雅黑 Light",40),bg='#66ccff')
    title.pack()
    file = Button(iw,text="安装whl",font=("微软雅黑 Light",25),command=pip_install_file,width=17,height=1,bg='#ffffff',bd=0)
    network = Button(iw,text="安装网络上的模块",font=("微软雅黑 Light",25),command=pip_install_network,width=17,height=1,bg='#ffffff',bd=0)
    file.pack()
    network.pack()
def pip_uninstall():
    unpy = simpledialog.askstring('提示','请输入模块名：')
    if unpy != None:
        os.system('start pip uninstall ' + unpy)
def pip_list():
    os.system('start list.cmd')
def pipu():
    os.system('start pip install --upgrade pip')
def update_package():
    uppy = simpledialog.askstring('提示','请输入模块名：')
    if (uppy == None) or (uppy == ''):
        return 
    a = messagebox.askyesnocancel('提示','请问需要指定升级版本号吗？')
    if a:
        all = '请输入' + uppy + '模块要升级的版本号：'
        uppyint = simpledialog.askstring('提示',all)
        if (uppyint == None) or (uppyint == ''):
            return 
        os.system('start pip install --upgrade ' + uppy + '==' + str(uppyint))
    if not a:
        os.system('start pip install --upgrade ' + uppy)
    if a == None:
        return
def show_package():
    showpy = simpledialog.askstring('提示','请输入模块名：')
    if (showpy == None) or (showpy == ''):
        return 
    os.system('start cmd /k pip show package ' + showpy)
def get_pip_ver():
    os.system('start cmd /k pip --version')
def cheak_package_update():
    os.system('start cmd /k pip list --outdated')
def uninstall_pip():
    os.system('start pip uninstall pip')
if float(nver) > ver:
    messagebox.showinfo('提示','此pipGUI不是最新版，请下载最新版')
if float(nver) < ver:
    messagebox.showerror('提示','检测到盗版，即将退出')
    exit()
root.deiconify()
root.title('pipGUI')
root.geometry('800x550+348+99')
root.config(bg='#66ccff')


title = Label(text="pipGUI 3.1",font=("微软雅黑 Light",30),bg='#66ccff')
title.pack()

b1 = Button(text="安装模块",font=("微软雅黑 Light",20),command=pip_install,width=17,height=1,bg='#ffffff',bd=0)

b1.pack()

b2 = Button(text="查看已安装的模块",font=("微软雅黑 Light",20),command=pip_list,width=17,height=1,bg='#ffffff',bd=0)

b2.pack()

b3 = Button(text="卸载模块",font=("微软雅黑 Light",20),command=pip_uninstall,width=17,height=1,bg='#ffffff',bd=0)

b3.pack()

b4 = Button(text="升级pip",font=("微软雅黑 Light",20),command=pipu,width=17,height=1,bg='#ffffff',bd=0)
b4.pack()

b5 = Button(text="升级指定包",font=("微软雅黑 Light",20),command=update_package,width=17,height=1,bg='#ffffff',bd=0)
b5.pack()
b6 = Button(text="查看pip版本",font=("微软雅黑 Light",20),command=get_pip_ver,width=17,height=1,bg='#ffffff',bd=0)
b6.pack()
b7 = Button(text="查看需更新的包",font=("微软雅黑 Light",20),command=cheak_package_update,width=17,height=1,bg='#ffffff',bd=0)
b7.pack()
b8 = Button(text="卸载pip(慎用)",font=("微软雅黑 Light",20),command=uninstall_pip,width=17,height=1,bg='#ffffff',bd=0)
b8.pack()
root.mainloop()
