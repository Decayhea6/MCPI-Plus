### A Simple And Clean Importer Of Textures Into MCPI (minecraft pi) ###

# To Import Files, Click Browse and Find Your Texture. Then Hit import.#

#---You can always go back to the default texture by hitting default---#

import os

import shutil

global dir_path

dir_path = os.path.dirname(os.path.realpath(__file__))

from tkinter import *

from tkinter import filedialog

global location

location = ''

global texdesin

texdesin = '/opt/minecraft-pi/data/images'

#########################################################################

def findTex():
    window.directory = filedialog.askdirectory()
    global location
    location = window.directory + '/images'
    print('Location is: ' + location)
    
def defaultTex():
    global location
    location = os.path.dirname(os.path.realpath(__file__)) + '/images'
    print('Location is: ' + location)

def pastefile():
    print('Location is: ' + location)
    print('Destination is: ' + texdesin)
    #if os.path.isfile(texdesin):
    shutil.rmtree(texdesin)
    shutil.copytree(location, texdesin)
    #else:
        #shutil.copytree(location, texdesin)
    
#########################################################################
    
window = Tk()
window.title('Texture+')

#########################################################################

title = Label(window, font = 'Times', text = 'Texture +')
subtitle = Label(window, text = 'Simple Texture Importer for MCPI')
def_btn = Button(window, anchor = W, text = 'Use Original Pack', command = defaultTex)
browse = Button(window, anchor = E, text = 'Use Custom Pack', command = findTex)
Finish = Button(window, text = 'Import', command = pastefile)

#########################################################################

title.pack()
subtitle.pack()
def_btn.pack(side=LEFT)
browse.pack(side=RIGHT)
Finish.pack(side=BOTTOM)

##########################################################################

window.mainloop()

