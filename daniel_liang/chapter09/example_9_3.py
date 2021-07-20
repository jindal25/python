from tkinter import *

class widgetDemo:
    def __init__(self):
        window =Tk()
        window.title("widget demo")

        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar();
        ckbt = Checkbutton(frame1, text = "bold", variable = self.v1 ,command = self.processCheckButton)
        self.v2 = IntVar();
        radioButton1 = Radiobutton(frame1, text = "red" ,bg = "red" ,value = 1 ,command = self.processRadioButton)
        radioButton2 = Radiobutton(frame1, text = "yellow", bg = "yellow", value =2 , command = self.processRadioButton)


        ckbt.grid(row = 1 , column = 1)
        radioButton1.grid(row = 1 , column = 2)
        radioButton2.grid(row = 1 , column = 3)

        frame2 = Frame(window)
        frame2.pack()

        window.mainloop()


    def processCheckButton(self):
        print(" procesCheckButton");

    def processRadioButton(self):
        print("processRadioButton");


widgetDemo()
