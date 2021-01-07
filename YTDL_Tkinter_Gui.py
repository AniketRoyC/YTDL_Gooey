from __future__ import unicode_literals
import youtube_dl
from tkinter import *
from tkinter import ttk


class YTDLGooey:
    def __init__(self, root):

        #Window Title
        root.title("YTDL Gooey")

        #FRAME1 --> Will contain all the video information
            #the actual link, playlist yes/no
        frame1 = ttk.Labelframe(root, text = 'Video Information', padding ="3 3 12 12")
        frame1.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        LinkLabel = ttk.Label(frame1, text = 'Video Link:').grid(column=1, row=1, sticky = W)

        #Variables


root = Tk()
YTDLGooey(root)
root.mainloop()

