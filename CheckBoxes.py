from Tkinter import *

class checkbox(Tk):
    chipsetstate = []
    MemSizeState = []
    
class Demo(Frame):

    
    def __init__(self,  parent = None):
        Frame.__init__(self)
        self.pack()
        #root = Tk()
        #checkboxes
        ChipLabel = Label(self, text = 'Chipset Type')
        ChipLabel.config(height = 2)
        ChipLabel.pack(side = TOP, anchor = W)
        global chipsetstate
        chipsetstate = []
        chipset = ['Nvida','AMD','Intel']
        for i, value in enumerate(chipset):
            var = IntVar()
            chk = Checkbutton(self, text=value, variable=var)
            chk.pack(side = TOP, anchor = W)
            chipsetstate.append(var)

        MemSizeLAbel = Label(self, text = 'Memory Size')
        MemSizeLAbel.config(height = 2)
        MemSizeLAbel.pack(side = TOP , anchor = W)
        global MemSizeState
        MemSizeState = []
        memorysize = ['> 11BG', '8GB','6GB','4GB','3GB','2GB','< 1GB',  ]
        for i, value in enumerate(memorysize):
            var = IntVar()
            chk = Checkbutton(self, text=value, variable=var)
            chk.pack(side = TOP, anchor = W)
            MemSizeState.append(var)       
#if __name__ == '_main_':

#Demo().mainloop()




