import tkinter as tk
from traceback import format_exception


def show():
    number = number_entry.get().strip()
    try:
        n = int(number)
        sum_result = 0
        for i in range(1, n + 1):
            sum_result += i
        if n >3:
            result_label.config(text=f"1+2+3+...+{n} = {sum_result}")
        elif n == 2:
            result_label.config(text=f"1+2 = {sum_result}")
        elif n == 1:
            result_label.config(text=f"1 = {sum_result}")
    except:
        result_label.config(text = "Enter a number!")



window = tk.Tk()
window.title("Lab-2")
window.geometry("260x100")

tk.Label(window, text="Enter a number:").grid(row=0, column=0, padx=10, pady=10)
number_entry = tk.Entry(window)
number_entry.grid(row=0, column=1, padx=10, pady=10)


validate_button = tk.Button(window, text="Calculate", command=show,width = 16)
validate_button.grid(row=1, column=1, pady=10)


result_label = tk.Label(window, text="", fg="black")
result_label.grid(row=1, column=0, pady=10)

window.mainloop()
