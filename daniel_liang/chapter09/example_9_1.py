from tkinter import *

window = Tk()
lab=Label(window, text = "Welcome to python");
btOk=Button(window, text = "ok")
btCancel=Button(window, text="cancel")

lab.pack()
btOk.pack()
btCancel.pack()

window.mainloop()
