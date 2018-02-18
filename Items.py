from Tkinter import *


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
        itemName = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'item 7']
        for selectedItem in enumerate(itemName):
            item = Label(interior, text=selectedItem[1])
            item.pack(expand=YES, fill=BOTH, side=TOP)
            item.config(relief=SUNKEN, width=40, height=7, bg='beige')

        canvas.pack()

# Demo().mainloop() don't enter mainloop here that will happen when the frames are attached
