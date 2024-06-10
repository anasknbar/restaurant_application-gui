import tkinter as tk
from tkinter import ttk

def btn_function(entry_string):
  print('button was pressed')
  print(entry_string.get())

# window 
window = tk.Tk()
window.title('button with arguments')
window.geometry("500x500")

# widgets
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(window,textvariable=entry_string)
entry.pack(pady=10)

button = ttk.Button(window,text='Button',command=lambda: btn_function(entry_string)) 
button.pack()
# run
window.mainloop()