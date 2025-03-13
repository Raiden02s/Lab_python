import tkinter as tk

window = tk.Tk()
window.title("Lab-4")
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# Початкове значення
number = 0

# Мітка для відображення значення
label = tk.Label(window, text=f"{number}",width= 10,height=5)
label.grid(row=0, column=1)

# Функція для збільшення значення
def add():
    global number
    number += 1
    label.config(text=f"{number}")  # Оновлюємо мітку

# Функція для зменшення значення
def sub():
    global number
    number -= 1
    label.config(text=f"{number}")  # Оновлюємо мітку

# Кнопка для зменшення
sub_button = tk.Button(window, text="Sub", command=sub, width=10, height=5)
sub_button.grid(row=0, column=0)

# Кнопка для збільшення
add_button = tk.Button(window, text="Add", command=add, width=10, height=5)
add_button.grid(row=0, column=2)

window.mainloop()