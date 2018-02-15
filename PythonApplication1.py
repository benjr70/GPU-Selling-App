from Tkinter import *
from tkMessageBox import *

def fetch():
    print 'Input => "%s"' %ent.get()

def notDone():
    showerror('Not implented','Not Available')

def makeMenu(win):
    top = Menu(win)
    win.config(menu = top)

    file = Menu(top, tearoff=0)
    file.add_command(label="new",command = notDone, underline = 0)
    top.add_cascade(label='File', menu = file, underline = 0)


root = Tk()
#top menu 
makeMenu(root)

#text search bar
ent = Entry(root)
ent.insert(0, 'search')
ent.grid(row = 0, column = 3, sticky = N)
ent.focus()
ent.bind('<Return>', (lambda event: fetch()))

#go button for search bar
btn = Button(root, text = 'GO', command = fetch)
btn.grid(row = 0, column = 3, sticky = E)

#item
msg = Label(root, text='item 1!!!!')
msg.grid(row = 0, column = 1)
msg.config(relief = SUNKEN, width = 50, height = 7, bg = 'beige')

#item
msg2 = Label(root, text='item 2!!!!')
msg2.grid(row = 1, column = 1)
msg2.config(relief = SUNKEN, width = 50, height = 7, bg = 'beige')

#item3
msg3 = Label(root, text='item 3!!!!')
msg3.grid(row = 2, column = 1)
msg3.config(relief = SUNKEN, width = 50, height = 7, bg = 'beige')

#item
msg = Label(root, text='item 1!!!!')
msg.grid(row = 3, column = 1)
msg.config(relief = SUNKEN, width = 50, height = 7, bg = 'beige')

#item
msg2 = Label(root, text='item 2!!!!')
msg2.grid(row = 4, column = 1)
msg2.config(relief = SUNKEN, width = 50, height = 7, bg = 'beige')

#item3
msg3 = Label(root, text='item 3!!!!')
msg3.grid(row = 5, column = 1)
msg3.config(relief = SUNKEN, width = 50, height = 7, bg = 'beige')

#checkboxes 
states = []
catName = ['red','blue','green','yellow','black','white']
for i, value in enumerate(catName):
    var = IntVar()
    chk = Checkbutton(root, text=value, variable=var)
    chk.grid(row = i,column = 0, sticky = W)
    states.append(var)



root.mainloop()