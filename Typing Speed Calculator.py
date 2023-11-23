from time import *
import random

def Delay_in_time(user_input,time1 ,time2 ):
    delay = time2 - time1
    e = round(delay,2)
    speed = len(input_str)/e
    typing_speed = round(speed)
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
        
    

print('------Typing Speed Calculator-----')
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
charge produced due to transfer of electron.''']
para= random.choice(a)
print(para)

time_delay1 = time()
input_str = input('Enter here: ')
time_delay2 = time()

print('Speed:' ,Delay_in_time(input_str,time_delay1,time_delay2),'w/sec')
print('Error:', mistake(input_str,para))
