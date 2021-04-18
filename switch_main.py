from tkinter import *
import os
import sys

root= Tk()
canvas =Canvas(root,height=500,width=500,bg="#263D42")
canvas.pack()
frame= Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
def send_mail():
    os.system('python send_mail.py')
def insta_login():
    os.system('python insta_login.py')
def Whatsapp():
    os.system('python whatsapp.py')
def Twitter():
    os.system('python twitter.py')
def Search_quary():
    os.system('python google_search.py')
def youtube():
    os.system("python youtube.py")   
def wikisearch():
    os.system('python wikisearch.py')    
def close_window(root):
    window.destroy()    

root.geometry("500x500")
myLabel1= Label(frame,text="hello sir",bg="#263D42",foreground="white",font="white")
myLabel2= Label(frame,text="what you want to do select your choice",bg="#263D42",font="white",foreground="white")
myLabel3= Label(frame,text="1.Send Mail ")
myLabel4= Label(frame,text="2.Login to Instagram Account")
myLabel5= Label(frame,text="3.Login to Whatsapp")
myLabel6= Label(frame,text="4.Add tweet To Twitter")
myLabel7= Label(frame,text="5.Search Your Quiery On Google")
myLabel8= Label(frame,text="6.donload video from youtube")
myLabel9= Label(frame,text="7.know more on wikipedia")


myLabel1.place(x=160,y=10)
myLabel2.place(x=73,y=40)
myLabel3.place(x=10,y=80)
myLabel4.place(x=10,y=120)
myLabel5.place(x=10,y=160)
myLabel6.place(x=10,y=200)
myLabel7.place(x=10,y=240)
myLabel8.place(x=10,y=280)
myLabel9.place(x=10,y=320)

button1=Button(frame,text="Click to send  email",command=send_mail)
button1.place(x=220,y=80)
button2=Button(frame,text="Click to login instagram",command=insta_login)
button2.place(x=220,y=120)
button3=Button(frame,text="Click to open whatsapp",command=Whatsapp)
button3.place(x=220,y=160)
button4=Button(frame,text="Click to send tweets",command=Twitter)
button4.place(x=220,y=200)
button5=Button(frame,text="Click to search ",command=Search_quary)
button5.place(x=220,y=240)
button6=Button(frame,text="Click to download youtube video",command=youtube)
button6.place(x=220,y=280)
button7=Button(frame,text="Click to searchon wikipedia",command=wikisearch)
button7.place(x=220,y=320)



root.title('Main Menu')
button_exit=Button(root,text="EXIT",command=close_window)

root.mainloop()