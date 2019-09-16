#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tkinter_GUI_Templates, 2019-09-16
 Template 7 includes a step beyond the previous one, making a query and displaying it on the screen"""


import pymysql.cursors
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox

"""*************************************************************"""
"""****the class to connect and disconnect from the database****"""
"""*************************************************************"""


class Connect:

    @staticmethod
    def connect():
        try:
            connection = pymysql.connect(host='localhost',
                                         user='your_username',
                                         password='your_password',
                                         db='agenda',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            print("connect successful!!")
            return connection
        except pymysql.MySQLError as e:
            print(e)

    @staticmethod
    def disconnect(connection):
        print("connection is running over")
        connection.close()
        print("connection is over")
        return None


"""*******************************************************************************"""
"""****In the class below we will place the methods to manipulate the database****"""
"""*******************************************************************************"""


class Contact(Connect):

    def sql_insert(self, n, s, p, e):
        conn = self.connect()  # make connection
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO contact VALUES(null, '" + n + "', '" + s + "', '" + p + "', '" + e + "')")
        conn.commit()
        self.disconnect(conn)

    def sql_query(self):
        conn = self.connect()  # make connection
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM contact")
        array = []
        for (contact) in cursor:
            array.append(contact)
        self.disconnect(conn)
        return array


"""************************************"""
"""****finally we implement tkinter****"""
"""************************************"""


def center(tk):
    w = 700
    h = 350

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    tk.geometry('%dx%d+%d+%d' % (w, h, x, y))


def do_insert():
    contact = Contact()  # create an object of the Contact class
    contact.sql_insert(name.get(), surname.get(), phone.get(), email.get())
    name.set("")
    surname.set("")
    phone.set("")
    email.set("")
    messagebox.showinfo("Message", "Contact inserted :)")
    do_query()


def do_query():
    widget_text.config(state=NORMAL)  # configure the widget to prevent accidental deletion
    widget_text.delete("1.0", END)
    widget_text.insert(INSERT, "Name\t\tSurname\t\tPhone\t\tEmail\t\n")
    contact = Contact()
    array = contact.sql_query()
    for c in array:
        widget_text.insert(INSERT, c) # TODO: replacement for the fragment below which throws an exception KeyError

#        text.insert(INSERT, c[1] + "\t\t"
#                    + c[2] + "\t\t"
#                    + c[3] + "\t\t"
#                    + c[4] + "\n")

    widget_text.place(x=20, y=30)
    widget_text.config(state=DISABLED)


def tab_insert():
    tab0 = ttk.Frame(notebook, style='My.TFrame')
    notebook.add(tab0, text="Insert")
    Label(tab0, text="Name = ", bg=background_color, fg=font_color).place(x=20, y=50)
    Label(tab0, text="Surname = ", bg=background_color, fg=font_color).place(x=20, y=100)
    Label(tab0, text="Phone = ", bg=background_color, fg=font_color).place(x=20, y=150)
    Label(tab0, text="Email = ", bg=background_color, fg=font_color).place(x=20, y=200)
    Entry(tab0, textvariable=name).place(x=120, y=50)
    Entry(tab0, textvariable=surname).place(x=120, y=100)
    Entry(tab0, textvariable=phone).place(x=120, y=150)
    Entry(tab0, textvariable=email).place(x=120, y=200)
    Button(tab0, text="Save", bg="#00a", fg="white", command=do_insert).place(x=120, y=250)


root = Tk()
background_color = '#006'
font_color = '#FFF'
Style().configure("My.TFrame", background=background_color, foreground=font_color)
name = StringVar()
surname = StringVar()
phone = StringVar()
email = StringVar()
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')
tab_insert()
tab1 = ttk.Frame(notebook, style='My.TFrame')  # including a new tab
notebook.add(tab1, text="Query")  # adding
widget_text = Text(tab1, width=70, height=15)  # add widget and assign it to a variable
do_query()
center(root)
root.mainloop()
