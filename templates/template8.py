#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tkinter_GUI_Templates:
    Template 8 consists of a small control selector panel with some basic design features."""

import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        if __name__ == '__main__':
            main_window.title("Position elements in Tcl/Tk")

        # create notebook
        self.notebook = ttk.Notebook(self)

        # create content notebook
        self.tab1_label = ttk.Label(self.notebook,
                                    text="Write description for the tab 1")
        # self.tab1_image = tk.PhotoImage(file="images.png")
        self.tab2_label = ttk.Label(self.notebook,
                                    text="Write description for the tab 2")
        self.tab3_label = ttk.Label(self.notebook,
                                    text="Write description for the tab 3")
        self.tab4_label = ttk.Label(self.notebook,
                                    text="Write description for the tab 4")


        # add them to the notebook
        self.notebook.add(self.tab1_label, text="Tab_one", padding=20)
        # self.notebook.add(self.tab1_label, text="Tab_one", image=self.tab1_image, compound=tk.LEFT, padding=20)
        self.notebook.add(self.tab2_label, text="Tab_two ", padding=20)
        self.notebook.add(self.tab3_label, text="Tab_three ", padding=20)
        self.notebook.add(self.tab4_label, text="Tab_four", padding=20)

        self.notebook.pack(padx=10, pady=10)
        self.pack()


root = tk.Tk()
root.resizable(width=False, height=False)
app = Application(root)
root.mainloop()
