from Tkinter import *
from subprocess import call
import tkMessageBox
import smtplib
import re
import argparse
import string
import md5
import auth
import sys
import os
from ctypes import *
import sent

def nextWindow():
    win = Toplevel()
    win.title("Authentication")
    win.geometry("500x500+200+200")
    frmWin = Frame(win)
    frmWin.grid()
    def main():
        wind    = Toplevel()
        wind.geometry("500x500+200+200")
        frmWind = Frame(wind)
        frmWind.grid()
        label0  = Label(frmWind,text= "WELCOME",relief=RAISED,width=50,bg="white")
        label0.grid()
        auth_type='1'
        username = t1.get()
        password = t2.get()
        hashp    = md5.new(password).digest()
        #auth_result = auth.auth(username, password,auth_type)
        auth_result="S"
        if  auth_result == "S":
            label111 = Label(frmWind,text="successfull",relief=RAISED,width=50,bg="white")
            label111.grid(padx=25,pady=25)
            ltr="./node 2433 certs/1.pem certs/1-key.pem /home/ajoy/project/dbfibc/files 0 0 0"
            os.chdir("dkg/")
            #call(ltr,shell=True)
            dkg_run  = Label(frmWind,text="DKG Running",relief=RAISED,width=50,bg="white")
            dkg_run.grid(padx=25,pady=25)
            ibc_run  = Label(frmWind,text="IBC Running",relief=RAISED,width=50,bg="white")
            ibc_run.grid(padx=25,pady=25)
            button   = Button(frmWind,text="SEND",bg="green",command=sent.say,width=50)
            button.grid(padx=25,pady=25)

            # os.chdir("/home/shanto/Desktop/interface/dbfibc/files")
            #ibc = cdll.LoadLibrary("./libibc.so.1.0.1")
            # ibcstring="ibc.start(username,1.pem)"
            # call(ibcstring,shell=True)
        else:
            label112 = Label(frmWind,text="failed")
            label112.grid()

        label1  = Label(frmWin,text="Email address:",width=50, fg="blue",relief=RAISED)
        label1.grid(padx=25,pady=25)
        t1      = Entry(frmWin)
        t1.grid()
        label2  = Label(frmWin,text="Password:",width=50,fg="blue",relief=RAISED)
        label2.grid(padx=25,pady=25)
        t2      = Entry(frmWin,show='*')
        t2.grid()
        tk_rgb = "#%02x%02x%02x" % (128, 250, 200)
        button  = Button(frmWin,text="Authenticate",bg=tk_rgb,width=17,command=main)
        button.grid(padx=25,pady=25)

def nextWindow1():
    win1 = Toplevel()
    win1.geometry("200x200+200+200")
    frmWin1 = Frame(win1)
    frmWin1.grid()
    label11 = Label(frmWin1,text="LDAP address:",width=50, fg="cyan")
    label11.grid(padx=25,pady=25)
    t11     = Entry(frmWin1)
    t11.grid()
    label21 = Label(frmWin1,text="Password:",width=50, fg="cyan")
    label21.grid(padx=25,pady=25)
    t21     = Entry(frmWin1,show='*')
    t21.grid()
    button11= Button(frmWin1,text="ok",bg="blue")
    button11.grid(padx=25,pady=25)

root = Tk()
root.title("Authentication Mode")
root.geometry("500x500+200+200")
app  = Frame(root)
app.grid()
label = Label(app,text="Authenticate", fg="blue",
              relief=RAISED,padx=15,pady=20,width=50)
label.grid(padx=25,pady=25)
relStatus = StringVar()
relStatus.set(None)
radiobut1 = Radiobutton(app, text="Email Authentication",
                        value="Email Authentication", variable = relStatus,
                        command=nextWindow,  fg="blue",
                        relief=RAISED).grid(padx=25,pady=25)
radiobut1 = Radiobutton(app, text="LDAP Authentication",
                        value="LDAP Authentication",  variable = relStatus,
                        command=nextWindow1, fg="blue",
                        relief=RAISED).grid(padx=25,pady=25)
root.mainloop()
