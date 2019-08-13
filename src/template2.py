#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter


def center(tk):
    w = 500
    h = 150

    sw = tk.winfo_screenwidth()
    sh = tk.winfo_screenheight()

    x = (sw - w) / 2
    y = (sh - h) / 2
    tk.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == '__main__':
    root = tkinter.Tk()
    root.resizable(width=False, height=False)
    center(root)

    root.mainloop()