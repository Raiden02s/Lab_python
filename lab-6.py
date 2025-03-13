import tkinter as tk
from random import randint

window = tk.Tk()
window.title("lab-6")
window.geometry("200x150")
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

a = randint(0,100)
attempts = 0
def quess():
    global attempts
    attempts += 1
    quess_nunber = guess_enter.get()
    try:

        quess_nunber = int(quess_nunber)
        if quess_nunber == a:
            Label_quess.config(text=f"Right number was: {a} \n Attempts:{attempts}")
            print(attempts)
        elif quess_nunber > a:
            Label_quess.config(text="quess > a")
            print(attempts)
        else:
            Label_quess.config(text="quess < a")
            print(attempts)

    except:
        Label_quess.config(text="Error")

Label1 = tk.Label(window,text="Quess number 1-100")
Label1.grid(row = 0,column = 0,columnspan=2)

guess_enter = tk.Entry(window)
guess_enter.grid(columnspan=2)

quess_button = tk.Button(window,command = quess,text ="Check",padx=10,pady=10)
quess_button.grid(row=2, column = 0,sticky = "e")

Label_quess = tk.Label(window,text="help",padx=10,pady=10)
Label_quess.grid(row = 2,column = 1,sticky = "w")

window.mainloop()