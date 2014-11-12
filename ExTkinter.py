from Tkinter import *

class Program:
    def __init__(self):
        self.r = Tk()           # We have to initialize it first.
        self.gr1 = IntVar()     # And initialize the place where we'll have the info.
        a = Radiobutton(text="Option A", command=self.callback, variable = self.gr1, value = 1).pack()
        b = Radiobutton(text="Option B", command=self.callback, variable = self.gr1, value = 2).pack()
        c = Radiobutton(text="Option C", command=self.callback, variable = self.gr1, value = 3).pack()


    def callback(self):
        print "clicked!"
        print "The state of gr1 is " + str(self.gr1.get()) # Notice here we need to get the value from the variable.

if __name__ == '__main__':
    program = Program()  #Initialize the class instance.

    mainloop()  # Everything just spins here.
