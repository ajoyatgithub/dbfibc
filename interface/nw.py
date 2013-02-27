from Tkinter import *

def nextWindow():
  win = Toplevel()
  win.geometry("500x500+200+200")
  frmWin = Frame(win)
  frmWin.grid()

  lbl = Label(frmWin,text="Which type of authentication do you want???")
  lbl.grid()

root=Tk()
root.title("my window")
root.geometry("500x500+200+200")

app=Frame(root)
app.grid()

label=Label(app,text="Which type of authentication do you want???")
label.grid()

radio1=Radiobutton(app,text="LDAP authentication", variable = opt)
radio1.grid()

radio2=Radiobutton(app,text="Gmail authentication", variable = opt)
radio2.grid()

button=Button(app,text="ok", command=nextWindow)
button.grid()

root.mainloop() 

