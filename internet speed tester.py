from tkinter import*
import speedtest
root = Tk()
root.title('Internet Speed tester')
root.geometry('500x600')
root.config(bg = 'sky blue')

def Speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str( round(sp.download()/(10**6),3))+'Mbps'
    upload = str( round(sp.upload()/(10**6),3))+'Mbps'
    label_down.config(text= down)
    label_upload.config(text= upload)

label = Label(root,text= '------Internet Speed Tester------',font= ('time new roman',20,'bold'),bg = 'sky blue')
label.place(x=60 , y=40,height = 50 ,width = 380)


label1 = Label(root,text= 'Download Speed',font= ('time new roman',20,'bold'))
label1.place(x=60 , y=120,height = 50 ,width = 380)


label_down = Label(root,text= '00',font= ('time new roman',20,'bold'))
label_down.place(x=60 , y=210,height = 50 ,width = 380)


label3 = Label(root,text= 'Upload Speed',font= ('time new roman',20,'bold'))
label3.place(x=60 , y=300,height = 50 ,width = 380)


label_upload = Label(root,text= '00',font= ('time new roman',20,'bold'))
label_upload.place(x=60 , y=390,height = 50 ,width = 380)


botton = Button(root,text= 'Check Speed',font = ('time new roman',20,'bold') , relief=RAISED,bg = 'red',command = Speedcheck)
botton.place(x=60 , y=470,height = 50 ,width = 380)


root.mainloop()
