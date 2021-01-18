from __future__ import unicode_literals
import youtube_dl
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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
        self.root.minsize(375, 375)

        #Variables
        self.VideoLink = StringVar() #video link 
        self.AudioFormat = StringVar() #Audio format
        self.AudioQuality = StringVar() #Audio Bitrate

        self.Filepath = StringVar(value = os.getcwd()) #Default download Location
        print('constructor check')
        print(self.Filepath.get())

        self.addWidgets() #runs the actual widgets



 
    def addWidgets(self):
        #Basic Window Config
        self.root.title("YTDL Gooey")
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)

        #=======================================================================================
        #FRAME1 --> Contains video link ===============
        frame1 = ttk.Labelframe(self.root, text = 'Video Link', padding = 5)
        frame1.grid(column = 0, row = 1, sticky = (N, E, W))
       
        frame1.columnconfigure(0, weight = 1)

        #Video Link (Entry)
        LinkInput = ttk.Entry(frame1,
                        textvariable = self.VideoLink,
                        width = 55)
        LinkInput.grid(column = 0, row = 1, sticky = (E, W))


        #=======================================================================================
        #FRAME2 --> Basic Options 
        frame2 = ttk.Labelframe(self.root, text = 'Audio Options', padding = 5)
        frame2.grid(column = 0, row = 2, sticky = (N, E, W))
        
        frame2.columnconfigure(0, weight = 0)
        frame2.columnconfigure(1, weight = 1)
        frame2.columnconfigure(2, weight = 0)
        frame2.columnconfigure(3, weight = 1)

        #Audio Format (ComboBox)
        AudFormatLabel = ttk.Label(frame2,
                        text = 'File format:',
                        padding = 3)
        AudFormatLabel.grid(column = 0, row = 1, sticky = E)
        
        AudFormat = ttk.Combobox(frame2,
                        textvariable = self.AudioFormat,
                        values = ('best', 'aac', 'flac', 'mp3', 'm4a', 'opus', 'vorbis', 'wav'),
                        width = 8)
        AudFormat.grid(column = 1, row = 1, sticky = (E,W))


        #Audio Quality (Entry)
        AudQualityLabel = ttk.Label(frame2,
                                text = "Quality:",
                                padding = 3)
        AudQualityLabel.grid(column = 2, row = 1, sticky = (E,W))

        AudQuality = ttk.Entry(frame2,
                            textvariable = self.AudioQuality,
                            width = 8)
        AudQuality.grid(column = 3, row = 1, sticky = (E,W), padx = 3, pady = 3)

        #FRAME3 --> Help notice, Apply/Run Buttons  (Always at the bottom) ====================
        #TODO add button to open instructions window
        frame3 = ttk.Frame(self.root, padding = 5)
        frame3.grid(column = 0, row = 4, sticky = (N, E, W))
        
        frame3.columnconfigure(0, weight = 1)
        frame3.columnconfigure(1, weight = 1)
        frame3.columnconfigure(2, weight = 1)

        #Options Notice
        OptionsNotice = ttk.Label(frame3,
                            text = '(For more information/instructions, refer to Help)')
        OptionsNotice.grid(column = 0, row = 0)    
        OptionsNotice['font'] = 'TkSmallCaptionFont'

        #Separator - b/w Options Notice and Apply Button
        s_frame3 = ttk.Separator(frame3,
                            orient = VERTICAL)
        s_frame3.grid(column = 1, row = 0, rowspan = 1, sticky = 'ns', padx = 5)

        #Apply Button - Updates all values for the ytdl_opts dictionary. Also checks for invalid entries
        ApplyButton = ttk.Button(frame3,
                        text = "Apply",
                        command = self.ytdlOptions)
        ApplyButton.grid(column = 2, row = 0, sticky = E)


        #FRAME4 --> FilePath ==================================================================
        frame4 = ttk.LabelFrame(self.root, text = 'File Options', padding = 5)
        frame4.grid(column = 0, row = 3, sticky = (N, W, E))
       
        frame4.columnconfigure(0, weight = 1)
        
        FileLocLabel = ttk.Label(frame4,
                            text = 'Save Location:')
        FileLocLabel.grid(column = 0, row = 0, sticky = W)
        
        #FileLocation --> DialogBox
        FileLocDisp = ttk.Entry(frame4,
                                textvariable = self.Filepath,
                                width = 55)
        FileLocDisp.grid(column = 0, row = 1, sticky = (W,E), padx = 3, pady = 3)

        FileLocButton = ttk.Button(frame4,
                            text = 'Change',
                            command = self.ChangeFilepath)
        FileLocButton.grid(column = 1, row = 1, sticky = E)                            

        #======================================================================================
        #Download Playlist (Checkbox)
        #PlaylistToggle = ttk.Radiobutton
        
    
             
    def ChangeFilepath(self):
        
        # bruh = ''
        # bruh = (filedialog.askdirectory())

        self.Filepath.set(filedialog.askdirectory())
        
        
        # print(bruh)
        print('Change Directory Check')
        print(self.Filepath.get())
        
    
    def ytdlOptions(opt = 'bruh', optconfig = 'moment' ):
        #ytdl_opts['opt'] = optconfig    #replaces 'opt' with the optconfig in the dictionary
        pass

    def runGooey(self):
        self.root.mainloop()

    def Download():
        pass



window = YTDLGooey()
window.runGooey()


