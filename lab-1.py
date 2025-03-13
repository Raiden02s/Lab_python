import tkinter as tk
from PIL import Image
def show():
    name = name_entry.get().strip()
    if name:
        greeting_label.config(text=f"Welcome {name}!")
    else:
        greeting_label.config(text="Please enter your name.")


window = tk.Tk()
window.title("Lab-1")
window.geometry("260x150")

tk.Label(window, text="Enter your name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)


validate_button = tk.Button(window, text="Show", command=show,width = 16)
validate_button.grid(row=1, column=1, pady=10)


greeting_label = tk.Label(window, text="", fg="black", font=("Arial", 12))
greeting_label.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()

