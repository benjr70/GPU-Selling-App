from Tkinter import *

demoModules = [ 'Banner','CheckBoxes','Items', 'cart']#add new frame file name here
parts = []
def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)
        part = module.Demo(root)
        part.config(bd=2,relief = GROOVE)
        part.pack(side = LEFT, fill = BOTH)
        parts.append(part)
def dumpState():
    for part in parts:
            print part.__module__+':',
            if hasattr(part,'report'):
                part.report()
            else:
                print 'None'
root = Tk()
addComponents(root)
mainloop()
