from Tkinter import *
import Tkinter as tk
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createsMenuButton()
        self.createsOptionsButton()
        self.createsHelpButton()
        self.createsUsernameWidget()
        self.createsUsernameEntryButton()
        self.createsLoginButton()
        
    #### creates title bar     
    def createsMenuButton(self):
        self.mb = Menubutton (self, text="FILE",
                              relief=FLAT,font=("Arial", 8), )
        self.mb.grid(row=0, column=0)
        self.mb.menu = Menu ( self.mb, tearoff=0 )
        self.mb['menu'] = self.mb.menu
        self.exitVar =IntVar()
        self.mb.menu.add_command (label="QUIT", 
                                       command=self.quit )
        
        
    def createsOptionsButton(self):
        self.mb = Menubutton (self, text="OPTIONS",
                              relief=FLAT,font=("Arial", 8))
        self.mb.grid(row=0, column=1)
        self.mb.menu = Menu ( self.mb, tearoff=0 )
        self.mb['menu'] = self.mb.menu
        self.clearVar = IntVar()
        self.mb.menu.add_checkbutton ( label="Font sizes",
                                       variable=self.clearVar )
    def createsHelpButton(self):
        self.mb = Menubutton (self, text="HELP",
                              relief=FLAT,font=("Arial", 8))
        self.mb.grid(row=0, column=2)
        self.mb.menu = Menu ( self.mb, tearoff=0 )
        self.mb['menu'] = self.mb.menu
        self.helpVar = IntVar()
        self.mb.menu.add_command ( label="help",
                                       command = self.NewWindow )
    def NewWindow(self):
        newWindow = Toplevel (master=None).minsize ( width=30,height=50)
        
        
    
        
    def createsUsernameWidget(self):
        self.username = Label (self, text="username:",
                   relief=FLAT,font=("Arial", 8))
        
        self.username.grid(row=1, column=1)
        
## This function creates the username libary
    def createsUsernameEntryButton(self):
        self.mb = Menubutton (self, 
                              relief=RIDGE,font=("Arial", 8))
        self.mb.grid(row=1, column=2)
        self.mb.menu = Menu ( self.mb, tearoff=0 )
        self.mb['menu'] = self.mb.menu
        self.helpVar = IntVar()
        self.helpVar2 = IntVar()
        self.helpVar3 = IntVar()
        self.helpVar4= IntVar()
        self.helpVar5 = IntVar()
        self.helpVar6 = IntVar()
        self.helpVar7 = IntVar()
        self.helpVar8 = IntVar()
##These are the names        
        self.mb.menu.add_checkbutton ( label="Adam Wilson",
                                       variable=self.helpVar )
        self.mb.menu.add_checkbutton ( label="Rhys Cee",
                                       variable=self.helpVar2 )
        self.mb.menu.add_checkbutton ( label="Steven Bee",
                                       variable=self.helpVar3 )
        self.mb.menu.add_checkbutton ( label="Adam eeS",
                                       variable=self.helpVar4 )
        self.mb.menu.add_checkbutton ( label="Aaron eeS",
                                       variable=self.helpVar5 )
        self.mb.menu.add_checkbutton ( label="Tom Arm",
                                       variable=self.helpVar6 )
        self.mb.menu.add_checkbutton ( label="Jamie Beee",
                                       variable=self.helpVar7 )
        self.mb.menu.add_checkbutton ( label="John Wee",
                                       variable=self.helpVar8 )
        
    def createsLoginButton (self):
        self.Button = Button (self, text="Login", command = self.loginPage,
                              relief=RAISED,font=("Arial", 8))
        self.Button.grid(row=2, column=1)
##HereHere
##HereHere
##Here
    def loginPage (self):
        logedInPage = Toplevel (master=None).minsize ( width=30,height=50)###I want to write text in the window created here
        w = Label (self, text("hi "))
        
                              
        
    
        
app = Application()
app.master.title("Wilson Messaging") 
app.mainloop()
