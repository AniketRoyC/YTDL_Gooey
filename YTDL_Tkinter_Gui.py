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
        pass
        #print(msg) TODO: Add logger functionality

def my_hook(d):
    if d['status'] == 'finished':
        print('Downloaded to ' + d['filename'] + '\n Converting...\n')
        #TODO add a status display (botttom or file-by-file?)

ytdl_opts = {                                                   #dictionary of ytdl options
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
        #Variables
        VideoLink = StringVar() #video link variable

    
    def GooeyGUI(self, root):
        
        #Window Title
        root.title("YTDL Gooey")

        #FRAME1 --> Will contain all the video information
            #Extract Audio (Checkbox)
        frame1 = ttk.Labelframe(root, text = 'Video Information', padding ="3 3 12 12")
        frame1.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, minsize=300,  weight=1)
        root.rowconfigure(0, minsize=300, weight=1)
        frame1['padding'] = (5,10) # Padding: 5px on L/R, 10px on Top/Bott
        
        #Not sure what these two are actually doing
        #frame1['width'] = 300
        #frame1['height'] = 300 

        LinkLabel = ttk.Label(frame1, 
                        text = 'Video Link:').grid(column=1, row=1, sticky = E)

        #Video Link (Entry)
        LinkInput = ttk.Entry(frame1,
                        textvariable = VideoLink,
                        width = 75).grid(column=2, row=1, sticky = (E, W))

        #Download Playlist (Checkbox)
        #PlaylistToggle = ttk.Radiobutton
        


    def ytdlOptions(self, opt, optconfig ):
        ytdl_opts['opt'] = optconfig    #replaces 'opt' with the optconfig in the dictionary




root = Tk()
YTDLGooey.GooeyGUI(root)
root.mainloop()

