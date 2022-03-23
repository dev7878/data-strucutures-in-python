"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-14"
-------------------------------------------------------
"""
# Imports
from tkinter import *
from tkinter.ttk import *
from time import strftime
# Constants
root = Tk()
root.title("Clock")


def time():
    string = strftime("%H:%M:%S: %p")
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80),
              background="green", foreground="orange")
label.pack(anchor="center")
time()
mainloop()
