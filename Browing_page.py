#**********************************************************
#***** Student: Kyle Paxton and Ben Rolf              *****
#***** Class: Human Factors and User Interface        *****
#***** Instructor: Gamradt                            *****
#***** Assignment: 1                                  *****
#***** Due Date: 02-23-18                             *****
#**********************************************************
#***** Description: This program is the user interface*****
#*****  of the company "The GPU Place". It features a *****
#*****  browsing page, a cart to store items that the *****
#*****  user wants to purchase, and new windows for   *****
#*****  the user to input their shipping and payment  *****
#*****  information.                                  *****
#**********************************************************
from Tkinter import *
from PIL import ImageTk, Image

demoModules = ['Banner', 'Items']  # add new frame file name here
parts = []

#**********************************************************
#***** Function: center                               *****
#**********************************************************
#***** Description: This function centers the window  *****
#*****  to the screens details.                       *****
#**********************************************************
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

#**********************************************************
#***** Function: addComponents                        *****
#**********************************************************
#***** Description: adds in the modules into the      *****
#*****  window.                                       *****
#**********************************************************
def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)
        part = module.Demo(root)
        part.config(bd=2, relief=GROOVE)
        part.pack(side=LEFT, fill=BOTH)
        parts.append(part)


def dumpState():
    for part in parts:
        print part.__module__ + ':',
        if hasattr(part, 'report'):
            part.report()
        else:
            print 'None'



root = Tk()
addComponents(root)
root.title("Home Page")
root.geometry("1100x750")
center(root)
mainloop()
