from tkinter import *
import pickle
global blockId
blockId = 0
global Directory
Directory = {'blockdata': blockId}

def sendinfo():
    blockId = ID.get()
    datafile = open('ParticleType.dat', 'wb')
    Directory = {'blockdata': blockId}
    pickle.dump(Directory, datafile)
    #print('sent')          #-=debuging
    #print(str(blockId))    #-=debuging
    



root = Tk()
root.title('Particle+ Editor')
ID = IntVar()

R0 = Radiobutton(root, text="Off", variable=ID, value=0, command = sendinfo)
R0.pack( anchor = W)

R1 = Radiobutton(root, text="Dandelion", variable=ID, value=37, command = sendinfo)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Lily", variable=ID, value=38, command = sendinfo)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Red Mushroom", variable=ID, value=40, command = sendinfo)
R3.pack( anchor = W)

R4 = Radiobutton(root, text="Brown Mushroom", variable=ID, value=39, command = sendinfo)
R4.pack( anchor = W)

R5 = Radiobutton(root, text="Cactus", variable=ID, value=81, command = sendinfo)
R5.pack( anchor = W)

R5 = Radiobutton(root, text="Torch", variable=ID, value=50, command = sendinfo)
R5.pack( anchor = W)

R6 = Radiobutton(root, text="Snow", variable=ID, value=78, command = sendinfo)
R6.pack( anchor = W)
mainloop()
