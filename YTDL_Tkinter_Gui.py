from __future__ import unicode_literals
import youtube_dl
from tkinter import *
from tkinter import ttk


class YTDLGooey:
    def __init__(self, root):

        #Window Title
        root.title("YTDL Gooey")

        #Main Window
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)





