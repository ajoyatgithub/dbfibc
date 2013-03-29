import re
from Tkinter import *
def say():
    top=Toplevel()
    frame=Frame(top)
    frame.pack()
    top.geometry("500x500+200+200")
    label=Label(frame,text="To",fg="blue",relief=RAISED,width=50,bg="white")
    label.pack(padx=10,pady=10)
    listbox = Listbox(frame,relief=RAISED,width=50)
    
    
    
    name=open("../contacts","r")
    while 1:
        line = name.readline()
        if not line:
            break
        line =line.rstrip("\n")
        pr = re.search("(ID:[\d]+:name:)([\S]+)",line)
        listbox.insert(END, pr.group(2))
    
    listbox.pack(padx=10,pady=10)
    text = Text(frame, height=10, width=57)
    text.pack(padx=10,pady=10)
    
    send=Button(frame,text="SEND",bg="green",relief=RAISED,width=47)
    send.pack(padx=10,pady=10)
    
    Quit=Button(frame,text="QUIT",bg="green",command=top.destroy,relief=RAISED,width=47)
    Quit.pack(padx=10,pady=10)    
