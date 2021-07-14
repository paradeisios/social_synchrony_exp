
from psychopy import visual,core,logging,constants,event
import numpy as np
import sys,os

from wx.core import Width
from utils.constants import *
import random, string


def sync_experiment(demographics_data,movie_fname):
    
    log = ""
    log += f"Name,{demographics_data[0]}\n"
    log += f"Age,{demographics_data[1]}\n"
    log += f"Gender,{demographics_data[2]}\n"
    log += f"Seen,{demographics_data[3]}\n"
    log += f"Birth,{demographics_data[4]}\n"
    log += f"Exp_with_coding,{demographics_data[5]}\n"
    log += f"Education,{demographics_data[6]}\n"
    log += "Time,X"

    win = visual.Window(size=(WIDTH,HEIGHT),units="pix",color=(-1,-1,-1))
    text = visual.TextStim(win=win,text="Loading experiment movie...")
    text.draw()
    win.flip()

    movie = visual.MovieStim3(win=win,filename=movie_fname)
    movie.size /= 1.5
    movie.size = np.round(movie.size)
    x = 0
    y = win.size[1]/2 - movie.size[1]/2
    movie.pos = (x,y)

  

    ####### stop and play buttons
    start_image = os.path.join(os.getcwd(), "assets","pics", BUTTONS[0])
    stop_image =  os.path.join(os.getcwd(), "assets","pics", BUTTONS[1])
    
    start_button = visual.ImageStim(win=win,
                                    image=start_image,
                                    pos=(-350,-350),
                                    size=(50,50))
    stop_button  = visual.ImageStim(win=win,
                                    image=stop_image,
                                    pos=(-280,-350),
                                    size=(50,50))
    line = visual.Line(win=win,
                       lineColor=[1, 1, 1],
                       start=(-300,-450),
                       end=(300,-450),
                       lineWidth=5,
                       interpolate=True)
    
    circle = visual.Circle(win=win,
                           radius=20,
                           pos=(0,-450),
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
        
    mouse.setPos(newPos=(0, -450))
    mouse.setVisible(1)
    
    paused = False
    
    while movie.status != constants.FINISHED:
        line.draw()
        circle.draw()
        movie.draw()
        win.flip()
        
        if mouse.isPressedIn(stop_button):
            movie.pause()
            paused = True
            
                
        if mouse.isPressedIn(start_button):
            movie.play()
            paused = False
 
    
           
        if (mouse.getPos()[0] < 300) and (mouse.getPos()[0] > -300) and not paused:
            circle.pos = (mouse.getPos()[0],-450)
            log +=f"{np.round(movie.getCurrentFrameTime(),3)},{circle.pos[0]}\n"
    
        
        if len(event.getKeys(keyList=["q"]))>0:
            log += f"{np.round(movie.getCurrentFrameTime(),3)},Experiment ended before movie end"
            break
        
    movie.stop()
    win.close()

    random_ascii = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    fname = os.path.join(os.getcwd(),"output","sync",random_ascii+"_movie_output.txt")
    print(fname)

    with open(fname,"w") as logger:
        logger.write(log)


def arousal_experiment(demographics_data,movie_fname):
    
    log = ""
    log += f"Name,{demographics_data[0]}\n"
    log += f"Age,{demographics_data[1]}\n"
    log += f"Gender,{demographics_data[2]}\n"
    log += f"Seen,{demographics_data[3]}\n"
    log += f"Birth,{demographics_data[4]}\n"
    log += f"Exp_with_coding,{demographics_data[5]}\n"
    log += f"Education,{demographics_data[6]}\n"
    log += "Time,X,Y\n"

    win = visual.Window(size=(WIDTH,HEIGHT),units="pix",color=(-1,-1,-1))

    text = visual.TextStim(win=win,text="Loading experiment movie...")
    text.draw()
    win.flip()

    arousal_grid = os.path.join(os.getcwd(), "assets","pics", AROUSAL)
    pic = visual.ImageStim(win=win,image= arousal_grid,size=(500,500),pos=(-360,0))
    mov = visual.MovieStim3(win=win,filename=movie_fname,size=(500,400),pos=(360,0))
    pointer = visual.Circle(win=win,pos=(0,0),units="pix",radius=10,fillColor=[1, -1, -1],edges=128,opacity=.8)

    mouse = event.Mouse(win=win,visible=True)

    start_image = os.path.join(os.getcwd(), "assets","pics", BUTTONS[0])
    stop_image =  os.path.join(os.getcwd(), "assets","pics", BUTTONS[1])
    start_button = visual.ImageStim(win=win,image=start_image,pos=(280,-350),size=(70,70))
    stop_button  = visual.ImageStim(win=win,image=stop_image,pos=(450,-350),size=(70,70))

    text.text="Move the slider by moving the mouse\nPress space to begin\nPress q to exit the experiment"
    text.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    
    for i in range(3,0,-1):
        text.text = i
        text.draw()
        win.flip()
        core.wait(1)
        
    mouse.setPos(newPos=(-180, 0))
    mouse.setVisible(1)
    
    paused = False

    while mov.status != constants.FINISHED: 

        pointer.pos = mouse.getPos()
        
        if pointer.pos[0] < -610:
            pointer.pos[0] = -610
        if pointer.pos[0] > -105:
            pointer.pos[0] = -105
        if pointer.pos[1] > 250:
            pointer.pos[1] = 250
        if pointer.pos[1] < -250:
            pointer.pos[1] = -250
        
        start_button.draw()
        stop_button.draw()
        pic.draw()
        mov.draw()
        pointer.draw()
        win.flip()
        
        if len(event.getKeys(keyList=["q"]))>0:
            break

        if mouse.isPressedIn(stop_button):
            mov.pause()
            paused = True
        
            
        if mouse.isPressedIn(start_button):
            mov.play()
            paused = False
            event.clearEvents()
        
        if (mouse.getPos()[0] < 300) and (mouse.getPos()[0] > -300) and not paused:
            log +=f"{np.round(mov.getCurrentFrameTime(),3)},{pointer.pos[0]},{pointer.pos[1]}\n"

        if len(event.getKeys(keyList=["q"]))>0:
            log += f"{np.round(mov.getCurrentFrameTime(),3)},Experiment ended before movie end"
            break
        

    mov.stop()
    win.close()

    random_ascii = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    fname = os.path.join(os.getcwd(),"output","arousal",random_ascii+"_movie_output.txt")
    print(fname)

    with open(fname,"w") as logger:
        logger.write(log)
