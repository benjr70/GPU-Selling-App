from Tkinter import *


class Demo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()
        menubar = Frame(parent)
        menubar.pack(side=TOP, fill=X)
        header = Label(menubar, text='GPU PLACE', font=("Helvetica", 24))
        header.pack(side=LEFT, padx = 10)

        top = Frame(menubar)
        top.pack(side=TOP, fill=X, pady=10, padx=10)

        def callback():
            print e.get()

        b = Button(menubar, text="-->", width=5, command=callback)
        e = Entry(menubar, width=25)
        b.pack(in_=top, side=RIGHT)
        e.pack(in_=top, side=RIGHT)

