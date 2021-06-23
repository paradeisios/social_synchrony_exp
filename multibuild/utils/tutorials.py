from psychopy import core,event,visual
from utils.constants import *
import time
import os




def social_sync_visual_tutorial():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(-1,-1,-1))

    text = visual.TextStim(win=win,text="הזדהות",  pos=(0,150),languageStyle= "RTL")
    text2 = visual.TextStim(win=win,
            text='''אתם עומדים לצפות בקטע וידאו קצר המתאר אינטראקציה חברתית. אנא דרגו בעזרת הסליידר את רמת סנכרון המגע בין הדמויות על סקאלה מ"ללא סנכרון מבט כלל" ועד ל"סנכרון מבט מקסימלי".''',
            pos=(0,-100),
            languageStyle= "RTL")


    text.draw()
    text2.draw()
    win.flip()
    time.sleep(5)

    #### slide 2
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

    #### slide 3
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

    #### slide 4
    text = visual.TextStim(win=win,text="רמה נמוכה של סנכרון מבט היא כאשר דמות א' מביטה בדמות ב' ודמות ב' מסיטה את מבטה ונמנעת מיצירת קשר עין",  
                           pos=(0,250),languageStyle= "RTL")  
    img1.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[3])
    img2.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[4])
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
    time.sleep(1)
    
    #### slide 5
    text = visual.TextStim(win=win,text="רמה נמוכה של סנכרון מבט היא כאשר דמות א' מביטה בדמות ב' ודמות ב' מסיטה את מבטה ונמנעת מיצירת קשר עין",  
                           pos=(0,250),languageStyle= "RTL")  
    img1.image=os.path.join(os.getcwd(), "assets","pics", GAZE_IMG[5])

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
    
    time.sleep(1)
    ####identification slide

    text = visual.TextStim(win=win,text="הזדהות",  
                           pos=(0,450),languageStyle= "RTL")
    text2 = visual.TextStim(win=win,text='''אתם עומדים לצפות בקטע וידאו קצר המתאר אינטראקציה חברתית. אנא דרגו בעזרת הסליידר עד כמה הנכם מזדהים עם הדמויות בסרט. מרמת הזדהות נמוכה - "אינני מזדהה כלל" ועד לרמת הזדהות גבוהה - "אני מזדהה עם הדמות ומרגיש את מה שהיא חווה"''',  
                           pos=(0,350),languageStyle= "RTL") 
    
    line1 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,200),end=(300,200),lineWidth=5,interpolate=True)
    line2 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,0),end=(300,0),lineWidth=5,interpolate=True)
    line3 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,-200),end=(300,-200),lineWidth=5,interpolate=True)
    line4 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,-400),end=(300,-400),lineWidth=5,interpolate=True)
    circle1 = visual.Circle(win=win,radius=20,pos=(-300,200),fillColor="red",edges=128)
    circle2 = visual.Circle(win=win,radius=20,pos=(-150,0),fillColor="red",edges=128)
    circle3 = visual.Circle(win=win,radius=20,pos=(150,-200),fillColor="red",edges=128)
    circle4 = visual.Circle(win=win,radius=20,pos=(300,-400),fillColor="red",edges=128)
    guide1 = visual.TextStim(win=win,text="אינני מזדהה כלל",pos=(-450,200),languageStyle= "RTL")
    guide2 = visual.TextStim(win=win,text="אני מזדהה מעט עם הדמות",pos=(-150,50),languageStyle= "RTL")
    guide3 = visual.TextStim(win=win,text="אני מזדהה עם הדמות במידה רבה",pos=(150,-250),languageStyle= "RTL")
    guide4 = visual.TextStim(win=win,text="אני מזדהה לגמרי עם הדמות\n ומרגיש את מה שהיא חווה",pos=(450,-400),languageStyle= "RTL")

    text.draw()
    text2.draw()
    line1.draw()
    line2.draw()
    line3.draw()
    line4.draw()
    circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()
    guide1.draw()
    guide2.draw()
    guide3.draw()
    guide4.draw()
    win.flip()
    time.sleep(10)
    win.close()
 


