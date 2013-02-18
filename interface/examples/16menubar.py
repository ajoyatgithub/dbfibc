#$Id: menubar.py,v 1.3 2004/03/17 04:29:31 mandava Exp $
#program to create a simple menu bar with file and edit options.
#we have open,close,save,print options in the fie menu and copy, cut ,
#paste options in the edit menu.
  
#we add buttons to the menubar using addmenu method and items to these
#using addmenuitem method.

#addmenu method:this method adds a menu button and its associated menu to
#the menubar.keyword arguments present will be passed to the constructor
#when creating the menu button.

#addmenuitem:this method adds a menuitem to the menu .the kind of menu item
#is given by the type. in this case we are creating menuitems of type
#command.
title = 'Pmw.simpleMenuBar'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):

	# Create and pack the MenuBar.
	menuBar = Pmw.MenuBar(parent,
		hull_relief = 'raised',
		hull_borderwidth = 1)

	menuBar.pack(fill = 'x')
	self.menuBar = menuBar

	# Add some buttons to the MenuBar.
    # here menu buttons file , edit and help are added to the menubar. menu
    # items open,close,save,print are added to file menu and menu items
	#cut,copy,paste are added to the edit menu.
 
	menuBar.addmenu('File','none')
	menuBar.addmenuitem('File','command',
		command = PrintOne('Action: open'),
		label = 'open')
	menuBar.addmenuitem('File', 'command',

		command = PrintOne('Action: close'),
		label = 'Close')
	menuBar.addmenuitem('File','command',
        command = PrintOne('Action:save'),
        label = 'save')
	menuBar.addmenuitem('File','command',
        command = PrintOne('Action:print'),
        label = 'print')

	menuBar.addmenuitem('File', 'separator')
	menuBar.addmenuitem('File', 'command',
		command = PrintOne('Action: exit'),
		label = 'Exit')

	menuBar.addmenu('Edit','none')
	menuBar.addmenuitem('Edit', 'command', 
		command = PrintOne('Action: cut'),
		label = 'cut')
	menuBar.addmenuitem('Edit', 'command',
        command = PrintOne('Action: copy'),
        label = 'copy')
	menuBar.addmenuitem('Edit', 'command',
        command = PrintOne('Action: paste'),
        label = 'paste')

	menuBar.addmenu('Help','none', side = 'right')
	menuBar.addmenuitem('Help', 'command',
		command = PrintOne('Action: about'),
		label = 'About...')

	# Create and pack the main part of the window.
	self.mainPart = Tkinter.Label(parent,
		text = 'This is the\nmain part of\nthe window',
		background = 'black',
		foreground = 'white',
		padx = 60,
		pady = 60)
	self.mainPart.pack(fill='both',expand=1)
class PrintOne:
	def __init__(self,text):
		self.text=text
   
	def __call__(self):
		print self.text

######################################################################

# Create demo in root window for testing.
if __name__ == '__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)

    exitButton = Tkinter.Button(root, text = 'Exit', command =
root.destroy)
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop()


