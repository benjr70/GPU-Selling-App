#**********************************************************
#***** Student: Kyle Paxton and Ben Rolf              *****
#***** Class: Human Factors and User Interface        *****
#***** Instructor: Gamradt                            *****
#***** Assignment: 1                                  *****
#***** Due Date: 02-23-18                             *****
#**********************************************************
#***** Description: This is the page which will keep  *****
#*****  most of the data in the program maintained.   *****
#*****  This page will focus on maintaining the items *****
#*****  and cart functionality as well as take user   *****
#*****  and payment information on check out.         *****
#**********************************************************

from Tkinter import *
from item_class import items
from PIL import ImageTk, Image
from tkMessageBox import *
import tkSimpleDialog
from cart_item_class import cartItem

# ********************************* keep line 2-7 the same for every frame
subtotal = 0
subtot = Label()
count = 0
itemL = Label()
remove = Button()
Verdana14B = ('verdana', 14, 'bold')
Verdana10B = ('verdana', 10, 'bold')
Verdana10 = ('verdana', 10)
Verdana8 = ('verdana', 8)
labelFont = ('verdana', 20, 'bold')

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
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


class Demo(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        # ***************************************** put code below this like so

        vScrollBar = Scrollbar(self, orient=VERTICAL)
        vScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vScrollBar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vScrollBar.config(command=canvas.yview)

        # Creates Frame inside canvas
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # **********************************************************
        # ***** Function: configureInterior                    *****
        # **********************************************************
        # ***** Description: This function will update the     *****
        # *****  canvas, frame and the scrollbars depending    *****
        # *****  on the size of the window.                    *****
        # **********************************************************
        def configureInterior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', configureInterior)

        # **********************************************************
        # ***** Function: configureCanvas                      *****
        # **********************************************************
        # ***** Description: This function will update the     *****
        # *****  canvas, accordingly.                          *****
        # **********************************************************
        def configureCanvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', configureCanvas)
        canvas.pack()

        # **********************************************************
        # ***** Function: addToCart                            *****
        # **********************************************************
        # ***** Description: This function performs the steps  *****
        # *****  to adding an item into the cart. this includes*****
        # *****  maintaining item quantity and the subtotal.   *****
        # **********************************************************
        def addToCart(item, quantity):
            global subtotal
            global subtot
            global itemL
            global remove
            global cartItem
            flag = True
            for cartItem in cartItem.cartList:
                tempitem = cartItem.get_itemclass()
                if (item.get_name() == tempitem.get_name()):
                    flag = False
                    itemL = cartItem.get_label()
                    remove = cartItem.get_button()
                    itemL.pack_forget()
                    remove.pack_forget()
                    newQuantity = int(quantity) + int(cartItem.get_quantity())
                    itemL = Label(self, text=item.get_name() + "   ( Quantity: " + str(newQuantity) + " )")
                    itemL.pack(fill=X, side=TOP, anchor=N)
                    itemL.config(relief=SUNKEN, width=40, height=1, bg='beige')
                    remove = Button(self, text="Remove " + item.get_name(),
                                    command=lambda j=r: removeCart(item.get_name()))
                    remove.pack(side=TOP, anchor=E)
                    cartItem.set_quantity(newQuantity)
                    cartItem.set_label(itemL)
                    cartItem.set_button(remove)
                    break
                else:
                    flag = True

            if (flag == True):
                itemL = Label(self, text=item.get_name() + "   ( Quantity: " + quantity + " )")
                itemL.pack(fill=X, side=TOP, anchor=N)
                itemL.config(relief=SUNKEN, width=40, height=1, bg='beige')

                remove = Button(self, text="Remove " + item.get_name(), command=lambda j=r: removeCart(item.get_name()))
                remove.pack(side=TOP, anchor=E)

                cartItem(itemL, remove, item, quantity)

            subtot.pack_forget()
            subtotal = subtotal + item.get_price() * int(quantity)

            subtot = Label(self, text="subtotal: $" + str(subtotal))
            subtot.config(relief=SUNKEN, width=40, height=1, bg='beige')
            subtot.pack(side=BOTTOM, fill=X, anchor=N)

        # **********************************************************
        # ***** Function: displayCheckOut                      *****
        # **********************************************************
        # ***** Description: This function displays the initial*****
        # *****  checkout window. and halts users if the cart  *****
        # *****  is empty.                                     *****
        # **********************************************************
        def displayCheckOut():
            self.lower(belowThis=None)
            if (len(cartItem.cartList) > 0):
                myDialog = CheckOutDialog(cartItem.cartList)
                center(myDialog)
                myDialog.wait_window(myDialog.top)
            else:
                showinfo('Empty Cart!', 'Your cart is empty!!! \nFill your cart before you check out.')

        # **********************************************************
        # ***** Function: removeCart                           *****
        # **********************************************************
        # ***** Description: This function removes an item     *****
        # *****  that is currently in the cart.                *****
        # **********************************************************
        def removeCart(itemname):
            global itemL
            global remove
            global cartItem
            global subtotal
            global subtot
            for cartItem in cartItem.cartList:
                tempitem = cartItem.get_itemclass()
                if (itemname == tempitem.get_name()):
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
        item1 = items("GTX 1080 ti", 549.00, 11, 'Nvidia', '1080TI.jpg',
                      '11GB DDR5X VRAM, Memory Speed 11Gbps, boost clock 1582 MHz, Cuda Cores - 3584')
        item2 = items("GTX 1070 ti", 449.00, 8, 'Nvidia', '1070.jpg',
                      '8GB GDDR5(259-bit) on-board memory, PCI Express 3.0 x 16 interface, NVIDIA CUDA technology, VR-ready')
        item3 = items("Radeon RX 480", 733.00, 8, 'AMD', 'Radeon480.jpg',
                      'Dual-slot Width, 1x HDMI, 3x Display port, 256Bit, 8GB GDDR5, PCI 3.0x16, GPU Clock: 1266 MHz')
        item4 = items("AMD FirePro", 229.00, 4, 'AMD', 'FirePro.jpg',
                      '4GB SDRAM, Core Clock 950MHz, PCI Express 3.0 x 16')
        item5 = items("GTX 1060", 390.00, 3, "Nvidia", '1060.jpg',
                      '1809 MHz boost Clock with 3GB GDDR58, VR-ready, Dual HDMI 2.0 ports')
        item6 = items("Radeon RX Vega 64", 1199.99, 8, 'AMD', 'vega.jpg',
                      '8GB 2048-bit HBM2, 1x DVI-D 2x HDMI 2.0 2x DisplayPort, PCI EXpress 3.0')
        item7 = items("MSI Radeon RX 580", 766.49, 8, 'AMD', 'rx580.jpg',
                      '8GB 256-bit GDDR5 Bosst Clock 1393MHz PCI Express x16')
        item8 = items("Gigabyte Geforce GTX 1050 Ti", 239.99, 4, 'Nvidia', '1050ti.jpg',
                      '4GB 128-Bit GDDR5, Boost Clock 1468 MHz,1 x Dual-Link DVI-D 3 x HDMI 2.0b 1 x DisplayPort 1.4')
        item9 = items("PNY  GTX Titan X", 1599.99, 12, 'Nividia', 'TitanX.jpg',
                      '12GB 384-Bit GDDR5, Boost Clock 1075 MHz,3072 CUDA Cores, PCI Express 3.0 x16')
        itemName = [item1, item2, item3, item4, item5, item6, item7, item8, item9]
        r = 0
        options = []
        for selectedItem in enumerate(itemName):
            image = Image.open(selectedItem[1].get_pic())
            image = image.resize((159, 119), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label = Label(interior, image=photo)
            label.image = photo
            label.grid(column=0, row=r)

            itemname = Label(interior, text=selectedItem[1].get_name())
            itemname.grid(column=2, row=r, sticky=NW)
            itemname.config(font=labelFont)

            description = Label(interior, text=selectedItem[1].get_description())
            description.grid(column=2, row=r, sticky=W)
            description.config(height=1)

            itemprice = Label(interior, text="$" + str(selectedItem[1].get_price()))
            itemprice.grid(column=3, row=r)
            itemprice.config(height=1)

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
        cart.config(font=labelFont)

        checkout = Button(self, text='Checkout', command=displayCheckOut)
        checkout.config(background='green', font=labelFont)
        checkout.pack(side=BOTTOM, fill=X, anchor=N)


class CheckOutDialog(Tk):

    def __init__(self, cartList):
        Tk.__init__(self)
        shippingFields = 'Full name', 'Address', 'Zip', 'City', 'State', 'Phone number'
        paymentFields = 'Card number', 'EXP', 'Security code', 'Name on card'
        delivery = 5.99
        tax = subtotal * 0.075
        total = subtotal + tax + delivery

        shippingEntries = []
        paymentEntries = []

        self.title('User Information')

        header = Frame(self)
        header.pack(side=TOP, fill=X)
        headerLabel = Label(header, pady=10, text="1. Shipping Address")
        headerLabel.pack(side=TOP, anchor='n')
        headerLabel.config(font=Verdana14B)
        for field in shippingFields:
            row = Frame(self)
            row.pack(side=TOP, fill=X)
            label = Label(row, width=15, pady=5, text=field, justify=LEFT)
            label.pack(side=LEFT)
            ent = Entry(row)
            ent.pack(side=LEFT, expand=NO)
            ent.config(width=30)
            shippingEntries.append(ent)

        header = Frame(self)
        header.pack(side=TOP, fill=X)
        headerLabel = Label(header, pady=10, text="2. Payment")
        headerLabel.pack(side=TOP, anchor='n')
        headerLabel.config(font=Verdana14B)
        for field in paymentFields:
            row = Frame(self)
            row.pack(side=TOP, fill=X)
            label = Label(row, width=15, pady=5, text=field, justify=LEFT)
            label.pack(side=LEFT)
            ent = Entry(row)
            ent.pack(side=LEFT, expand=NO)
            ent.config(width=30)
            paymentEntries.append(ent)
        mainButton = Button(self, text='Review', command=lambda: self.onClick(shippingEntries, paymentEntries))
        mainButton.pack()

        top = self.top = Toplevel(self)

        top.title('Order Summary')

        header = Frame(top)
        header.pack(side=TOP, fill=X)

        headerLabel = Label(header, pady=10, text="3. Review")
        headerLabel.pack(side=TOP, anchor='n')
        headerLabel.config(font=Verdana14B)

        paymentHeader = Frame(top)
        paymentHeader.pack(side=TOP, fill=X)

        headerLabel = Label(paymentHeader, pady=10, text="Payment Summary")
        headerLabel.pack(side=TOP, anchor='w')
        headerLabel.config(font=Verdana10B, padx=35)

        paymentSecondHeader = Frame(top)
        paymentSecondHeader.pack(side=TOP, fill=X)

        headerLabel = Label(paymentSecondHeader, pady=10, text="Item")
        headerLabel.grid(column=0, row=1, padx=35)
        headerLabel.config(font=Verdana10)
        headerLabel = Label(paymentSecondHeader, pady=10, text="Quantity")
        headerLabel.grid(column=1, row=1, padx=35)
        headerLabel.config(font=Verdana10)
        headerLabel = Label(paymentSecondHeader, pady=10, text="Unit Price")
        headerLabel.grid(column=2, row=1, padx=25)
        headerLabel.config(font=Verdana10)

        usedNames = []
        for cartItem in cartList:
            body = Frame(top)
            body.pack(side=TOP, fill=X)
            body.config(bg="light grey")

            used = FALSE
            tempitem = cartItem.get_itemclass()

            if cartItem.get_quantity() > 0:
                for each in usedNames:
                    if tempitem.get_name() == each:
                        used = TRUE

            if cartItem.get_quantity() > 0 and used == FALSE:
                labeltext = tempitem.get_name()
                if len(tempitem.get_name()) > 10:
                    labeltext = '%s...' % tempitem.get_name()[:10]
                headerLabel = Label(body, pady=10, text=labeltext)
                headerLabel.grid(column=0, row=1, padx=(50 - len(labeltext)))
                headerLabel.config(font=Verdana8, bg="light grey")

                headerLabel = Label(body, pady=10, text=cartItem.get_quantity())
                headerLabel.grid(column=1, row=1, padx=35)
                headerLabel.grid(column=1, row=1, padx=(35 - len(str(cartItem.get_quantity()))))
                headerLabel.config(font=Verdana8, bg="light grey")

                headerLabel = Label(body, pady=10, text=tempitem.get_price())
                headerLabel.grid(column=2, row=1, padx=50, sticky=E)
                headerLabel.grid(column=2, row=1, padx=(35 - len(str(tempitem.get_price()))))
                headerLabel.config(font=Verdana8, bg="light grey")
                usedNames.append(tempitem.get_name())

        subTotalFrame = Frame(top)
        subTotalFrame.pack(side=TOP, fill=X)

        subtotalLabel = Label(subTotalFrame)
        subtotalLabel.pack(side=TOP, anchor='nw')

        subtotalLabel = Label(subTotalFrame, text="Subtotal: $" + str("%.2f" % subtotal))
        subtotalLabel.pack(side=TOP, anchor='nw')
        subtotalLabel.config(font=Verdana10, pady=10, padx=35)
        deliveryLabel = Label(subTotalFrame, text="Delivery: $" + str("%.2f" % delivery))
        deliveryLabel.pack(side=TOP, anchor='nw')
        deliveryLabel.config(font=Verdana10, pady=10, padx=35)
        taxLabel = Label(subTotalFrame, text="Tax:       $" + str("%.2f" % tax))
        taxLabel.pack(side=TOP, anchor='nw')
        taxLabel.config(font=Verdana10, pady=10, padx=35)
        totalLabel = Label(subTotalFrame, text="Total:      $" + str("%.2f" % total))
        totalLabel.pack(side=TOP, anchor='nw')
        totalLabel.config(font=Verdana10B, pady=10, padx=35)
        mainButton = Button(subTotalFrame, text='Place Order', command=self.lastClick)
        mainButton.pack()

        top.withdraw()

    # **********************************************************
    # ***** Function: onClick                              *****
    # **********************************************************
    # ***** Description: This function is activated on     *****
    # *****  the "Review" button. It checks to make sure   *****
    # *****  all entry fields are filled. It also removes  *****
    # *****  The current window, and centers the next window****
    # **********************************************************
    def onClick(self, shippingEntries, paymentEntries):
        for i in shippingEntries:
            if len(i.get()) == 0:
                showerror('error', 'Please make sure all shipping address fields are filled!')
                self.tkraise(aboveThis=None)
                return
        for i in paymentEntries:
            if len(i.get()) == 0:
                showerror('error', 'Please make sure all payment fields are filled!')
                self.tkraise(aboveThis=None)
                return
        self.withdraw()
        self.top.deiconify()
        center(self.top)

    # **********************************************************
    # ***** Function: lastClick                            *****
    # **********************************************************
    # ***** Description: This function is activated on     *****
    # *****  the "Place Order" button. It alerts the user  *****
    # *****  that the order has been successfully placed   *****
    # *****  and removes the current window.               *****
    # **********************************************************
    def lastClick(self):
        showinfo('Order Placed!', 'Your order has been placed and purchased!\n Thank you!')
        self.top.destroy()

# Demo().mainloop() #don't enter mainloop here that will happen when the frames are attached
