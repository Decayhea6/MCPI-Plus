# the gui for the script to place blocks not in the minecraft inventory

from tkinter import *
import pickle
global blockId
blockId = 0
global Directory
Directory = {'blockdata': blockId}

def sendinfo():
    blockId = ID.get()
    datafile = open('BlockID.dat', 'wb')
    Directory = {'blockdata': blockId}
    pickle.dump(Directory, datafile)
    #print('sent')          #-=debuging
    #print(str(blockId))    #-=debuging
    



root = Tk()
root.title('Secret Block PLacer MCPI')
ID = IntVar()

R1 = Radiobutton(root, text="Water", variable=ID, value=8, command = sendinfo)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Lava", variable=ID, value=10, command = sendinfo)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Snow", variable=ID, value=78, command = sendinfo)
R3.pack( anchor = W)

R4 = Radiobutton(root, text="Glowing Obsidian", variable=ID, value=246, command = sendinfo)
R4.pack( anchor = W)

R5 = Radiobutton(root, text="Border Block", variable=ID, value=95, command = sendinfo)
R5.pack( anchor = W)

R6 = Radiobutton(root, text="?", variable=ID, value=255, command = sendinfo)
R6.pack( anchor = W)



mainloop()
