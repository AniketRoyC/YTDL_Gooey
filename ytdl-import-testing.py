from __future__ import unicode_literals
import youtube_dl

#method for adding lines to keep ouput clean (probably will remove later)
def separator(seplength=45):
    separator = ''
    for i in range(0, seplength):
        separator = separator + '-'
    print(separator)

#logger that only outputs errors, (can also do debug and warnings)
class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

#prints status of ffmpeg/ytdl
def my_hook(d):
    # #TODO - see if 'downloadspam' fix is still necessary to GUI implementation
        # if d['status'] == 'downloading':
        #     print('\nDownloading...')

    if d['status'] == 'finished':
        print('Downloaded to ' + d['filename'] + '\n Converting...\n')

userdir = input("\nEnter directory to save downloads in:\n")
separator()
userlink = input("Link to convert: \n")
separator() 

#main options (secret sauce)
ytdl_opts = {
    'format':'bestaudio/best', #best available audio format / best overall
    'outtmpl': userdir + '\\' + 'vibecheck\\%(title)s.%(ext)s', #output location+template
    'restrictfilenames': True, #Do not allow "&" and spaces in file names
   
    'postprocessors': [{ #names post-processor + keyword arguments for it
        'key': 'FFmpegExtractAudio', #names postprocessor
        'preferredcodec': 'mp3', #self explanatory
        'preferredquality': '6', #320kbps
        }],
    
    'logger' : MyLogger(), #error logging (method made above) 
    'progress_hooks' : [my_hook], #progress logging (method made above)
    #'forcetitle': True, #forces printing title (irrelevant outside cmd)
}

#actually running ytdl with all the setup done
with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
    ydl.download([userlink])