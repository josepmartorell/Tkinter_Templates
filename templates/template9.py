#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import package
from tkinter import *


def click():
    variable = parameter.get()
    try:
        dictionary[variable]
    except:
        screen.configure(text="Invalid key")


def close_window():
    root.destroy()
    exit()


# root window
root = Tk()
parameter = StringVar()
root.title("Panel control bot")
root.configure(background="white")
root.geometry("400x120")

# widgets
photo = PhotoImage(file="image.gif")
Label(root, image=photo, bg="white").grid(row=0, column=0, sticky=W)
Entry(root, textvariable=parameter, width=30, bg="white").place(x=150, y=60)
Button(root, text="START", width=14, command=click).grid(row=2, column=0, columnspan=2, sticky=W)
Button(root, text="EXIT", width=14, command=close_window).grid(row=6, column=0, columnspan=2, sticky=W)
screen = Label(root, text="", bg="white", fg="black", font="none 12 bold")
screen.place(x=150, y=90)

# set of parameters
dictionary = {'key1': 'value1',
              'key2': 'value2',
              'key3': 'value3',
              'key4': 'value4'}

# start window
root.mainloop()
