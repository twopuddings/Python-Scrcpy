import os
import threading
import subprocess
import tkinter as tk
window = tk.Tk()
window.title('安卓投屏')

class Scrcpy_thread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        start_screen()

def start_screen():
    if e4.get() == '':
        str1=''
    else:
        str1=' -s '+e4.get()
    cmd='echo.| .\scrcpy --max-fps '+e3.get()+' -b '+e2.get()+'M'+ckv.get()+' -m '+e1.get()+str1
    res = subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def start_screen_Enter(self):
    start_screen_thread()

def check_devices():
    cmd2='adb devices'
    os.system('start cmd /K '+cmd2)

def start_screen_thread():
    thread1 = Scrcpy_thread(1,"Scrcpy")
    thread1.start()

frm=tk.Frame(window)
frm.pack(side='left',fill='y')

#注意事项
lb5=tk.Label(frm,text='手机用数据线连接电脑\n并打开手机的USB调试模式',fg='red')
lb5.pack(side='top',fill='x')

#使用说明
lb1=tk.Label(frm,text='全屏 -- ALT+F\n缩放窗口到1:1 -- ALT+G\n缩放窗口到没有黑边 -- ALT+W\n主页键 -- 鼠标中键\n返回键 -- 鼠标右键\n最近任务栏 -- ALT+S\n电源键 -- ALT+P\n下拉通知栏 -- ALT+N')
lb1.pack(side='top',fill='x')

#分辨率
lb2=tk.Label(window,text='分辨率(按手机分辨率比例缩放，填入分辨率的长）',font=(12))
lb2.pack(side='top',fill='x',anchor='center')

screen=tk.StringVar(value='900')
e1=tk.Entry(window,textvariable=screen)
e1.pack(side='top',anchor='center')

#码率
lb3=tk.Label(window,text='传输码率(越高越清晰，但手机负荷越大)',font=(12))
lb3.pack(side='top',fill='x',anchor='center')

bit=tk.StringVar(value='20')
e2=tk.Entry(window,textvariable=bit)
e2.pack(side='top',anchor='center')

#帧率
lb4=tk.Label(window,text='帧率(越高越流畅，但手机负荷越大)',font=(12))
lb4.pack(side='top',fill='x',anchor='center')

fps=tk.StringVar(value='60')
e3=tk.Entry(window,textvariable=fps)
e3.pack(side='top',anchor='center')

#设备码(在控制台输入adb devices查看设备码)
lb6=tk.Label(window,text='设备码(点击查看设备按钮即可查看)',font=(12))
lb6.pack(side='top',fill='x',anchor='center')

#框体2
frm2=tk.Frame(window,width=3)
frm2.pack(side='top',anchor='center')

e4=tk.Entry(frm2)
e4.pack(side='left',anchor='center')

b2=tk.Button(frm2,text='查看设备',command=check_devices,height=1)
b2.pack(side='left')

#关闭手机屏幕
ckv=tk.StringVar()
ck=tk.Checkbutton(window,text='关闭手机屏幕',onvalue=' -S',offvalue='',variable=ckv)
ck.select()
ck.pack(side='top',anchor='center')

#按钮
b=tk.Button(window,text='开始投屏',command=start_screen_thread,width=10,height=1)
b.pack(side='bottom',fill='x')
window.bind('<Return>',start_screen_Enter)

window.mainloop()