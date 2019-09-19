#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import package
from tkinter import *

# set of parameters
values = {'key1': 'value1',
          'key2': 'value2',
          'key3': 'value3',
          'key4': 'value4'}


def click():
    pass


def close_window():
    root.destroy()
    exit()


# root window
root = Tk()
parameter = StringVar()
output = StringVar()
root.title("Panel control bot")
root.configure(background="white")
root.geometry("400x120")

# widgets
photo = PhotoImage(file="image.gif")
Label(root, image=photo, bg="white").grid(row=0, column=0, sticky=W)
Entry(root, textvariable=parameter, width=30, bg="white").place(x=150, y=60)
Button(root, text="START", width=14, command=click).grid(row=2, column=0, columnspan=2, sticky=W)
Button(root, text="EXIT", width=14, command=close_window).grid(row=6, column=0, columnspan=2, sticky=W)
Label(root, textvariable=output, bg="white", fg="black", font="none 12 bold").place(x=150, y=90)

# start window
root.mainloop()
