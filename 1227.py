# import tkinter
# top = tkinter.Tk()
# label = tkinter.Label(top,text='Hello World', width=90 , height=5 , bg="green" , font=("Arial", 12))
# label.pack()
# tkinter.mainloop()




# import tkinter
# top = tkinter.Tk()
# label = tkinter.Label(top,text='one', width=90 , height=5 , bg="green" , font=("Arial", 12))
# label.pack()
# label = tkinter.Label(top,text='two', width=90 , height=10 , bg="red" , font=("Arial", 12))
# label.pack()
# label = tkinter.Label(top,text='three', width=90 , height=15 , bg="blue" , font=("Arial", 12))
# label.pack()
# tkinter.mainloop()




from tkinter import *

def Calculate1():
    a1 = int(text1.get('1.0',END))  #从行首取到行尾
    a2 = int(text2.get('1.0',END))
    a3 = a1 + a2
    a4 = a1 - a2
    a5 = a1 * a2
    a6 = a1 / a2
    text3.delete('1.0',END)
    text3.insert(INSERT,a3)
    text4.delete('1.0',END)
    text4.insert(INSERT,a4)
    text5.delete('1.0',END)
    text5.insert(INSERT,a5)
    text6.delete('1.0',END)
    text6.insert(INSERT,a6)

def Calculate2():
    a1 = int(text1.get('1.0',END))  #从行首取到行尾
    a2 = int(text2.get('1.0',END))
    a4 = a1 - a2
    text4.delete('1.0', END)
    text4.insert(INSERT, a4)

root = Tk()
root.title('计算器')
label1 = Label(root, text='First number:')
label1.grid(row=0,column=0)
text1 = Text(root, width=30,height=1)
text1.grid(row=1,column=0)
label2 = Label(root, text='Second number:')
label2.grid(row=2,column=0)
text2 = Text(root,width=30,height=1)
text2.grid(row=3,column=0)
label3 = Label(root, text='Result+:')
label3.grid(row=4,column=0)
text3 = Text(root,width=30,height=1)
text3.grid(row=5,column=0)
label4 = Label(root, text='Result-:')
label4.grid(row=6,column=0)
text4 = Text(root,width=30,height=1)
text4.grid(row=7,column=0)
label5 = Label(root, text='Result*:')
label5.grid(row=8,column=0)
text5 = Text(root,width=30,height=1)
text5.grid(row=9,column=0)
label5 = Label(root, text='Result/:')
label5.grid(row=10,column=0)
text6 = Text(root,width=30,height=1)
text6.grid(row=11,column=0)
button1 = Button(root,text='Calculate',command=Calculate1)
button1.grid(row=12,column=0)
button2 = Button(root,text='Calculate-',command=Calculate2)
button2.grid(row=13,column=0)
mainloop()