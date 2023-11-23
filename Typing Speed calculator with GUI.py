from time import *
import random as r
from tkinter import *

def Speed(user_input,time1 ,time2 ):
    delay = time2 - time1
    e = round(delay,2)
    speed1 = len(sor_txt)/e
    typing_speed = round(speed1)
    return typing_speed
def mistake(user_input, paragraph):
    error=0
    for i in range(len(paragraph)):
        try:
            if paragraph != user_input:
                error = error + 1
        except:
            error = error + 1
    return error

top = Tk()
top.geometry('500x700')
top.config(bg = 'brown')
top.title('Typing Speed Calculator by Rajeshwar Akhodiya')
label = Label(top,text='-----------Typing Speed Calculator-----------', font  = ('Arial',18,'bold'),bg='brown',fg= 'black')
label.place(x= 100,y = 40,height = 50,width = 300)
label.pack()

label_text = Label(top,text= 'This is your Pharagraph:',font = ('time new roman',16,'bold'),fg = 'black',bg='brown')
label_text.place(x= 100,y = 100,height = 20,width = 300)
label_text.pack()

a= ['''The electricity produced due to friction is known as frictional electricity &
the charge produced on the body will become static therefore it is called
static Electricity.''',
       '''In 1600 BC, a greek philosopher thales found a resinous (gum like) substance
in the source of Baltic Sea which is called Amber & the Greek name of amber
was electrical.''',
       '''When two material rubbed to each other then the frictional heat is so produced 
& this heat is absorbed by a atom of materials but the atom which has low work 
function, emits the electron & get + ve charge & the atom which has higher work 
function gains the 𝑒𝑠− & get − ve charge. Hence, in frictional electricity the opposite 
charge produced due to transfer of electron.''',
    '''In GUI programming, a top-level root windowing object contains all of the little
windowing objects that will be part of your complete GUI application. These can be
text labels, buttons, list boxes, etc. These individual little GUI components are known
as widgets.''',
    '''Widgets can be stand-alone or be containers. If a widget contains other widgets, it is
considered the parent of those widgets. Accordingly, if a widget is contained in another
widget, it’s considered a child of the parent, the parent being the next immediate enclosing
container widget.''',
    '''Usually, widgets have some associated behaviors, such as when a button is pressed,
or text is filled into a text field. These types of user behaviors are called events, and the
GUI’s response to such events are known as callbacks.''']
para= r.choice(a)

label2 =Label(top, text = para,font = (12))
label2.place(x= 10,y = 130,height = 150,width = 480)
label2.pack()

label_text1= Label(top,text= 'Type below:',font = ('time new roman',16,'bold'),fg = 'black',bg='brown')
label_text1.pack()

frame = Frame(top).pack(side='bottom')
time_delay1 = time()
sor_txt = Text(frame,font = ('times new roman',12))
sor_txt.place(x= 100,y = 360,height = 20,width = 300)
sor_txt.pack()
time_delay2 = time()

Button (top, text='Quit', command=top.quit).pack(side=LEFT)


Typing_speed = Label(top,text= Speed(sor_txt,time_delay1,time_delay2),font = ('time new roman',16,'bold'),fg = 'black',bg='brown')
top.mainloop()








