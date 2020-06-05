import tkinter as tk

"""Tkinter_GUI_Templates, 2020-06-05"""

"""********************************************************************************************************"""
"""****starting with the next grid tkinter template build an awesome interface for my new search engine****"""
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
            self.pack()
            self.make_widgets()
            master.configure(background='white')

        def make_widgets(self):
            self.winfo_toplevel().title("Factiva's Search Engine")

            # create buttons
            self.check = tk.Button(self, fg="black", bg="gray")
            self.hint = tk.Button(self, fg="black", bg="gray")
            self.target = tk.Button(self, fg="black", bg="gray")
            self.search = tk.Button(self, fg="black", bg="gray")
            self.tracker = tk.Button(self, fg="black", bg="gray")
            self.recall = tk.Button(self, fg="black", bg="gray")
            self.feed = tk.Button(self, fg="black", bg="gray")
            self.report = tk.Button(self, fg="black", bg="gray")
            self.reset = tk.Button(self, fg="black", bg="gray")
            self.start = tk.Button(self, fg="black", bg="gray")
            self.display = tk.Button(self, fg="black", bg="gray")

            # text and commands settings
            self.check["text"] = "CHECK BACK"
            self.check["command"] = self.output

            self.hint["text"] = "CAPTIONS HINT"
            self.hint["command"] = self.output

            self.target["text"] = "SELECT TARGET"
            self.target["command"] = self.output

            self.search["text"] = "SEARCH ENGINE"
            self.search["command"] = self.output

            self.tracker["text"] = "AUTOMATIC TRACKER"
            self.tracker["command"] = self.output

            self.recall["text"] = "RECALL POINT"
            self.recall["command"] = self.output

            self.feed["text"] = "JOURNAL FEED"
            self.feed["command"] = self.output

            self.report["text"] = "MAKE REPORT"
            self.report["command"] = self.output

            self.reset["text"] = "RESET ALL"
            self.reset["command"] = self.master.destroy

            self.start["text"] = "START/STOP"
            self.start["command"] = self.master.destroy

            self.display["text"] = "METRIC DISPLAYER"
            self.display["command"] = self.master.destroy

            # widgets packing
            self.check.pack(side="bottom", ipadx=0, fill="x")
            self.hint.pack(side="bottom", ipadx=0, fill="x")
            self.target.pack(side="bottom", ipadx=0, fill="x")
            self.search.pack(side="bottom", ipadx=0, fill="x")
            self.tracker.pack(side="bottom", ipadx=0, fill="x")
            self.recall.pack(side="bottom", ipadx=0, fill="x")
            self.feed.pack(side="bottom", ipadx=0, fill="x")
            self.report.pack(side="bottom", ipadx=0, fill="x")
            self.reset.pack(side="bottom", ipadx=0, fill="x")
            self.start.pack(side="bottom", ipadx=0, fill="x")
            self.display.pack(side="bottom", ipadx=0, fill="x")

        def output(self):
            print("chévere!")


    root = tk.Tk()
    center(root)
    app = Application(master=root)
    app.mainloop()
