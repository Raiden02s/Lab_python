import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("200x310")
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2,3], minsize=50, weight=1)

Calc_enter = tk.Entry(window,width=30,font=('Arial', 20))
Calc_enter.insert(0, "0")
Calc_enter.grid(columnspan=4,pady = 0,padx = 0)
index1 = 0
# Number buttons
def num1():
    global index1
    index1 +=1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"1")
def num2():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"2")
def num3():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"3")
def num4():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"4")
def num5():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"5")
def num6():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"6")
def num7():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"7")
def num8():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"8")
def num9():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"9")
# Number buttons

# to do buttons
def add():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"+")
def sub():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"-")
def mult():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"*")
def div():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"/")
def open_1():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"(")
def close():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f")")

def num0():
    global index1
    index1 += 1
    if index1 == 1:
        Calc_enter.delete(0, tk.END)
    Calc_enter.insert(index1, f"0")
#MAIN FUNCTION!!
def calc():
    print("calc")
    evasion = Calc_enter.get()
    try:
        print(evasion)
        result = eval(evasion)
        Calc_enter.delete(0, tk.END)
        Calc_enter.insert(0, f"{result}")

        global index1
        index1 = 1
    except:
        Calc_enter.delete(0, tk.END)
        Calc_enter.insert(0, "Error")
        print("Some error has occured")

#MAIN FUNCTION!!
def clear():
    Calc_enter.delete(0, tk.END)
# to do buttons

num1_button = tk.Button(window,command = num1 ,text ="1",width = 6,height=3,pady=0,padx=0)
num1_button.grid(row=1, column = 0,sticky = "n")

num2_button = tk.Button(window,command = num2 ,text ="2",width = 6,height=3,pady=0,padx=0)
num2_button.grid(row=1, column = 1,sticky = "n")

num3_button = tk.Button(window,command = num3 ,text ="3",width = 6,height=3,pady=0,padx=0)
num3_button.grid(row=1, column = 2,sticky = "n")

num4_button = tk.Button(window,command = num4 ,text ="4",width = 6,height=3,pady=0,padx=0)
num4_button.grid(row=2, column = 0,sticky = "n")

num5_button = tk.Button(window,command = num5 ,text ="5",width = 6,height=3,pady=0,padx=0)
num5_button.grid(row=2, column = 1,sticky = "n")

num6_button = tk.Button(window,command = num6 ,text ="6",width = 6,height=3,pady=0,padx=0)
num6_button.grid(row=2, column = 2,sticky = "n")

num7_button = tk.Button(window,command = num7 ,text ="7",width = 6,height=3,pady=0,padx=0)
num7_button.grid(row=3, column = 0,sticky = "n")

num8_button = tk.Button(window,command = num8 ,text ="8",width = 6,height=3,pady=0,padx=0)
num8_button.grid(row=3, column = 1,sticky = "n")

num9_button = tk.Button(window,command = num9 ,text ="9",width = 6,height=3,pady=0,padx=0)
num9_button.grid(row=3, column = 2,sticky = "n")

num0_button = tk.Button(window,command = num0 ,text ="0",width = 6,height=3,pady=0,padx=0)
num0_button.grid(row=4, column = 0,sticky = "n")

add_button = tk.Button(window,command = add ,text ="+",width = 6,height=3,pady=0,padx=0)
add_button.grid(row=1, column = 3,sticky = "n")

sub_button = tk.Button(window,command = sub ,text ="-",width = 6,height=3,pady=0,padx=0)
sub_button.grid(row=2, column = 3,sticky = "n")

mult_button = tk.Button(window,command = mult ,text ="*",width = 6,height=3,pady=0,padx=0)
mult_button.grid(row=3, column = 3,sticky = "n")

div_button = tk.Button(window,command = div ,text ="/",width = 6,height=3,pady=0,padx=0)
div_button.grid(row=4, column = 3,sticky = "n")

open_button = tk.Button(window,command = open_1 ,text ="(",width = 6,height=3,pady=0,padx=0)
open_button.grid(row=4, column = 1,sticky = "n")

close_button = tk.Button(window,command = close ,text =")",width = 6,height=3,pady=0,padx=0)
close_button.grid(row=4, column = 2,sticky = "n")

result_button = tk.Button(window,command = calc ,text ="calc",width = 13,height=2,pady=0,padx=0)
result_button.grid(row=5, column = 0,sticky = "n",columnspan= 2)

clear_button = tk.Button(window,command = clear ,text ="clear",width = 13,height=2,pady=0,padx=0)
clear_button.grid(row=5, column = 2,sticky = "n",columnspan= 2)

window.mainloop()