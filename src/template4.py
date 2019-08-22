#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" template4 would be the draft of a basic contact list,
starting from the previous template number three ... """

from tkinter import *

""" initialize list to store contacts """
the_list = []

""" take the center method from template2 to place the main window """


def center(tk):
    w = 700
    h = 300

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    tk.geometry('%dx%d+%d+%d' % (w, h, x, y))


""" place here the methods to manage the contacts """


def save():
    print("Hello world!")


def remove():
    print("Hello world!")


""" set your main window here """
root = Tk()
name = StringVar()
surname = StringVar()
maternal_surname = StringVar()
phone = StringVar()
mail = StringVar()
delete_phone = StringVar()
background_color = '#006'
font_color = '#FFF'
root.title('tk')
root.configure(background = background_color)
my_label_title = Label(root, text='Agenda with files', bg=background_color,
                       fg=font_color,font=("Helvetica", 16)).place(x=230,y=10)

""" place your widgets here """
my_label_name = Label(root, text='Name', bg=background_color, fg=font_color).place(x=50,y=50)
my_box_name = Entry(root, textvariable=name).place(x=150,y=50)

my_label_surname = Label(root, text='Surname', bg=background_color, fg=font_color).place(x=50,y=80)
my_box_surname = Entry(root, textvariable=surname).place(x=150,y=80)

my_label_maternal_surname = Label(root, text='Maternal surn.', bg=background_color, fg=font_color).place(x=50,y=110)
my_box_maternal_surname = Entry(root, textvariable=maternal_surname).place(x=150,y=110)

my_label_phone = Label(root, text='Phone', bg=background_color, fg=font_color).place(x=50,y=140)
my_box_phone = Entry(root, textvariable=phone).place(x=150,y=140)

my_label_mail = Label(root, text='Mail', bg=background_color, fg=font_color).place(x=50,y=170)
my_box_mail = Entry(root, textvariable=mail).place(x=150,y=170)

my_label_delete_phone = Label(root, text='Phone', bg=background_color, fg=font_color).place(x=370,y=50)
my_spin_box_delete_phone = Spinbox(root, textvariable=delete_phone).place(x=450,y=50)

my_button_save_contact = Button(root, text="Save", command=save, bg="#009", fg="white").place(x=150,y=200)
my_button_remove_contact = Button(root, text="Remove", command=remove, bg="#009", fg="white").place(x=450,y=80)

""" spread the window """
center(root)
mainloop()