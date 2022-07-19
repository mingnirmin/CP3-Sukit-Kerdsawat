from tkinter import *
import math

def CalBMI(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if BMI < 18.5:
        labelResult.configure(text="{:.2f}".format(BMI),bg="brown")
        labelResult2.configure(text="ผอม")
    elif BMI < 22.9 and BMI > 18.5 :
        labelResult.configure(text="{:.2f}".format(BMI),bg="brown")
        labelResult2.configure(text="สุขภาพดี")
    elif BMI < 24.9 and BMI > 23:
        labelResult.configure(text="{:.2f}".format(BMI),bg="brown")
        labelResult2.configure(text="ท้วม")
    elif BMI < 29.9 and BMI > 25:
        labelResult.configure(text="{:.2f}".format(BMI),bg="brown")
        labelResult2.configure(text="อ้วน")
    else:
        labelResult.configure(text="{:.2f}".format(BMI),bg="brown")
        labelResult2.configure(text="อ้วนมาก")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)",font=("FC Daisy",30))
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)",font=("FC Daisy",30))
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน",font=("FC Daisy",30))
calculateButton.bind('<Button-1>', CalBMI)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์",font=("FC Daisy",30))
labelResult.grid(row=2,column=1)
labelResult2 = Label(MainWindow,text="",font=("FC Daisy",30))
labelResult2.grid(row=3,column=1)

MainWindow.mainloop()