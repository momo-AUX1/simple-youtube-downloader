import tkinter as tk
from tkinter import ttk 
import os
from tkinter import messagebox
import pytube 
from pytube import YouTube

app = tk.Tk()
app.title("YT DOWNLOADER")
app.config(height=360,width=560)




L1 = ttk.Label(
    app,
    text="YOUTUBE DOWNLOADER VER 0.1 AUDIO ONLY",
    font="roboto",
    background="red"
)


E1 = ttk.Entry(
    app,
    width=70
)


def C1():
    text = E1.get()
    YT = YouTube(text)
    AU = YT.streams.filter(only_audio=True).first()
    AU.download(filename=YT.title + ".mp3")
    messagebox.showinfo("audio downloaded","check the folder")



def C2():
    text = E1.get()
    YT = YouTube(text)
    AU = YT.streams.filter(only_video=True).first()
    AU.download(filename=YT.title+".mp4")
    messagebox.showinfo("video downloaded","check the folder")


    


B1 = ttk.Button(
    app,
    text = "download audio",
    command = C1
)

B2 = ttk.Button(
    app,
    text = "download video",
    command = C2,
    state = "disabled"
)

B2.place(x=290,y=170)
B1.place(x=165,y=170)
E1.place(x=65,y=90)
L1.place(x=100,y=50)
app.mainloop()