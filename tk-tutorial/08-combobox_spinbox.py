import tkinter as tk
from tkinter import ttk

def combo_fun():
  print('something')
# window 
window = tk.Tk()
window.title("Combobox and Spinbox")
window.geometry("500x400")

# widgets

items = ("ice cream","pizza","broccoli")
food_string = tk.StringVar(value= items[0])
combo = ttk.Combobox(window,textvariable=food_string)
# combo.configure(values=items)
combo['values'] = items
combo.pack()

# combo events
combo.bind("<<ComboboxSelected>>",lambda event:label_1.config(text=f"Selected Option: {food_string.get()}")) # special event for the combo 

label_1 = ttk.Label(window,text='a Label')
label_1.pack()

# spinbox

num_var = tk.IntVar(value=10)
spinbox = ttk.Spinbox(
  window,
  from_= 10,
  to=100,
  increment=10,
  textvariable=num_var
  )
spinbox.bind('<<Increment>>',lambda event: print(num_var.get()))
spinbox.bind('<<Decrement>>',lambda event: print(num_var.get()))
spinbox.pack()

# exercise
# 1- create a spinbox that contains the letters A B C D E.
# 2- and print the value whenever the value is decreased.
letters =  ("A","B","C","D","E")
letter_var = tk.StringVar(value=letters[0])
spbox = ttk.Spinbox(
  window,
  values=letters,
  textvariable=letter_var)


spbox.bind("<<Decrement>>",lambda event:print(letter_var.get()))
spbox.pack()

# run
window.mainloop()