import tkinter as tk
from tkinter.ttk import *

base = tk.Tk()
base.title("Calculator")
base.geometry("350x500")


def show(num):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    operators = ['+','-','*','/']

    if num in numbers:
        num = int(num)
        entry.insert(tk.END , num)
    elif num in operators:
        entry.insert(tk.END , num)
    elif num == '=':
        equation = entry.get('1.0' , tk.END)
        result = eval(equation)
        entry.delete("1.0" , tk.END)
        entry.insert("1.0" , result)
    else:
        entry.delete("1.0" , tk.END)    
        

nb = Notebook(base)

frame = Frame(base)

entry = tk.Text(frame , width=40 , height=1)
entry.grid(row=0 , column=0 , columnspan=4, pady=10)

i = 1
for x in range(1 , 4):
    for y in range(1 , 4):
        button = Button(frame , text=f'{i}' , command=lambda b = i : show(b))
        button.grid(row=x , column=y-1)
        i = i + 1

arr = ['+','-','*','/']
for index , val in enumerate(arr):
    button = Button(frame , text=f'{val}' , command= lambda b = val : show(b))
    button.grid(row=index+1 , column=3)

arr = ['<','0','=']
for index , val in enumerate(arr):
    button = Button(frame , text=f"{val}" , command= lambda b = val : show(b))
    button.grid(row=4 , column=index)


frame.pack(fill=tk.BOTH , expand=True)

nb.pack(fill=tk.BOTH , expand=True , padx=10 , pady=10)
nb.add(frame , text="Main")

base.mainloop()