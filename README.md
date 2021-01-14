# YTDL_Gooey
Tkinter-based Python GUI for Youtube-DL

Based on the Youtube DL Python module.
I could have chosen to make a GUI that passes commands to the ```.exe``` version of the program, but I chose to implement it entirely in Python as a challenge.

## Development Blog 

**11-Jan-21**

This was more of a challenge than I thought. I basically know nothing about this kind of programming. I've done data science stuff before, but never anything remotely like this. So far, I have a window with a box for the link. We'll see how this goes.

**13-Jan-21**

Finally got some quality development time in today. Got the basics going. For now, I'll keep going at the GUI part of things, and leave the YTDL part of it for later. Shouldn't be too complicated (refer to ```ytdl-import-testing.py``` for more info).

**13-Jan-21**
Part 2: (```StringVar``` machine broke B)

For some godforsaken reason, having the Filepath display as a ```Label``` just completely refused to function. Changed it to an ```Entry```, and the exact same code worked perfectly. If someone reads this in the future and knows why, please tell me. I wasted 20% of today's coding time on this.
I guess you can enter filenames manually now too if you want, as a consequencey of the entry.

## Conventions

Padding - add it to the ```.grid``` command

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Frames/LabelFrames (i.e frame1, frame2, etc) = 5px
   
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Everything else (i.e. within numbered frames) = 3px 
        

```<something> = <something>``` for **EVERYTHING** with an equals sign
