'''
YOUTUBE CONTENT DOWNLOADER

Author - Mayank Bajaj

pip install pafy
'''

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.filedialog
import pafy

def b3():
    if urltext.get() == '':
        messagebox.showerror('Error', 'Please Enter a URL')
    else:
        vdownload = Label(ytcd, text='Downloading..', font=('arial', 13, 'bold')).place(x=20, y=320)
        url = urltext.get()
        vdo = pafy.new(url)
        if av.get() == 0:
            vbest = vdo.getbest(preftype='mp4')
            vbest.download(filepath=fgr.get())
        elif av.get() == 1:
            abest = vdo.getbestaudio(preftype='m4a')
            abest.download(filepath=fgr.get())
        tklg = Label(ytcd, image=img4).place(x=130, y=320)
        vdownload2 = Label(ytcd, text='Downloaded', font=('arial', 15, 'bold')).place(x=21, y=320)

def b2():
    fdr = tkinter.filedialog.askdirectory()
    vlocr = Label(ytcd, text=fdr, font=('arial', 13, 'bold')).place(x=155, y=260)
    vloc = Label(ytcd, text='Video Location : ', font=('arial', 13, 'bold')).place(x=20, y=260)


def b1():
    if urltext.get() == '':
        messagebox.showerror('Error', 'Please Enter a URL')
    else:
        url = urltext.get()
        vdo = pafy.new(url)
        streams = vdo.allstreams
        title = vdo.title
        vtitler = Label(ytcd, text=title, font=('arial', 13, 'bold')).place(x=120, y=200)
        vdurr = Label(ytcd, text=vdo.duration, font=('arial', 13, 'bold')).place(x=180, y=231)
        if av.get() == 0:
            vbest = vdo.getbest(preftype='mp4')
            v = round(vbest.get_filesize() * 0.000001, 2)
            dsizer = Label(ytcd, text=str(v) + ' MB', font=('arial', 13, 'bold')).place(x=115, y=170)
        elif av.get() == 1:
            abest = vdo.getbestaudio(preftype='m4a')
            a = round(abest.get_filesize() * 0.000001)
            dsizer = Label(ytcd, text=str(a) + ' MB', font=('arial', 13, 'bold')).place(x=115, y=170)

    dsize = Label(ytcd, text='Total Size : ', font=('arial', 13, 'bold')).place(x=20, y=170)
    vtitle = Label(ytcd, text='Video Title : ', font=('arial', 13, 'bold')).place(x=20, y=200)
    vdur = Label(ytcd, text='Content Duration : ', font=('arial', 13, 'bold')).place(x=20, y=230)

ytcd = Tk()
title = ytcd.title('YouTube Content Downloader')
ytcd.geometry('510x400')
ytcd.resizable(False, False)
ytcd.attributes()
ytcd.iconbitmap('YCD ICON.ico')

img = ImageTk.PhotoImage(Image.open(
    r'YCD IMG.png'))
ycdlogo = Label(ytcd, image=img).place(width=200, height=100)


img3 = ImageTk.PhotoImage(Image.open(
    r'Made by Mayank Bajaj.png'))
mbmb = Label(ytcd, image=img3).place(x=236, y=349)

img4 = ImageTk.PhotoImage(Image.open(
    r'Tick Logo.png'))

fgr = StringVar()
urltext = StringVar()
UrlEntry = Entry(ytcd, textvariable=urltext, font=('arial', 17, 'bold'), width=27).place(x=20, y=100)

b1 = Button(ytcd, text='Get Data', font=('Arial', 10, 'bold'), width=12, bd=4, command=b1).place(x=380, y=98)
b2 = Button(ytcd, text='Select Location', font=('Arial', 10, 'bold'), width=12, bd=4, command=b2).place(x=380, y=130)
b3 = Button(ytcd, text='Start Downloading', font=('Arial', 10, 'bold'), width=15, bd=4, command=b3).place(x=360,y=300)

av = IntVar()
audio = Radiobutton(ytcd, text='Video', value=0, variable=av).place(x=20, y=140)
video = Radiobutton(ytcd, text='Audio', value=1, variable=av).place(x=100, y=140)

ytcd.mainloop()
