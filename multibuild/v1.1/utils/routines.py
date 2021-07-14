from tkinter import *
from tkinter import filedialog
from utils.tutorials import *




def select_movie():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path



def specify_experiment_phase():
    
    root = Tk()
    root.title("Social Synchrony Exp v1.1")

    gaze_button = Button(root,text="Gaze Synchrony",width=50,height=2,command=lambda x: tutorial_loop("gaze"))
    touch_button = Button(root, text="Touch Synchrony ",width=50,height=2,command=lambda x: tutorial_loop("touch"))
    arousal_button = Button(root, text="Valence/Arousal",width=50,height=2,command=lambda x: tutorial_loop("valance"))
    id_button =  Button(root,text="Identification",width=50,height=2,command=lambda x: tutorial_loop("id"))
    general_sync_button = Button(root,text="General Synchrony Button",width=50,height=2,command=lambda x: tutorial_loop("general"))

    gaze_button.grid(row=0,column=0)
    touch_button.grid(row=1,column=0)
    arousal_button.grid(row=2,column=0)
    id_button.grid(row=3,column=0)
    general_sync_button.grid(row=4,column=0)

    root.mainloop()
