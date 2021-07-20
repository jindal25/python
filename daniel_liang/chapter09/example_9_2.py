from tkinter import *

class myGUIClass:
    def __init__(self):
        window = Tk()
        lab=Label(window, text = "Welcome to python");
        btOk=Button(window, text = "ok", fg = "red" ,command = self.commandOk)
        btCancel=Button(window, text="cancel", bg = "yellow" ,command = self.commandCancel)

        lab.pack()
        btOk.pack()
        btCancel.pack()

        window.mainloop()

    def commandOk(self):
        print(" OK button pressed")

    def commandCancel(self):
        print(" Cancel button pressed")

myGUIClass()
