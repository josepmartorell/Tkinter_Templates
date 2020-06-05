import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

"""Tkinter_GUI_Templates, 2020-06-05"""

"""********************************************************************************************************"""
"""****Starting from the tkinter grid template, I created an amazing interface for my new search engine****"""
"""********************************************************************************************************"""

# run mode selector
switch = int(input('\nSWITCH TEMPLATE RUN MODE:\n\t'
                   '- START TEMPLATE........(0 + Enter)\n\t'
                   '- FINAL TEMPLATE........(1 + Enter)\n'))
if switch != 1:

    colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

    r = 0
    for c in colours:
        tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=r, column=0)
        tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r, column=1)
        r = r + 1

    tk.mainloop()

else:

    def center(tk):
        w = 1100
        h = 373

        sw = tk.winfo_screenwidth()
        sh = tk.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        tk.geometry('%dx%d+%d+%d' % (w, h, x, y))


    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)

            self.master = master
            self.make_widgets()
            master.configure(background='white')
            master.resizable(width=False, height=False)

        def make_widgets(self):
            self.winfo_toplevel().title('JTECH search engine panel (www.jtech.network)')

            # create buttons
            buttons = [
                'SEARCH ENGINE',
                'SELECT TARGET',
                'JOURNAL FEED',
                'AUTOMATIC TRACKER',
                'LAUNCHER',
                'RECALL POINT',
                'CHECK BACK',
                'RESET ALL',
                'DISPLAY METER',
                'MAKE REPORT',
                'CAPTIONS HINT',

            ]

            row = 0
            for button in buttons:
                tk.Button(text=button, command=self.output, fg="black", bg="white", relief=tk.RIDGE, width=20).grid(
                    row=row, column=0)
                row = row + 1
            # START/STOP
            tk.Button(text='START/STOP', command=self.output, fg="black", bg="white", relief=tk.RIDGE, width=20).grid(
                row=11, column=0)

            # create labels + text fields
            colours = ['azure', 'azure', 'azure', 'azure']
            row = 0
            for colour in colours:
                tk.Entry(bg=colour, relief=tk.SUNKEN, width=80).grid(row=row, column=1)
                tk.Label(text=' * SET OFF last launchment <time>', bg='white').grid(row=row, column=2, sticky='w')
                row = row + 1

            # create tracker
            tracks = [' -> Track 1: deactivated at  <time>',
                      ' -> Track 2: deactivated at  <time>',
                      ' -> Track 3: deactivated at  <time>',
                      ' -> Track 4: deactivated at  <time>']
            row = 4
            for track in tracks:
                tk.Label(text=track, fg='gray', bg='white').grid(row=row, column=2, sticky='w')
                row = row + 1

            # create triggers meter
            triggers = ['   * Deactived: Auto. Traker <time>',
                        '   * Triggered: Journal Feed <time>',
                        '   * Deactived: Recall Point <time>',
                        '   * Deactived: Caption Hint <time>']
            row = 8
            for trigger in triggers:
                tk.Label(text=trigger, fg='black', bg='white').grid(row=row, column=2, sticky='w')
                row = row + 1

            # graphics style
            style.use('grayscale')

            # create object to insert into the drawing area
            fig = Figure()
            axl = fig.add_subplot(111)

            # create drawing area
            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.draw()
            # # position canvas
            canvas.get_tk_widget().place(x=189, y=130, width=644, height=240)

            # check graphic
            plt.show()

        def output(self):
            print("chévere!")


    root = tk.Tk()
    center(root)
    app = Application(master=root)
    app.mainloop()
