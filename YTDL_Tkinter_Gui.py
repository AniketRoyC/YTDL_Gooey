from __future__ import unicode_literals
import youtube_dl
from tkinter import *
from tkinter import ttk

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        #print(msg) TODO: Add status bar near bottom to display logger

ytdl_opts = { 
    'format':'bestaudio/best',                                  #best available audio format / best overall
    'outtmpl': '',#TODO add file location option                #output location+template
    'restrictfilenames': True,                                  #Do not allow "&" and spaces in file names
   
    'postprocessors': [{                                        #names post-processor + keyword arguments for it
        'key': 'FFmpegExtractAudio',                            #names postprocessor
        'preferredcodec': 'mp3',                                #self explanatory
        'preferredquality': '320',                              #320kbps
        }],
    
    'logger' : MyLogger(),                                      #error logging (method made above) 
    'progress_hooks' : [my_hook],                               #progress logging (method made above)

    }

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

    def ytdlOptions(self, opt, optconfig ):
        pass




root = Tk()
YTDLGooey(root)
root.mainloop()

