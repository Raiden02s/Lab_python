import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Lab-3")
window.geometry("300x200")

mainmenu = Menu(window)

window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit")

helpmenu = Menu(mainmenu,tearoff=0)
helpmenu.add_command(label="Python docs")

mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)

window.mainloop()