from Tkinter import *
from item_class import items
from PIL import ImageTk, Image


# ********************************* keep line 2-7 the same for every frame
subtotal = 0
subtot = Label()
class Demo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        # ***************************************** put code below this like so

        # create a canvas object and a vertical scrollbar for scrolling it
        vScrollBar = Scrollbar(self, orient=VERTICAL)
        vScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vScrollBar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vScrollBar.config(command=canvas.yview)

        # This creates a frame inside the canvas
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # updates the canvas, frame, and scrollbars
        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)
        canvas.pack()
        
        def addToCart(item, quantity):
            itemp = Label(self, text=item.get_name() + "   ( Quantity: " + quantity + " )")
            itemp.pack(fill=X, side=TOP, anchor=N)
            itemp.config(relief=SUNKEN, width=40, height=1, bg='beige')
            global subtotal
            global subtot
            subtot.pack_forget()
            subtotal = subtotal + item.get_price()*int(quantity)
            subtot = Label(self, text = "subtotal: $" + str(subtotal))
            subtot.config(relief = SUNKEN, width=40, height=1, bg='beige')
            subtot.pack(side=BOTTOM, fill=X, anchor=N)  

        # Create a list of items
        item1 = items("GTX 1080 ti", 549.00, 11, 'Nvidia', '1080TI.jpg')
        item2 = items("GTX 1070 ti", 449.00, 8, 'Nvidia', '1070.jpg')
        item3 = items("Radeon RX 480", 733.00, 8, 'AMD', 'Radeon480.jpg')
        item4 = items("AMD FirePro", 229.00, 4, 'AMD', 'FirePro.jpg')
        itemName = [item1, item2, item3, item4]
        r = 0
        options = []
        for selectedItem in enumerate(itemName):
            image = Image.open(selectedItem[1].get_pic())
            photo = ImageTk.PhotoImage(image)
            label = Label(interior, image=photo)
            label.image = photo  
            label.grid(column=0, row=r)

            itemname = Label(interior, text=selectedItem[1].get_name())
            itemname.grid(column=2, row=r, sticky=N)
            itemname.config(relief=SUNKEN, height=1, bg='beige')
            itemprice = Label(interior, text=selectedItem[1].get_price())
            itemprice.grid(column=3, row=r)
            itemprice.config(relief=SUNKEN, height=1, bg='beige')

            var = StringVar()
            var.set(1)
            options.append(var)
            drop = OptionMenu(interior, var, '1', '2', '3')
            drop.grid(column=2, row=r, sticky=S)
            drop.config(height=1, borderwidth=1)

            Button(interior, borderwidth=1, text='Add to cart',
                command=lambda j=r: addToCart(itemName[j], options[j].get())).grid(column=3, row=r, sticky=S, pady=3, padx=10)

            r = r + 1

        cart = Label(self, text='Cart')
        cart.pack(fill=BOTH, side=TOP)
        cart.config(relief=SUNKEN, width=15, height=1, bg='green')
        labelFont = ('verdana', 20, 'bold')
        cart.config(font=labelFont)

        checkout = Button(self, text='Checkout')
        checkout.config(background='green', font=labelFont)
        checkout.pack(side=BOTTOM, fill=X, anchor=N)


# Demo().mainloop() #don't enter mainloop here that will happen when the frames are attached
