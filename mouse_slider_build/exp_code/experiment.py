# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 17:51:26 2021

@author: Paradeisios
"""

from psychopy import visual,core,logging,constants,event
import numpy as np
import sys

def experiment(win,exp_video,log_data):
    
    """ The main experiment. Works by 
    1. Creating a logger text that record timestap and rating for each frame (approximately)
    2. Projects the movie and the slider on the screen
    3. Keeps playing the movie and updating the slider 
    4. If subject hits q, movie will close  """
    

    log = ""
    log += f"Name, {log_data[0]}\n"
    log += f"Age,{log_data[1]}\n"
    log += "Timestap,Rating\n"
    clock = core.Clock()
    
    text = visual.TextStim(win=win)
    text.text = "Loading experiment movie..."
    text.draw()
    win.flip()
    

    mov = visual.MovieStim3(win=win,filename=exp_video)

    mov.size /= 2
    mov.size = np.round(mov.size)
    x = 0
    y = win.size[1]/2 - mov.size[1]/2
    mov.pos = (x,y)
    
    
    line = visual.Line(win=win,
                       lineColor=[1, 1, 1],
                       start=(-300,-200),
                       end=(300,-200),
                       lineWidth=5,
                       interpolate=True)
    
    circle = visual.Circle(win=win,
                       radius=20,
                       pos=(0,-200),
                       fillColor="red",
                       edges=128)
    
    mouse = event.Mouse(win=win,visible=True)
 
    text.text="Move the slider by moving the mouse\nPress space to begin\nPress q to exit the experiment"
    text.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    
    for i in range(3,0,-1):
        text.text = i
        text.draw()
        win.flip()
        core.wait(1)
        
    clock.reset()
    mouse.setPos(newPos=(0, -200))
    mouse.setVisible(1)
    log += f"{np.round(clock.getTime(),3)},{circle.pos[0]}\n"
    while mov.status != constants.FINISHED:
        line.draw()
        circle.draw()
        mov.draw()
        win.flip()
        if mouse.getPos()[0] < 300 and mouse.getPos()[0] > -300:
            circle.pos = (mouse.getPos()[0],-200)
        log +=f"{np.round(clock.getTime(),3)},{circle.pos[0]}\n"
        
        if len(event.getKeys(keyList=["q"]))>0:
            log += f"{np.round(clock.getTime(),3)},Experiment ended before movie end"
            break
        
    mov.stop()
    win.close()
    
    with open(f"{log_data[0]}_movie_output.txt","w") as logger:
        logger.write(log)
     
    sys.exit()

