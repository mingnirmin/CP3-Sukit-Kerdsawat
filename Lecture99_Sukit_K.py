from tkinter import *
import math

def CalBMI(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if BMI < 18.5:
        labelResult.configure(text="ผอม")
    elif BMI < 22.9 and BMI > 18.5 :
        labelResult.configure(text="สุขภาพดี")
    elif BMI < 24.9 and BMI > 23:
        labelResult.configure(text="ท้วม")
    elif BMI < 29.9 and BMI > 25:
        labelResult.configure(text="อ้วน")
    else:
        labelResult.configure(text="อ้วนมาก")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', CalBMI)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()