from tkinter import *
import datetime
root =  Tk()
root.geometry('760x380')
root.config(bg = 'black')
root.title('Digital Clock')

def date1():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    
    label1.config(text = hr)
    label2.config(text = mi)
    label3.config(text = sec)
    label4.config(text = am)

    label9.config(text = date)
    label10.config(text = month)
    label11.config(text = year)
    label12.config(text = day)
    label1.after(200,date1)
    
label1 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',50,'bold'))
label1.place(x=80,y=50,height = 80,width = 90)

label2 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',50,'bold'))
label2.place(x=250,y=50,height = 80,width = 90)

label3 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',50,'bold'))
label3.place(x=420,y=50,height = 80,width = 90)

label4 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',40,'bold'))
label4.place(x=590,y=50,height = 80,width = 90)

label5 = Label(root,text= 'Hour',bg = 'green',fg= 'white',font= ('times new roman',20,'bold'))
label5.place(x=80,y=150,height = 30,width = 90)

label6 = Label(root,text= 'Min',bg = 'green',fg= 'white',font= ('times new roman',20,'bold'))
label6.place(x=250,y=150,height = 30,width = 90)

label7 = Label(root,text= 'Sec',bg = 'green',fg= 'white',font= ('times new roman',20,'bold'))
label7.place(x=420,y=150,height = 30,width = 90)

label8 = Label(root,text= 'AM/PM',bg = 'green',fg= 'white',font= ('times new roman',15,'bold'))
label8.place(x=590,y=150,height = 30,width = 90)

label9 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',50,'bold'))
label9.place(x=80,y=200,height = 80,width = 90)

label10 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',50,'bold'))
label10.place(x=250,y=200,height = 80,width = 90)

label11 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',50,'bold'))
label11.place(x=420,y=200,height = 80,width = 90)

label12 = Label(root,text= '00',bg = 'green',fg= 'white',font= ('times new roman',30,'bold'))
label12.place(x=590,y=200,height = 80,width = 90)

label13 = Label(root,text= 'Date',bg = 'green',fg= 'white',font= ('times new roman',20,'bold'))
label13.place(x=80,y=300,height = 30,width = 90)

label14 = Label(root,text= 'Month',bg = 'green',fg= 'white',font= ('times new roman',20,'bold'))
label14.place(x=250,y=300,height = 30,width = 90)

label15 = Label(root,text= 'Year',bg = 'green',fg= 'white',font= ('times new roman',20,'bold'))
label15.place(x=420,y=300,height = 30,width = 90)

label16 = Label(root,text= 'Day',bg = 'green',fg= 'white',font= ('times new roman',20,'bold'))
label16.place(x=590,y=300,height = 30,width = 90)

date1()

root.mainloop()
