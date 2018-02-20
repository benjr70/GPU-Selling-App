from Tkinter import *
from item_class import items
from PIL import ImageTk, Image
# ********************************* keep line 2-7 the same for every frame
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

        # Create a list of items
        item1 = items("GTX 1080 ti", 549.00, 11, 'Nivdia', '1080TI.jpg')
        item2 = items("GTX 1070 ti", 449.00, 8, 'Nivdia', '1070.jpg')
        itemName = [item1, item2]
        r = 0
        for selectedItem in enumerate(itemName):
            image = Image.open(selectedItem[1].get_pic())
            photo = ImageTk.PhotoImage(image)
            label = Label(interior,image=photo)
            label.image = photo # keep a reference!
            label.grid(column = 0, row = r)             
            
            itemname = Label(interior, text=selectedItem[1].get_name())
            itemname.grid(column = 1, row = r, sticky = N)
            itemname.config(relief=SUNKEN, height=1, bg='beige')
            itemprice = Label(interior, text=selectedItem[1].get_price())
            itemprice.grid(column = 2, row = r)
            itemprice.config(relief=SUNKEN, height=1, bg='beige')
            Button(interior, text = 'Add to cart').grid(column = 2, row = r, sticky = S)
            r = r +1
        canvas.pack()

#Demo().mainloop() #don't enter mainloop here that will happen when the frames are attached
