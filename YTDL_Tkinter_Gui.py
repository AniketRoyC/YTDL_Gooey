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

ytdl_opts = {                                                   #dictionary of ytdl options (defaults are included here)
    'format':'mp3',                                  #best available audio format / best overall
    
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
    def __init__(self):

        self.root = Tk()

        #Variables
        self.VideoLink = StringVar() #video link 
        self.AudioFormat = StringVar() #Audio format

        self.addWidgets() #runs the actual widgets


    def addWidgets(self):
        #Basic Window Config
        self.root.title("YTDL Gooey")
        self.root.columnconfigure(0,   weight=1) #minsize=200,
        self.root.rowconfigure(0,  weight=1) #minsize=200,

        #FRAME1 --> Contains video link ===============
        frame1 = ttk.Labelframe(self.root, text = 'Video Link', padding ="3 3 10 10")
        frame1.grid(column=0, row=1, sticky=(N, W))

        

        #frame1['padding'] = (5,10) # Padding: 5px on L/R, 10px on Top/Bott
        
      
        #Video Link (Entry)
        LinkInput = ttk.Entry(frame1,
                        textvariable = self.VideoLink,
                        width = 75).grid(column=2, row=1, sticky = (E, W))

        #FRAME2 --> Basic Options ===============
        frame2 = ttk.Labelframe(self.root, text = 'Audio Options', padding = '3 3 10 10')
        frame2.grid(column=0, row=2, sticky = (E, W))

        #Audio FOrmat (ComboBox)
        AudFormatLabel = ttk.Label(frame2,
                        text = 'Format:').grid(column=1, row=1, sticky =E)
        AudFormat = ttk.Combobox(frame2,
                        textvariable = self.AudioFormat,
                        values = ('best', 'aac', 'flac', 'mp3', 'm4a', 'opus', 'vorbis', 'wav'),
                        width = 15).grid(column=2, row=1, sticky = (E,W))
        #Download Playlist (Checkbox)
        #PlaylistToggle = ttk.Radiobutton
        

     


    
    def ytdlOptions(self, opt, optconfig ):
        ytdl_opts['opt'] = optconfig    #replaces 'opt' with the optconfig in the dictionary

    def runGooey(self):
        self.root.mainloop()



window = YTDLGooey()
window.runGooey()


