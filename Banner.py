from Tkinter import *
from tkMessageBox import *

class Demo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        def displayAbout():
            showinfo('About', 'Student names: Kyle Paxton, Ben Rolf \n\n'+
                              'Course: SE 330\n\n' +
                              'Assignment: Assignment 1')

        def displayHelp():
            showinfo('Help',  '1. Browse through the selection of GPU\'s\n\n'+
                              '2. Add items to the cart \n\n' +
                              '3. Press the checkout button to proceed to next step.\n\n' +
                              '4. Enter your shipping and payment information press review\n\n'+
                              '5. Review all your information and press "place order"')


        menubar = Frame(parent)
        menubar.pack(side=TOP, fill=X)

        btnFile = Menubutton(menubar, text='File', underline=0)
        btnFile.pack(side=LEFT)
        file = Menu(btnFile)
        file.add_command(label='Help', command=displayHelp, underline=0)
        file.add_command(label='About', command=displayAbout, underline=0)
        btnFile.config(menu=file)

        headerFrame = Frame(parent)
        headerFrame.pack(side=TOP, fill=X)
        header = Label(headerFrame, text='GPU PLACE', font=("Helvetica", 24))
        header.pack(side=LEFT, padx=10)

        top = Frame(headerFrame)
        top.pack(side=TOP, fill=X, pady=10, padx=10)

        def callback():
            print e.get()

        b = Button(headerFrame, text="-->", width=5, command=callback)
        e = Entry(headerFrame, width=25)
        b.pack(in_=top, side=RIGHT)
        e.pack(in_=top, side=RIGHT)
