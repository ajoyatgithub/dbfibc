#$Id: scrolltext.py,v 1.3 2004/03/17 04:29:31 mandava Exp $
# this is a program to create a scrolledtextbox, we can import files in to
# the text box. 

#'importfile' reads the contents of the filename into the text component.
#we also have 'exportfile' option which writes the contents of the text
#component to the file specified .



title = 'Pmw.ScrolledText'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']



import string
import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):

	# Create the ScrolledText .
        fixedFont = Pmw.logicalfont('Fixed')
       	self.st = Pmw.ScrolledText(parent,
		labelpos = 'n',
		label_text='ScrolledText',


		usehullsize = 1,
		hull_width = 400,
		hull_height = 300,
		text_wrap='none',
		text_font = fixedFont,

		text_padx = 4,
		text_pady = 4,
	)
	self.st.importfile('python.txt');
	self.st.pack(padx = 5, pady = 5, fill = 'both', expand = 1)

        # Prevent users' modifying text and headers
	self.st.configure(
            text_state = 'disabled',

        )

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


