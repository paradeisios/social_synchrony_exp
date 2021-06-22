from psychopy import gui
from tkinter import *
from tutorials import *
from experiments import *


def demographics():

    log_gui = gui.Dlg(title="Social Synchrony Pilot")

    log_gui.addField("Name:")
    log_gui.addField("Age:")
    log_gui.addField("Gender:", choices=["M","F","Other"])
    log_gui.addField("Have you seen the movie before:", choices=["Y","N"])
    log_gui.addField("Date of birth (dd/mm/yyyy):")
    log_gui.addField("Do you have any experience with behavioral coding:", choices=["Y","N"])
    log_gui.addField("Educational Level:",choices=["Highschool","BA","MA","PhD","Engineering Degree"])

    log_data = log_gui.show()  
    if log_gui.OK: 
        print(log_data)
    else:
        print('user cancelled')
    
    return log_data

def checker():
    pass

def specify_experiment(demographics_data):

    root = Tk()
    root.title("Social Synchrony Exp v1.0")
        
    def ask_which_slider():

            root2 = Tk()
            visual_tutorial = Button(root2,text="Visual Tutorial",padx=20,pady=20,command=social_sync_visual_tutorial)
            visual_experiment = Button(root2,text="Visual Synchrony Experiment",padx=20,pady=20,
                                       command=lambda: social_sync_visual_experiment(demographics_data))
            touch_tutorial = Button(root2,text="Touch Tutorial",padx=20,pady=20,command=social_sync_touch_tutorial)
            touch_experiment = Button(root2,text="Touch Synchrony Experiment",padx=20,pady=20,command=checker)
            visual_tutorial.grid(row=0,column=0)
            visual_experiment.grid(row=0,column=1)
            touch_tutorial.grid(row=1,column=0)
            touch_experiment.grid(row=1,column=1)
            root2.mainloop()

    def ask_which_grid():

            root2 = Tk()
            visual_tutorial = Button(root2,text="Visual Tutorial",padx=20,pady=20,command=checker)
            visual_experiment = Button(root2,text="Visual Synchrony Experiment",padx=20,pady=20,command=checker)
            touch_tutorial = Button(root2,text="Touch Tutorial",padx=20,pady=20,command=checker)
            touch_experiment = Button(root2,text="Touch Synchrony Experiment",padx=20,pady=20,command=checker)
            visual_tutorial.grid(row=0,column=0)
            visual_experiment.grid(row=0,column=1)
            touch_tutorial.grid(row=1,column=0)
            touch_experiment.grid(row=1,column=1)
            root2.mainloop()

    button_slider = Button(root,
                           text="Social Synchrony Experiment",
                           padx=20,
                           pady=20,
                           command=ask_which_slider)

    button_grid = Button(root,
                         text="Arousal/Emotion Experiment",
                         padx=20,
                         pady=20,
                         command=ask_which_grid)

    button_slider.grid(row=0,column=0)
    button_grid.grid(row=0,column=1)
    root.mainloop()



