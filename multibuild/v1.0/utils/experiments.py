from psychopy import visual,core,logging,constants,event
import numpy as np
import sys,os
from utils.constants import *
import random, string

def social_sync_visual_experiment(demographics_data):

    log = ""
    log += f"Name,{demographics_data[0]}\n"
    log += f"Age,{demographics_data[1]}\n"
    log += f"Gender,{demographics_data[2]}\n"
    log += f"Seen,{demographics_data[3]}\n"
    log += f"Birth,{demographics_data[4]}\n"
    log += f"Exp_with_coding,{demographics_data[5]}\n"
    log += f"Education,{demographics_data[6]}\n"

    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(-1,-1,-1))
    text = visual.TextStim(win=win,text="Loading experiment movie...")
    text.draw()
    win.flip()

    moviefile = os.path.join(os.getcwd(), "assets","movies", VIDEOS[0])
    movie = visual.MovieStim3(win=win,filename=moviefile)
    movie.size /= 1.5
    movie.size = np.round(movie.size)
    x = 0
    y = win.size[1]/2 - movie.size[1]/2
    movie.pos = (x,y)

    # tqdm progress    
    video_tracker_bg = visual.Rect(win=win,
                                   lineColor="green",
                                   fillColor="black",
                                   pos=(0,-350),
                                   width=400,
                                   height=20)
    
    video_tracker_tqdm = visual.Rect(win=win,
                                   lineColor="green",
                                   fillColor="green",
                                   pos=(-200,-350),
                                   width=1,
                                   height=20)
    
    tqdm_text = visual.TextStim(win=win,
                                text=f"{movie.getCurrentFrameTime()}/{movie.duration}",
                                pos = (280,-350))

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
        
        video_tracker_bg.draw()
        curr_perc = movie.getCurrentFrameTime() * movie.duration / 100 
        x = -200 + curr_perc
        video_tracker_tqdm.pos=(x,-350)
        width = curr_perc*2
        video_tracker_tqdm.width=width
        video_tracker_tqdm.draw()
        tqdm_text.text = f"{np.round(movie.getCurrentFrameTime(),1)}/{movie.duration}"
        tqdm_text.draw()
        
        start_button.draw()
        stop_button.draw()
        
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
    fname = os.path.join(os.getcwd(),"output",random_ascii+"_movie_output.txt")

    with open(fname,"w") as logger:
        logger.write(log)

    os.path.join(os.getcwd(), "output","pics", GAZE_IMG[0])
def grid_experiment():
    pass
