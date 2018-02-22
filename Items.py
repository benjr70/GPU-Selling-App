from Tkinter import *
from item_class import items
from PIL import ImageTk, Image
import tkSimpleDialog
from cart_item_class import cartItem

# ********************************* keep line 2-7 the same for every frame
subtotal = 0
subtot = Label()
itemL = Label()
remove = Button()
Verdana14 = ('verdana', 14, 'bold')
Verdana10 = ('verdana', 10, 'bold')



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
            global subtotal
            global subtot
            global itemL
            global remove
            global cartItem
            flag = True
            for cartItem in cartItem.cartList:
                tempitem = cartItem.get_itemclass()
                print tempitem.get_name()
                if(item.get_name() == tempitem.get_name()):
                    flag = False
                    print 'in flag = false item'
                    itemL = cartItem.get_label()
                    remove = cartItem.get_button()
                    itemL.pack_forget()
                    remove.pack_forget()
                    newQuantity = int(quantity) + int(cartItem.get_quantity())
                    itemL = Label(self, text=item.get_name() + "   ( Quantity: " + str(newQuantity) + " )")
                    itemL.pack(fill=X, side=TOP, anchor=N)
                    itemL.config(relief=SUNKEN, width=40, height=1, bg='beige')
                    remove = Button(self, text= "Remove " + item.get_name(), command = lambda j=r:removeCart(item.get_name()))
                    remove.pack(side=TOP, anchor=E)
                    cartItem.set_quantity(newQuantity)
                    cartItem.set_label(itemL)
                    cartItem.set_button(remove)
                    break
                else:
                    flag = True
                    print 'in else true'
                    
            if(flag == True):
                print 'in if(flag == true)'
                itemL = Label(self, text=item.get_name() + "   ( Quantity: " + quantity + " )")
                itemL.pack(fill=X, side=TOP, anchor=N)
                itemL.config(relief=SUNKEN, width=40, height=1, bg='beige')
            
                remove = Button(self, text= "Remove " + item.get_name(), command = lambda j=r:removeCart(item.get_name()))
                remove.pack(side=TOP, anchor=E)
            
                cartItem(itemL, remove, item, quantity)
            
            subtot.pack_forget()
            subtotal = subtotal + item.get_price() * int(quantity)
            
            subtot = Label(self, text="subtotal: $" + str(subtotal))
            subtot.config(relief=SUNKEN, width=40, height=1, bg='beige')
            subtot.pack(side=BOTTOM, fill=X, anchor=N)
        def displayCheckOut():
            myDialog = CheckOutDialog()
            myDialog.wait_window(myDialog.top)
            
        def removeCart(itemname):
            print 'int removeCart'
            global itemL
            global remove
            global cartItem
            global subtotal
            global subtot
            for cartItem in cartItem.cartList:
                tempitem = cartItem.get_itemclass()
                if(itemname == tempitem.get_name()):
                    itemL = cartItem.get_label()
                    remove = cartItem.get_button()
                    subtotal = subtotal - tempitem.get_price() * float(cartItem.get_quantity())
                    cartItem.set_quantity(0)
                    subtot.pack_forget()                    
                    subtot = Label(self, text="subtotal: $" + str(subtotal))
                    subtot.config(relief=SUNKEN, width=40, height=1, bg='beige')
                    subtot.pack(side=BOTTOM, fill=X, anchor=N)
                    
                    
            itemL.pack_forget()
            remove.pack_forget()

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
                   command=lambda j=r: addToCart(itemName[j], options[j].get())).grid(column=3, row=r, sticky=S, pady=3,
                                                                                      padx=10)

            r = r + 1

        cart = Label(self, text='Cart')
        cart.pack(fill=BOTH, side=TOP)
        cart.config(relief=SUNKEN, width=15, height=1, bg='green')
        labelFont = ('verdana', 20, 'bold')
        cart.config(font=labelFont)

        checkout = Button(self, text='Checkout', command=displayCheckOut)
        checkout.config(background='green', font=labelFont)
        checkout.pack(side=BOTTOM, fill=X, anchor=N)




class CheckOutDialog(Tk):
    def __init__(self):
        Tk.__init__(self)
        shippingFields = 'Full name', 'Address', 'Zip', 'City', 'State', 'Phone number'
        paymentFields = 'Card number', 'EXP', 'Security code', 'Name on card'
        delivery = 5.99
        tax = subtotal * 0.075
        total = subtotal + tax + delivery
        entries = []

        header = Frame(self)
        header.pack(side=TOP, fill=X)
        headerLabel = Label(header, pady=10, text="1. Shipping Address")
        headerLabel.pack(side=TOP, anchor='n')
        headerLabel.config(font=Verdana14)
        for field in shippingFields:
            row = Frame(self)
            row.pack(side=TOP, fill=X)
            label = Label(row, width=15, pady=5, text=field, justify=LEFT)
            label.pack(side=LEFT)
            ent = Entry(row)
            ent.pack(side=LEFT, expand=NO)
            ent.config(width=30)
            entries.append(ent)

        header = Frame(self)
        header.pack(side=TOP, fill=X)
        headerLabel = Label(header, pady=10, text="2. Payment")
        headerLabel.pack(side=TOP, anchor='n')
        headerLabel.config(font=Verdana14)
        for field in paymentFields:
            row = Frame(self)
            row.pack(side=TOP, fill=X)
            label = Label(row, width=15, pady=5, text=field, justify=LEFT)
            label.pack(side=LEFT)
            ent = Entry(row)
            ent.pack(side=LEFT, expand=NO)
            ent.config(width=30)
            entries.append(ent)
        mainButton = Button(self, text='Continue', command=self.on_click)
        mainButton.pack()

        top = self.top = Toplevel(self)
        header = Frame(top)
        header.pack(side=TOP, fill=X)
        headerLabel = Label(header, pady=10, text="3. Review")
        headerLabel.pack(side=TOP, anchor='n')
        headerLabel.config(font=Verdana14)

        subtotalLabel = Label(top, text="subtotal: $" + str("%.2f" % subtotal))
        subtotalLabel.pack(side=TOP, anchor='ne')
        subtotalLabel.config(font=Verdana10)
        deliveryLabel = Label(top, text="delivery: $" + str("%.2f" % delivery))
        deliveryLabel.pack(side=TOP, anchor='ne')
        deliveryLabel.config(font=Verdana10)
        taxLabel = Label(top, text="tax: $" + str("%.2f" % tax))
        taxLabel.pack(side=TOP, anchor='ne')
        taxLabel.config(font=Verdana10)
        totalLabel = Label(top, text="total: $" + str("%.2f" % total))
        totalLabel.pack(side=TOP, anchor='ne')
        totalLabel.config(font=Verdana10)
        mainButton = Button(top, text='Place Order', command=self.last_click)
        mainButton.pack()

        top.withdraw()

        reviewTop = self.reviewTop = Toplevel(self)



        reviewTop.withdraw()

    def send(self):
        self.top.withdraw()

    def on_click(self):
        self.top.deiconify()

    def destroyRest(self):
        self.top.destroy()

    def last_click(self):
        self.top.destroy()




# Demo().mainloop() #don't enter mainloop here that will happen when the frames are attached
