from psychopy import core,event,visual
from constants import *
import time
import os


def social_sync_visual():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(-1,-1,-1))
    text = visual.TextStim(win=win,text="הזדהות",  pos=(0,150),languageStyle= "RTL")
    text2 = visual.TextStim(win=win,
             text='''אתם עומדים לצפות בקטע וידאו קצר המתאר אינטראקציה חברתית. אנא דרגו בעזרת הסליידר את רמת סנכרון המגע בין הדמויות על סקאלה מ"ללא סנכרון מבט כלל" ועד ל"סנכרון מבט מקסימלי".''',
            pos=(0,-100),
            languageStyle= "RTL")

    img1 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[0]),pos=(-100,-100))
    img2 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[1]),pos=(100,-100))

    text.draw()
    text2.draw()
    win.flip()
    time.sleep(2)

    #### slide 1
    text = visual.TextStim(win=win,text="סינכרון מבט מקסימלי הוא קשר עין ישיר בין הדמויות (למשל דמות א' מביטה ישירות בדמות ב', אשר גם מביטה ישירות בדמות א')",  
                           pos=(0,250),languageStyle= "RTL")  

    img1 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[0]),pos=(-300,0))
    img2 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[1]),pos=(300,0))
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
    
    time.sleep(1)

    #### slide 2
    text = visual.TextStim(win=win,text="בשלב הבא, סינכרון מבט גבוה קיים כאשר שתי הדמויות מביטות באותו אובייקט בו זמנית",  
                           pos=(0,250),languageStyle= "RTL")  
    img1.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[2])
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

    time.sleep(1)

    #### slide 3

    win.close()

    
#social_sync_visual()










def social_sync_touch():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(1,1,1))

def grid_visual():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(1,1,1))

def grid_touch():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(1,1,1))
