import tkinter as tk
import module.ytube_module as m
from tkinter import messagebox
from pytube import YouTube
import threading


def clickSearch():
    url = ytUrl.get()
    try:
        YouTube(url)
    except:
        messagebox.showerror('error')
        return
    urls = m.getUrls(url)
    if urls and messagebox.askyesno('pleace check','void is all download?(if no selected so one void download)'):
        print('Start list')
        for u in urls:
            threading.Thread(target=m.startDownload,args=(u,listbox)).start()
    else:
        yt= YouTube(url)
        if messagebox.askyesno('pleace check',f'is ok to download{yt.title}?'):
            threading.Thread(target=m.startDownload,args=(url,listbox)).start()
        else:
            print('cansel download')

windows = tk.Tk()
windows.geometry('640x480')
windows.title('Youtube Download')

inputFm = tk.Frame(windows,bg='black',width=640,height=120)
inputFm.pack()

lb = tk.Label(inputFm,text='please enter Youtube URL',bg='red',fg='white',font=('細明體',12))
lb.place(rely=0.25,relx=0.5,anchor='center')

ytUrl = tk.StringVar()
entry=tk.Entry(inputFm,textvariable=ytUrl,width=50)
entry.place(rely=0.5,relx=0.5,anchor='center')


inputButton = tk.Button(inputFm,text='Download',command=clickSearch,bg='red',fg='Black',font=('細明體',10))
inputButton.place(rely=0.5,relx=0.85,anchor='center')


downLoadForm = tk.Frame(windows,width=500,height=480-120,)
downLoadForm.pack()

lb = tk.Label(downLoadForm,text='Download Status',fg='black',font=('細明體',10))
lb.place(rely=0.1,relx=0.5,anchor='center')

listbox = tk.Listbox(downLoadForm,width=65,height=15)
listbox.place(rely=0.5,relx=0.5,anchor='center')


sbar = tk.Scrollbar(downLoadForm)
sbar.place(rely=0.5,relx=1,anchor='center',relheight=0.7)

#將捲動軸設置為垂直並放入listbox裡
listbox.config(yscrollcommand=sbar.set)

#將此捲動軸連結至listbox
sbar.config(command=listbox.yview)

windows.mainloop()