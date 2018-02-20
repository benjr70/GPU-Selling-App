from Tkinter import *
from item_class import items


class Demo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.pack()

        cart = Label(self, text='Cart')
        cart.pack(fill=BOTH, side=TOP)
        cart.config(relief=SUNKEN, width=15, height=1, bg='green')
        labelFont = ('verdana', 20, 'bold')
        cart.config(font=labelFont)

        # item  = Label(self, text = 'item 1!!!!!')
        # item.pack(fill = X, side = TOP,anchor = N)
        # item.config(relief = SUNKEN, width = 40, height = 5, bg = 'beige')

        checkout = Button(self, text='Checkout')
        checkout.config(background='green', font=labelFont)
        checkout.pack(side=TOP, fill=X, anchor=N)

# Demo().mainloop()
