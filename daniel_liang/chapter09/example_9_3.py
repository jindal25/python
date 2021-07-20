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
        lab1=Label(frame2, text = " Enter your name:");
        self.name = StringVar()
        ent=Entry(frame2, textvariable=self.name)
        msg=Message(frame2, text = " this is a widget window")
        radb=Button(frame2, text="Get name", command=self.processRadio)
        lab1.grid(row = 1, column = 1)
        ent.grid(row = 1 , column = 2)
        msg.grid(row = 1 , column = 3)
        radb.grid(row = 1, column = 4)

        text=Text(window)
        text.pack()
        text.insert(END,"this is the window")
        text.insert(END,"this showsn many windows")


        window.mainloop()


    def processCheckButton(self):
        print(" procesCheckButton");

    def processRadioButton(self):
        print("processRadioButton");

    def processRadio(self):
        print("processRadio your name is " + self.name.get());

widgetDemo()
