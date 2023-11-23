import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import wikipedia
import subprocess
import wolframalpha
import json
import random

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try :
            print('recognizing...')
            data = recognizer.recognize_google(audio)
            return data
        except  sr.UnknownValueError:
            print('Not Understand')

def speech_to_text(a):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',170)
    engine.say(a)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speech_to_text("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speech_to_text("Good Afternoon Sir !")  
  
    else:
        speech_to_text("Good Evening Sir !") 
  
    assname =("My name is Aman")
    speech_to_text("I am your Assistant")
    speech_to_text(assname)
def username():
    #speech_to_text("What should i call you sir")
    #uname = sptext()
    #speech_to_text("Welcome Mister")
    #speech_to_text(uname)
    speech_to_text("How can i Help you, Sir")


 

if __name__ == '__main__':
    wishMe()
    username()
while True:
        if sptext().lower()== 'hello' :
            speech_to_text("hello sir")
            data1 = sptext().lower()
            if 'what is your name' in data1:
                speech_to_text('My name is Aman')
            elif 'what is your good name' in data1:
                speech_to_text('My name is Aman')
            elif 'tumhara naam kya hai' in data1:
                speech_to_text('mera naam Aman hai')
            elif 'tum kya khate ho' in data1:
                speech_to_text('i cannot eat')
            elif 'What are you eating' in data1:
                speech_to_text('i am a robot i do not eat or drink')
            elif 'What is your age' in data1:
                speech_to_text('I am twenty five year old')
            elif 'Tumhari Umra kya hai' in data1:
                speech_to_text('मेरी उम्र पच्चीस साल है')
            elif "who made you" or " who created you" in data1:
                speech_to_text("I have been created by Rajeshwar.")
            elif 'Tumhen kisne banaya hai' in data1:
                speech_to_text('Mujhe Rajeshwar Ne Banaya hai')
            elif  'open wikipedia' in data1:
                speech_to_text('Searching Wikipedia...')
                data1 = data1.replace("wikipedia", "")
                results = wikipedia.summary(data1, 2)
                speech_to_text("According to Wikipedia")
                speech_to_text(results)
        else:
            speech_to_text('thanks')
                
        



 
