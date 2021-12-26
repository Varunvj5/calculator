# Importing tkinter library

import tkinter
from tkinter import *
from tkinter import messagebox

# Creating the window

root = tkinter.Tk()
root.geometry("250x400+500+100")
root.resizable(0, 0)
root.title("Calculator")


# Creating button frames in the window

data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=('Verdana', 20),
    textvariable=data,
    bg='#ffffff',
    fg='#000000',

)
lbl.pack(expand=True, fill="both")

btnr1 = Frame(root, bg="#000000")
btnr1.pack(expand=TRUE, fill="both")

btnr2 = Frame(root)
btnr2.pack(expand=TRUE, fill="both")

btnr3 = Frame(root)
btnr3.pack(expand=TRUE, fill="both")

btnr4 = Frame(root)
btnr4.pack(expand=TRUE, fill="both")

# Declaring function of the buttons

val = ''
A = 0
operator = ''

# # Functions of value buttons


def btn7isclicked():
    global val
    val = val + '7'
    data.set(val)


def btn8isclicked():
    global val
    val = val + '8'
    data.set(val)


def btn9isclicked():
    global val
    val = val + '9'
    data.set(val)


def btn4isclicked():
    global val
    val = val + '4'
    data.set(val)


def btn5isclicked():
    global val
    val = val + '5'
    data.set(val)


def btn6isclicked():
    global val
    val = val + '6'
    data.set(val)


def btn1isclicked():
    global val
    val = val + '1'
    data.set(val)


def btn2isclicked():
    global val
    val = val + '2'
    data.set(val)


def btn3isclicked():
    global val
    val = val + '3'
    data.set(val)


def btn0isclicked():
    global val
    val = val + '0'
    data.set(val)

# # Functions of operator buttons


def btnplusclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = '+'
    val = val + '+'
    data.set(val)


def btnminusclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = '-'
    val = val + '-'
    data.set(val)


def btnmultiplyclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = '*'
    val = val + '*'
    data.set(val)


def btndivideclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = '/'
    val = val + '/'
    data.set(val)

#  Function of clear button


def btncclicked():
    global A
    global operator
    global val
    val = ''
    A = 0
    operator = ''
    data.set(val)

# Function of equal to button


def btneqtoclicked():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == '-':
        x = int((val2.split('-')[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == '*':
        x = int((val2.split('*')[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == '/':
        x = int((val2.split('/')[1]))
        if x == 0:
            messagebox.showerror("ERROR!", "Division by 0 is not supported")
            A = ''
            val = ''
            data.set(val)
        else:
            c = int(A/x)
            data.set(c)
            val = str(c)

# Creating and formatting all the buttons


# Row 1
btn1 = Button(
    btnr1,
    text='7',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn7isclicked,
)
btn1.pack(side=LEFT, expand=TRUE, fill="both")

btn2 = Button(
    btnr1,
    text='8',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn8isclicked,
)
btn2.pack(side=LEFT, expand=TRUE, fill="both")

btn3 = Button(
    btnr1,
    text='9',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn9isclicked,
)
btn3.pack(side=LEFT, expand=TRUE, fill="both")

btn4 = Button(
    btnr1,
    text='+',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btnplusclicked,
)
btn4.pack(side=LEFT, expand=TRUE, fill="both")

# Row 2

btn5 = Button(
    btnr2,
    text='4',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn4isclicked,
)
btn5.pack(side=LEFT, expand=TRUE, fill="both")

btn6 = Button(
    btnr2,
    text='5',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn5isclicked,
)
btn6.pack(side=LEFT, expand=TRUE, fill="both")

btn7 = Button(
    btnr2,
    text='6',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn6isclicked,
)
btn7.pack(side=LEFT, expand=TRUE, fill="both")

btn8 = Button(
    btnr2,
    text='-',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btnminusclicked,
)
btn8.pack(side=LEFT, expand=TRUE, fill="both")

# Row 3

btn9 = Button(
    btnr3,
    text='1',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn1isclicked,
)
btn9.pack(side=LEFT, expand=TRUE, fill="both")

btn10 = Button(
    btnr3,
    text='2',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn2isclicked,
)
btn10.pack(side=LEFT, expand=TRUE, fill="both")

btn11 = Button(
    btnr3,
    text='3',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn3isclicked,
)
btn11.pack(side=LEFT, expand=TRUE, fill="both")

btn12 = Button(
    btnr3,
    text='x',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btnmultiplyclicked,
)
btn12.pack(side=LEFT, expand=TRUE, fill="both")

# Row 4

btn13 = Button(
    btnr4,
    text='C',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btncclicked,
)
btn13.pack(side=LEFT, expand=TRUE, fill="both")

btn14 = Button(
    btnr4,
    text='0',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btn0isclicked,
)
btn14.pack(side=LEFT, expand=TRUE, fill="both")

btn15 = Button(
    btnr4,
    text='=',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btneqtoclicked,
)
btn15.pack(side=LEFT, expand=TRUE, fill="both")

btn16 = Button(
    btnr4,
    text='/',
    font=('Verdana', 22),
    relief=GROOVE,
    border=0,
    command=btndivideclicked,
)
btn16.pack(side=LEFT, expand=TRUE, fill="both")


root.mainloop()
