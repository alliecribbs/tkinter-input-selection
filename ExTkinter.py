from Tkinter import *

class Program:

def __init__(self):
    a = Radiobutton(text="Option A", command=self.callback, variable = "gr1", value = 1).pack()
    b = Radiobutton(text="Option B", command=self.callback, variable = "gr1", value = 2).pack()
    c = Radiobutton(text="Option C", command=self.callback, variable = "gr1", value = 3).pack()


def callback(self):
    print "clicked!"
program = Program()

mainloop()