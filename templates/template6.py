#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tkinter_GUI_Templates, 2019-09-14"""

"""************************************************************************************"""
"""****going an step further the template6 includes connection with MySQL databases****"""
"""************************************************************************************"""

import pymysql.cursors
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox


"""***********************************************************************************"""
"""****this class contains the methods to connect and disconnect from the database****"""
"""***********************************************************************************"""


class Connect:

    @staticmethod
    def connect():
        try:
            connection = pymysql.connect(host='localhost',
                                         user='username',
                                         password='password',
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

    def insert(self, n, s, p, e):
        conn = self.connect() # make connection
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO contact VALUES(null, '"+n+"', '"+s+"', '"+p+"', '"+e+"')")
        conn.commit()
        self.disconnect(conn)


"""************************************"""
"""****finally we implement tkinter****"""
"""************************************"""


def center(tk):
    w = 400
    h = 350

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    tk.geometry('%dx%d+%d+%d' % (w, h, x, y))


def insert():
    contact = Contact()  # create an object of the Contact class
    contact.insert(name.get(), surname.get(), phone.get(), email.get())
    name.set("")
    surname.set("")
    phone.set("")
    email.set("")
    messagebox.showinfo("Message", "Contact inserted :)")


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
    Button(tab0, text="Save", bg="#00a", fg="white", command=insert).place(x=120, y=250)


root = Tk()
background_color = '#006'
font_color = '#FFF'
Style().configure("My.TFrame", background=background_color, foreground=font_color)
name = StringVar()
surname = StringVar()
phone = StringVar()
email = StringVar()
notebook = ttk.Notebook(root)
notebook.pack(fill='both',expand='yes')
tab_insert()
center(root)
root.mainloop()












