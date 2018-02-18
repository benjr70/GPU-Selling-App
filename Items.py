from Tkinter import *
#********************************* keep line 2-7 the smae for every frame
class Demo(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self)
        self.pack()
#***************************************** put code below this like so
        item  = Label(self, text = 'item 1!!!!!')
        item.pack(expand = YES, fill = BOTH, side = TOP)
        item.config(relief = SUNKEN, width = 40, height = 7, bg = 'beige')

        item  = Label(self, text = 'item 2!!!!!')
        item.pack(expand = YES, fill = BOTH, side = TOP)
        item.config(relief = SUNKEN, width = 40, height = 7, bg = 'beige')

        item  = Label(self, text = 'item 3!!!!!')
        item.pack(expand = YES, fill = BOTH, side = TOP)
        item.config(relief = SUNKEN, width = 40, height = 7, bg = 'beige')       

#Demo().mainloop() dont enter mainloop here that will happen when the frames are attached
