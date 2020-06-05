import tkinter as tk

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
        w = 1200
        h = 340

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

        def make_widgets(self):
            self.winfo_toplevel().title("Factiva's Search Engine")

            # create buttons
            buttons = ['CHECK BACK',
                       'CAPTIONS HINT',
                       'SELECT TARGET',
                       'SEARCH ENGINE',
                       'AUTOMATIC TRACKER',
                       'RECALL POINT',
                       'JOURNAL FEED',
                       'MAKE REPORT',
                       'RESET ALL',
                       'START/STOP',
                       'METRIC DISPLAYER']

            row = 0
            for button in buttons:
                tk.Button(text=button, command=self.output, fg="black", bg="white", relief=tk.RIDGE, width=20).grid(row=row, column=0)
                row = row + 1

            # tk.Entry(bg="gray", relief=tk.SUNKEN, width=10).grid(row=0, column=1)

        def output(self):
            print("chévere!")


    root = tk.Tk()
    center(root)
    app = Application(master=root)
    app.mainloop()
