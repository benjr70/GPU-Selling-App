#**********************************************************
#***** Student: Kyle Paxton and Ben Rolf              *****
#***** Class: Human Factors and User Interface        *****
#***** Instructor: Gamradt                            *****
#***** Assignment: 1                                  *****
#***** Due Date: 02-23-18                             *****
#**********************************************************
#***** Description: This page creates a top menu of   *****
#*****  the program. This top menu includes a file    *****
#*****  button that cascades into our help and about  *****
#*****  buttons, as well as contains a title for our  *****
#*****  company's page.                               *****
#**********************************************************

from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image

class Demo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        # **********************************************************
        # ***** Function: displayAbout                         *****
        # **********************************************************
        # ***** Description: This function will display the    *****
        # *****  course information                            *****
        # **********************************************************
        def displayAbout():
            showinfo('About', 'Student names: Kyle Paxton, Ben Rolf \n\n'+
                              'Course: SE 330\n\n' +
                              'Assignment: Assignment 1')

        # **********************************************************
        # ***** Function: displayHelp                          *****
        # **********************************************************
        # ***** Description: This function will display the    *****
        # *****  steps to use this software.                   *****
        # **********************************************************
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
        header = Label(headerFrame, text='THE GPU PLACE', font=("Helvetica", 24))
        header.pack(side=LEFT, padx=10)
