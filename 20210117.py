from datetime import *
import tkinter as tk
from tkinter import *
from tkinter import ttk

solar_month = [1,3,5,7,8,10,12]
lunar_month = [4,6,9,11]


def Calculate1():
    a1 = int(text1.get('1.0',END))
    a2 = int(text2.get('1.0',END))
    a3 = int(text3.get('1.0',END))
    dt1 = date.today()
    dt2 = date(a1, a2, a3)
    a4 = (dt1 - dt2).days
    text4.delete('1.0', END)
    text4.insert(INSERT, a4)

def Calculate2():
    a1 = int(text1.get('1.0', END))
    a2 = int(text2.get('1.0', END))
    a3 = int(text3.get('1.0', END))
    a5 = int(text5.get('1.0', END))
    a6 = int(text6.get('1.0', END))
    a7 = int(text7.get('1.0', END))
    dt2 = date(a1, a2, a3)
    dt3 = date(a5, a6, a7)
    a8 = (dt3 - dt2).days
    text8.delete('1.0', END)
    text8.insert(INSERT, a8)

root = Tk()
root.title('日期计算器')
label1 = Label(root,text='year1')
label1.grid(row=0,column=0)
text1 = Text(root, width=30,height=1)
text1.grid(row=1,column=0)
label2 = Label(root,text='month1')
label2.grid(row=2,column=0)
text2 = Text(root, width=30,height=1)
text2.grid(row=3,column=0)
label3 = Label(root,text='day1')
label3.grid(row=4,column=0)
text3 = Text(root, width=30,height=1)
text3.grid(row=5,column=0)
button1 = Button(root,text='Calculate1',command=Calculate1)
button1.grid(row=6,column=0)
label4 = Label(root,text='result')
label4.grid(row=7,column=0)
text4 = Text(root, width=30,height=1)
text4.grid(row=7,column=1)

label5 = Label(root,text='year2')
label5.grid(row=0,column=1)
text5 = Text(root, width=30,height=1)
text5.grid(row=1,column=1)
label6 = Label(root,text='month2')
label6.grid(row=2,column=1)
text6 = Text(root, width=30,height=1)
text6.grid(row=3,column=1)
label7 = Label(root,text='day2')
label7.grid(row=4,column=1)
text7 = Text(root, width=30,height=1)
text7.grid(row=5,column=1)
button2 = Button(root,text='Calculate2',command=Calculate2)
button2.grid(row=6,column=1)
text8 = Text(root, width=30,height=1)
text8.grid(row=7,column=1)

number = tk.StringVar()
b1 = ttk.Combobox(root, width=20,textvariable=number)
b1['values'] = (list(range(1,13)))
b1.grid(column=0, row=3)

b2 = ttk.Combobox(root, width=20,)
b2['values'] = (list(range(1,13)))
b2.grid(column=1, row=3)

x1v = tk.StringVar()
b3 = ttk.Combobox(root, width=20,textvariable=x1v)
b3['values'] = (list(range(1,32)))
b3.grid(column=0, row=5)

b4 = ttk.Combobox(root, width=20,)
b4['values'] = (list(range(1,32)))
b4.grid(column=1, row=5)

b5 = ttk.Combobox(root, width=20,)
b5['values'] = (list(range(1900,2100)))
b5.grid(column=0, row=1)

b6 = ttk.Combobox(root, width=20,)
b6['values'] = (list(range(1900,2100)))
b6.grid(column=1, row=1)


# com = ttk.Combobox(root,textvariable=number)
# com.pack()
# com['value']=list(range(1,13))

max = 0

def xFunc(event):
    global max
    # print(com.get())  # #获取选中的值方法1
    # print(xVariable.get())  # #获取选中的值方法2
    if int(b1.get()) in solar_month:
        print('in solar ')
        max = 32
    elif int(b1.get()) in lunar_month:
        max = 31
    elif int(b1.get()) == 2:
        max = 29
    b3['value'] = list(range(1,max))

b1.bind("<<ComboboxSelected>>", xFunc)

mainloop()

# print(a4)
# print(a5)