def social_sync_touch_tutorial():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(-1,-1,-1))
 
    text = visual.TextStim(win=win,text="סינכרון מגע",  pos=(0,150),languageStyle= "RTL")
    text2 = visual.TextStim(win=win,
            text='''אתם עומדים לצפות בקטע וידאו קצר המתאר אינטראקציה חברתית. אנא דרגו בעזרת הסליידר את רמת סנכרון המגע בין הדמויות על סקאלה מ"ללא סנכרון מגע כלל" ועד ל"סנכרון מגע מקסימלי".''',
            pos=(0,-100),
            languageStyle= "RTL")

    text.draw()
    text2.draw()
    win.flip()
    time.sleep(5)

    #### slide 2
    text = visual.TextStim(win=win,text="סנכרון מגע מקסימלי מוגדר כאשר דמות א' ודמות ב' נוגעות זו בזו בו-זמנית. המגע הפיזי יכול להיות בקונטקסט חיובי (חיבוק) או  בקונטקסט שלילי (האבקות).",  
                           pos=(0,250),languageStyle= "RTL")  

    img1 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[0]),pos=(-800,0))
    img2 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[1]),pos=(-400,0))
    img3 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[2]),pos=(0,0))
    img4 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[3]),pos=(400,0))
    img5 = visual.ImageStim(win=win,image=os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[4]),pos=(800,0))
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
    
    time.sleep(1)

    #### slide 3
    text = visual.TextStim(win=win,text="רמה גבוהה של סנכרון מגע היא כאשר דמות א' נוגעת בדמות ב', אך דמות ב' אינה מנסה לגעת בדמות א'.",  
                           pos=(0,250),languageStyle= "RTL") 
    img1.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[5])
    img2.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[6])
    img3.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[7])
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

    time.sleep(1)

    #### slide 4

    text = visual.TextStim(win=win,text="כאשר שתי הדמויות רוכנות זו אל זו אך אין מגע ישיר, רמת סנכרון המגע נמוכה",  
                           pos=(0,250),languageStyle= "RTL") 
    img1.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[8])
    img2.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[9])
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

    time.sleep(1)

    ### slide 5

    text = visual.TextStim(win=win,text="כאשר על המסך מופיעה דמות אחת בלבד או כאשר הדמויות אינן נוגעות זו בזו, אין כלל סינכרון מגע.",  
                           pos=(0,250),languageStyle= "RTL") 
    img1.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[10])
    img2.image= os.path.join(os.getcwd(), "assets","pics", TOUCH_IMG[11])
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

    time.sleep(1)
    ####identification slide

    text = visual.TextStim(win=win,text="הזדהות",  
                           pos=(0,450),languageStyle= "RTL")
    text2 = visual.TextStim(win=win,text='''אתם עומדים לצפות בקטע וידאו קצר המתאר אינטראקציה חברתית. אנא דרגו בעזרת הסליידר עד כמה הנכם מזדהים עם הדמויות בסרט. מרמת הזדהות נמוכה - "אינני מזדהה כלל" ועד לרמת הזדהות גבוהה - "אני מזדהה עם הדמות ומרגיש את מה שהיא חווה"''',  
                           pos=(0,350),languageStyle= "RTL") 
    
    line1 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,200),end=(300,200),lineWidth=5,interpolate=True)
    line2 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,0),end=(300,0),lineWidth=5,interpolate=True)
    line3 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,-200),end=(300,-200),lineWidth=5,interpolate=True)
    line4 = visual.Line(win=win,lineColor=[1, 1, 1],start=(-300,-400),end=(300,-400),lineWidth=5,interpolate=True)
    circle1 = visual.Circle(win=win,radius=20,pos=(-300,200),fillColor="red",edges=128)
    circle2 = visual.Circle(win=win,radius=20,pos=(-150,0),fillColor="red",edges=128)
    circle3 = visual.Circle(win=win,radius=20,pos=(150,-200),fillColor="red",edges=128)
    circle4 = visual.Circle(win=win,radius=20,pos=(300,-400),fillColor="red",edges=128)
    guide1 = visual.TextStim(win=win,text="אינני מזדהה כלל",pos=(-450,200),languageStyle= "RTL")
    guide2 = visual.TextStim(win=win,text="אני מזדהה מעט עם הדמות",pos=(-150,50),languageStyle= "RTL")
    guide3 = visual.TextStim(win=win,text="אני מזדהה עם הדמות במידה רבה",pos=(150,-250),languageStyle= "RTL")
    guide4 = visual.TextStim(win=win,text="אני מזדהה לגמרי עם הדמות\n ומרגיש את מה שהיא חווה",pos=(450,-400),languageStyle= "RTL")

    text.draw()
    text2.draw()
    line1.draw()
    line2.draw()
    line3.draw()
    line4.draw()
    circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()
    guide1.draw()
    guide2.draw()
    guide3.draw()
    guide4.draw()
    win.flip()
    time.sleep(10)
    win.close()
 

def grid_visual():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(1,1,1))

def grid_touch():
    
    win = visual.Window(size=[1024, 1080],units="pix",fullscr=True,color=(1,1,1))
