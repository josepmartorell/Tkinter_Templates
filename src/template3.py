#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter


def center(tk):
    w = 300
    h = 100

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    tk.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = tkinter.Tk()
root.resizable(width=False, height=False)


name = tkinter.StringVar()
tkinter.Entry(root, textvariable=name, width=30).grid(row=0, column=1)
tkinter.Label(root, text = 'Name').grid(row=0, column=0)

surname = tkinter.StringVar()
tkinter.Entry(root, textvariable=surname, width=30).grid(row=1, column=1)
tkinter.Label(root, text = 'Surname').grid(row=1, column=0)

cell_phone = tkinter.StringVar()
tkinter.Entry(root, textvariable=cell_phone, width=30).grid(row=2, column=1)
tkinter.Label(root, text = 'Cell phone').grid(row=2, column=0)


contacts={}
def save():
    nam = name.get()
    sur = surname.get()
    cell = cell_phone.get()
    contacts[cell] = [nam, sur]
    return contacts

button1 = tkinter.Button(root, text='Save', command = save).grid(row=4,
                                                            column=0,
                                                            columnspan=2,
                                                            sticky = 'ew')
button1_lambda = tkinter.Button\
    (root, text='Save', command = lambda: print(save())).grid(row=4, column=0, columnspan=2, sticky = 'ew')
center(root)
root.mainloop()