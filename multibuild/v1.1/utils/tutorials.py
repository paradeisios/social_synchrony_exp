from psychopy import visual,event,core
from utils.constants import *
import os
import time



def tutorial(exp=""):

    win = visual.Window(size=(WIDTH,HEIGHT),units="pix",fullscr=False,color=(-1,-1,-1))
    
    work_folder = os.path.join(os.getcwd(),"assets","pics",exp)
    pictures = [os.path.join(work_folder,file) for file in os.listdir(work_folder)]
    
    for picture in pictures:

        print(picture)
        event.clearEvents()
        slide = visual.ImageStim(win=win,image=picture)

        while True:
            
            slide.draw()
            win.flip()

            if len(event.getKeys(keyList=["right"])):
                break
            event.clearEvents()
    
    
    win.close()



