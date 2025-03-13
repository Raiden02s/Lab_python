import tkinter as tk

window = tk.Tk()
window.title("lab-5")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

label1 = tk.Label(window, text="Виберіть валюту",width= 13,height=0)
label1.grid(row=0, column=0, padx=0, pady=2,sticky = "w")

currency_var = tk.StringVar(value="USD")

usd = 41.5
eur = 43.4

def show_selection():
    print("Вибрана валюта:", currency_var.get())
    a = currency_var.get()
    if a == "USD":
        currency_num.config(text = usd)
    else:
        currency_num.config(text = eur)

def calculate():
    print("calc")
    a = currency_var.get()
    number = number_entry.get()
    number = float(number)
    if a == "USD":
        result = number*usd
        print(result)
        result_label.config(text = result)
    else:
        result = number * eur
        print(result)
        result_label.config(text=result)



radiobutton_usd = tk.Radiobutton(window, text="USD", variable=currency_var, value="USD", command=show_selection)
radiobutton_eur = tk.Radiobutton(window, text="EUR", variable=currency_var, value="EUR", command=show_selection)


radiobutton_usd.grid(row=0, column=1)
radiobutton_eur.grid(row=1, column=1)

currency_label = tk.Label(window, text="Курс:",width= 0,height=0)
currency_label.grid(row=2,column = 0,sticky = "w")

currency_num =  tk.Label(window, text=f"25",width= 0,height=0)
currency_num.grid(row=2,column = 1,sticky = "w")

button = tk.Button(window, text="Calc", command=calculate,width = 12)
button.grid(row=4, column=0, pady=10)

result_label = tk.Label(window, text=f"0",width= 0,height=0)
result_label.grid(row=4,column = 1,sticky = "w")

number_enter = tk.Label(window, text="Enter a number:")
number_enter.grid(row=3, column=0, pady=10,sticky = "w")
number_entry = tk.Entry(window)
number_entry.grid(row=3, column=1, pady=10,sticky = "w")

window.mainloop()