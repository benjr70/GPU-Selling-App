from Tkinter import *
from tkMessageBox import *

root = Tk()


#checkboxes
ChipLabel = Label(root, text = 'Chipset Type')
ChipLabel.config(height = 2)
ChipLabel.pack(side = TOP, anchor = W)
chipsetstate = []
chipset = ['Nivida','AMD','Intel']
for i, value in enumerate(chipset):
    var = IntVar()
    chk = Checkbutton(root, text=value, variable=var)
    chk.pack(side = TOP, anchor = W)
    chipsetstate.append(var)

MemSizeLAbel = Label(root, text = 'Memory Size')
MemSizeLAbel.config(height = 2)
MemSizeLAbel.pack(side = TOP , anchor = W)
MemSizeState = []
memorysize = ['> 11BG', '8GB','6GB','4GB','3GB','2GB','< 1GB',  ]
for i, value in enumerate(memorysize):
    var = IntVar()
    chk = Checkbutton(root, text=value, variable=var)
    chk.pack(side = TOP, anchor = W)
    MemSizeState.append(var)


root.mainloop()


