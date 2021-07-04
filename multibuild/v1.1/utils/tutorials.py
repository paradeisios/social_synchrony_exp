from tkinter import *
from tkinter import filedialog
from psychopy import visual,event,core
from utils.constants import *
import os
import time

WIDTH = 1280
HEIGHT = 720


def gaze_tutorial():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(-1,-1,-1))

    image_instuctions = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[0]))

    while True:
        image_instuctions.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()

    #### slide 2
    text = visual.TextStim(win=win,text="סינכרון מבט מקסימלי הוא קשר עין ישיר בין הדמויות (למשל דמות א' מביטה ישירות בדמות ב', אשר גם מביטה ישירות בדמות א')",  
                           pos=(0,250),languageStyle= "RTL")  

    img1 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[1]),pos=(-300,0))
    img2 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[2]),pos=(300,0))
    line = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,-300),end=(300,-300),lineWidth=5,interpolate=True)
    circle = visual.Circle(win=win,radius=20,pos=(0,-300),fillColor="red",edges=128)

    text.draw()
    img1.draw()
    img2.draw()
    line.draw()
    circle.draw()
    win.flip()
    time.sleep(1)

    for i in range(40):
        circle.pos += (7,0)
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)
    
    while True:
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()

    #### slide 3
    text = visual.TextStim(win=win,text="בשלב הבא, סינכרון מבט גבוה קיים כאשר שתי הדמויות מביטות באותו אובייקט בו זמנית",  
                           pos=(0,250),languageStyle= "RTL")  
    img1.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[3])
    img1.pos = (0,0)
    circle.pos = (0,-300)

    for i in range(25):
        circle.pos += (7,0)
        text.draw()
        img1.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)

    while True:
        text.draw()
        img1.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()

    #### slide 4
    text = visual.TextStim(win=win,text="רמה נמוכה של סנכרון מבט היא כאשר דמות א' מביטה בדמות ב' ודמות ב' מסיטה את מבטה ונמנעת מיצירת קשר עין",  
                           pos=(0,250),languageStyle= "RTL")  
    img1.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[4])
    img2.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[5])
    img1.pos = (-300,0)
    img2.pos = (300,0)
    circle.pos = (0,-300)

    for i in range(25):
        circle.pos -= (7,0)
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)
    
    while True:
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()
    
    #### slide 5
    text = visual.TextStim(win=win,text="רמה נמוכה של סנכרון מבט היא כאשר דמות א' מביטה בדמות ב' ודמות ב' מסיטה את מבטה ונמנעת מיצירת קשר עין",  
                           pos=(0,250),languageStyle= "RTL")  
    img1.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[6])

    img1.pos = (0,0)
    circle.pos = (0,-300)

    for i in range(40):
        circle.pos -= (7,0)
        text.draw()
        img1.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)
    
    while True:
        text.draw()
        img1.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()
    
    win.close()
 
###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################


def touch_tutorial():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(-1,-1,-1))
    image_instuctions = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[0]))

    print("ok")
    while True:
        image_instuctions.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()

    #slide 2 

    text = visual.TextStim(win=win,text="סנכרון מגע מקסימלי מוגדר כאשר דמות א' ודמות ב' נוגעות זו בזו בו-זמנית. המגע הפיזי יכול להיות בקונטקסט חיובי (חיבוק) או  בקונטקסט שלילי (האבקות).",  
                           pos=(0,250),languageStyle= "RTL")  

    img1 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[1]),pos=(-800,0))
    img2 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[2]),pos=(-400,0))
    img3 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[3]),pos=(0,0))
    img4 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[4]),pos=(400,0))
    img5 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[5]),pos=(800,0))
    line = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,-300),end=(300,-300),lineWidth=5,interpolate=True)
    circle = visual.Circle(win=win,radius=20,pos=(0,-300),fillColor="red",edges=128)

    text.draw()
    img1.draw()
    img2.draw()
    img3.draw()
    img4.draw()
    img5.draw()
    line.draw()
    circle.draw()
    win.flip()
    time.sleep(1)

    for i in range(40):
        circle.pos += (7,0)
        text.draw()
        img1.draw()
        img2.draw()
        img3.draw()
        img4.draw()
        img5.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)
    
    while True:
        text.draw()
        img1.draw()
        img2.draw()
        img3.draw()
        img4.draw()
        img5.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()

    #slide 3

    text = visual.TextStim(win=win,text="רמה גבוהה של סנכרון מגע היא כאשר דמות א' נוגעת בדמות ב', אך דמות ב' אינה מנסה לגעת בדמות א'.",  
                           pos=(0,250),languageStyle= "RTL") 
    img1.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[6])
    img2.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[7])
    img3.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[8])
    circle.pos = (0,-300)
    img1.pos = (-500,0)
    img2.pos = (0,0)
    img3.pos = (500,0)

    text.draw()
    img1.draw()
    img2.draw()
    img3.draw()
    line.draw()
    circle.draw()
    win.flip()
    
    for i in range(25):
        circle.pos += (7,0)
        text.draw()
        img1.draw()
        img2.draw()
        img3.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)

    while True:
        text.draw()
        img1.draw()
        img2.draw()
        img3.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()
    

    #slide 4

    text = visual.TextStim(win=win,text="כאשר שתי הדמויות רוכנות זו אל זו אך אין מגע ישיר, רמת סנכרון המגע נמוכה",  
                           pos=(0,250),languageStyle= "RTL") 
    img1.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[9])
    img2.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[10])
    circle.pos = (0,-300)
    img1.pos = (-300,0)
    img2.pos = (300,0)

    text.draw()
    img1.draw()
    img2.draw()
    line.draw()
    circle.draw()
    win.flip()
    
    for i in range(25):
        circle.pos -= (7,0)
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)

    while True:
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()

    
    #slide 5

    text = visual.TextStim(win=win,text="כאשר על המסך מופיעה דמות אחת בלבד או כאשר הדמויות אינן נוגעות זו בזו, אין כלל סינכרון מגע.",  
                           pos=(0,250),languageStyle= "RTL") 
    img1.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[11])
    img2.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[12])
    circle.pos = (0,-300)
    img1.pos = (-300,0)
    img2.pos = (300,0)

    text.draw()
    img1.draw()
    img2.draw()
    line.draw()
    circle.draw()
    win.flip()
    
    for i in range(40):
        circle.pos -= (7,0)
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
        core.wait(.05)

    while True:
        text.draw()
        img1.draw()
        img2.draw()
        line.draw()
        circle.draw()
        win.flip()
    
        if len(event.getKeys())>0:
            break
        event.clearEvents()

    win.close()







###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################


def valence_arousal_tutorial():
    pass


###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################


def general_sync_instructions():
    
    win = visual.Window(size=[WIDTH, HEIGHT],units="pix",fullscr=False,color=(-1,-1,-1))
    
    img_path = os.path.join(os.getcwd(), "assets","pics", GENERAL)
    instructions = visual.ImageStim(win=win,image=img_path,size=[WIDTH, HEIGHT])

    while True:
        instructions.draw()
        win.flip()

        if len(event.getKeys())>0:
            break
        event.clearEvents()
    
    win.close()
    
    
