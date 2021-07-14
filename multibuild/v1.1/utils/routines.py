from tkinter import *
from tkinter import filedialog
from psychopy import gui
from utils.tutorials import *
from utils.experiments import *




def select_movie():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path



def specify_experiment_phase(movie_fname,demographics_data):
    
    root = Tk()
    root.title("Social Synchrony Exp v1.1")

    gaze_button = Button(root,text="Gaze Synchrony",width=50,height=2,command=lambda: tutorial("gaze"))
    touch_button = Button(root, text="Touch Synchrony ",width=50,height=2,command=lambda: tutorial("touch"))
    arousal_button = Button(root, text="Valence/Arousal",width=50,height=2,command=lambda: tutorial("valance"))
    id_button =  Button(root,text="Identification",width=50,height=2,command=lambda: tutorial("id"))
    general_sync_button = Button(root,text="General Synchrony",width=50,height=2,command=lambda: tutorial("general"))

    gaze_exp = Button(root,text="Gaze Experiment",width=50,height=2,command = lambda: sync_experiment(demographics_data,movie_fname))
    touch_exp = Button(root, text="Touch Experiment",width=50,height=2, command=lambda: sync_experiment(demographics_data,movie_fname))
    arousal_exp = Button(root, text="Valence/Arousal Experiment",width=50,height=2,command=lambda: arousal_experiment(demographics_data,movie_fname))
   
    gaze_button.grid(row=0,column=0)
    touch_button.grid(row=1,column=0)
    arousal_button.grid(row=2,column=0)
    id_button.grid(row=3,column=0)
    general_sync_button.grid(row=4,column=0)

    gaze_exp.grid(row=5,column=0)
    touch_exp.grid(row=6,column=0)
    arousal_exp.grid(row=7,column=0)
    
    root.mainloop()
 
 

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


        