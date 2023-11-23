import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
from tkinter import*

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        label2.config(text = 'Listening...')
        audio = recognizer.listen(source)
        
        try :
            label3.config(text = 'Recognizing...')
            data = recognizer.recognize_google(audio)
            label4.config(text = data)
        except  sr.UnknownValueError:
            c = 'Not Understand'
            label4.config(text =c)


def speech_to_text(a):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(a)
    engine.runAndWait()
    
     

root = Tk()
root.title('JARVIS')
root.config(bg= 'skyblue')
root.geometry('500x650')
label =Label(root,text= '***Welcome in Voice Recognition***',font= ('times new roman',18,'bold'))
label.place(x=40,y=20,height = 40,width = 420)

label1=Button(root,text= 'Start',font= ('times new roman',25,'bold'),bg = 'red',command = sptext)
label1.place(x=180,y=80,height = 40,width = 100)

label2 =Label(root,text= '---------',font= ('times new roman',25,'bold'))
label2.place(x=40,y=140,height = 40,width = 420)

label3 =Label(root,text= '---------',font= ('times new roman',25,'bold'))
label3.place(x=40,y=200,height = 40,width = 420)

label4 =Label(root,text= '---------',font= ('times new roman',14))
label4.place(x=40,y=260,height = 120,width = 420)


speech_to_text('hello guys')
