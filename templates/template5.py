#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" template5 comes to complete the previous one
incorporating a file as a database ... """

from tkinter import *
from tkinter import messagebox

# initialize list to store contacts
the_list = []


# place all application methods below
def center(tk):
    w = 700
    h = 500

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    tk.geometry('%dx%d+%d+%d' % (w, h, x, y))


def start_file():
    my_file = open("my_file.txt", "a")
    my_file.close()


def load():  # load the file into the list
    my_file = open("my_file.txt", "r")
    line = my_file.readline()
    # if you find the first line iterate all lines found
    if line:
        while line:
            if line[-1] == '\n':
                line = line[:-1]
                # store all lines in the list
            the_list.append(line)
            line = my_file.readline()
    my_file.close()


def write_contact():
    my_file = open("my_file.txt", "w")
    the_list.sort()
    for element in the_list:
        my_file.write(element + '\n')
    my_file.close()


def consult():
    global my_spin_phone
    my_consult = Text(root, width=80, height=15)  # text widget
    the_list.sort()
    values = []
    my_consult.insert(INSERT, "Name\t\tSurname\t\tMaternal sur.\t\tPhone\t\tMail\n")
    for element in the_list:
        arrangement = element.split("$")
        values.append(arrangement[3])
        my_consult.insert(INSERT, arrangement[0] + "\t\t"
                          + arrangement[1] + "\t\t"
                          + arrangement[2] + "\t\t"
                          + arrangement[3] + "\t\t"
                          + arrangement[4] + "\t\n")
        my_consult.place(x=20, y=230)
        # note that 'values' is the default widget value:
        my_spin_phone = Spinbox(root, value=values, textvariable=delete_contact).place(x=450, y=50)  # Spinbox widget
        # if it is confirmed that the list is empty we set Spinbox without the variable 'delete_contact'
    if not the_list:
        my_spin_phone = Spinbox(root, value=values).place(x=450, y=50)  # Spinbox widget reset


def save():
    # get all entry-variables
    get_name = name.get()
    get_surname = surname.get()
    get_maternal_surname = maternal_surname.get()
    get_phone = phone.get()
    get_mail = mail.get()
    # append to the list
    the_list.append(get_name + '$'
                    + get_surname + '$'
                    + get_maternal_surname + '$'
                    + get_phone + '$'
                    + get_mail)
    # call above method to write contact
    write_contact()
    # pop-up notification
    messagebox.showinfo("Saved", "The contact has been saved in the phonebook")
    # clean fields
    name.set("")
    surname.set("")
    maternal_surname.set("")
    phone.set("")
    mail.set("")
    consult()  # update


def remove():
    deleted = delete_contact.get()
    removed = False  # to check if it is deleted correctly
    for element in the_list:
        arrangement = element.split('$')
        if deleted == arrangement[3]:
            the_list.remove(element)
            removed = True
    write_contact()  # update
    consult()
    if removed:
        messagebox.showinfo('Remove', 'Item Deleted: ' + deleted)


# set your main window here
root = Tk()
name = StringVar()
surname = StringVar()
maternal_surname = StringVar()
phone = StringVar()
mail = StringVar()
delete_contact = StringVar()
background_color = '#066'
font_color = '#FFF'
root.title('tk')
root.configure(background=background_color)

# initialize the agenda with the loading and query methods after the main window
start_file()
load()
consult()  # update

# place your widgets here
my_label_title = Label(root, text='Agenda with files', bg=background_color,
                       fg=font_color, font=("Helvetica", 16)).place(x=230, y=10)

my_label_name = Label(root, text='Name', bg=background_color, fg=font_color).place(x=50, y=50)
my_box_name = Entry(root, textvariable=name).place(x=150, y=50)

my_label_surname = Label(root, text='Surname', bg=background_color, fg=font_color).place(x=50, y=80)
my_box_surname = Entry(root, textvariable=surname).place(x=150, y=80)

my_label_maternal_surname = Label(root, text='Maternal sur.', bg=background_color, fg=font_color).place(x=50, y=110)
my_box_maternal_surname = Entry(root, textvariable=maternal_surname).place(x=150, y=110)

my_label_phone = Label(root, text='Phone', bg=background_color, fg=font_color).place(x=50, y=140)
my_box_phone = Entry(root, textvariable=phone).place(x=150, y=140)

my_label_mail = Label(root, text='Mail', bg=background_color, fg=font_color).place(x=50, y=170)
my_box_mail = Entry(root, textvariable=mail).place(x=150, y=170)

my_label_spin_phone = Label(root, text='Phone', bg=background_color, fg=font_color).place(x=370, y=50)
my_spin_phone = Spinbox(root, textvariable=delete_contact).place(x=450, y=50)

my_button_save_contact = Button(root, text="Save", command=save, bg="#099", fg="white").place(x=150, y=200)
my_button_remove_contact = Button(root, text="Remove", command=remove, bg="#099", fg="white").place(x=450, y=80)

# spread the window
center(root)
mainloop()
