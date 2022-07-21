from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter import ttk
import datetime

currency_list = CurrencyRates()

month = ["1","2","3","4","5","6","7","8","9","10","11","12"]

def click_average_currency(event):
    sum = 0
    m = int(text_box_month.get())
    currency = first_currency_select.get()
    currency2 = second_currency_select.get()
    if m == 4 or m == 6 or m == 9 or m == 11:
        d = 30
        for i in range(1,30):
            date_obj = datetime.datetime(2021, m, i)
            sum += currency_list.get_rate(currency, currency2, date_obj)
    elif m == 2:
        d = 28
        for i in range(1, 28):
            date_obj = datetime.datetime(2021, 2, i)
            sum += currency_list.get_rate(currency, currency2, date_obj)
    else:
        d = 31
        for i in range(1,31):
            date_obj = datetime.datetime(2021, m, i)
            sum += currency_list.get_rates(currency, currency2, date_obj)
    res = round(sum/d, 3)
    label_result.configure(text=res)

MainWindow = Tk()
label_title = Label(MainWindow,text='คำนวณหาค่าเฉลี่ยของหน่วยเงินที่ต้องการ',font=("Helvetica",20))
label_title.grid(row=0, column=0)
label_title2 = Label(MainWindow,text='(ข้อมูลของปี 2021)',font=("Helvetica",20))
label_title2.grid(row=0, column=1)

label_month = Label(MainWindow, text="เดือน",font=("Helvetica",15))
label_month.grid(row=1, column=0)
label_currency = Label(MainWindow, text="หน่วยเงินที่ต้องการหาค่าเฉลี่ย",font=("Helvetica",15))
label_currency.grid(row=2, column=0)
label_currency2 = Label(MainWindow, text="หน่วยเงินค่าเฉลี่ย",font=("Helvetica",15))
label_currency2.grid(row=3, column=0)
text_box_month = ttk.Combobox(MainWindow, values=list(month))
text_box_month.current(0)
text_box_month.grid(row=1, column=1)
label_result = Label(MainWindow, text="ผลลัพธ์",font=("Helvetica",15))
label_result.grid(row=4, column=1)

#Select Currency Unit
first_currency_select = ttk.Combobox(MainWindow, values=list(currency_list.get_rates("").keys()))
first_currency_select.current(0)
first_currency_select.bind("<<ComboboxSelected>>")
first_currency_select.grid(row=2, column=1)
second_currency_select = ttk.Combobox(MainWindow, values=list(currency_list.get_rates("").keys()))
second_currency_select.current(28)
second_currency_select.bind("<<ComboboxSelected>>")
second_currency_select.grid(row=3, column=1)

calculate_button = Button(MainWindow,text = "คำนวณหาค่าเฉลี่ย",font=("Helvetica",10))
calculate_button.bind('<Button-1>', click_average_currency)
calculate_button.grid(row=4,column=0)

MainWindow.mainloop()