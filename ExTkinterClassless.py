from Tkinter import *

def callback():
    print "clicked!"
    print "The state of gr1 is " + str(gr1.get()) # Notice here we need to get the value from the variable.

r = Tk()           # We have to initialize it first.
gr1 = IntVar()     # And initialize the place where we'll have the info.
a = Radiobutton(text="Option A", command=callback, variable = gr1, value = 1).pack()
b = Radiobutton(text="Option B", command=callback, variable = gr1, value = 2).pack()
c = Radiobutton(text="Option C", command=callback, variable = gr1, value = 3).pack()

mainloop()  # Everything just spins here.
