import tkinter as tk
from tkinter import ttk

# window 

window = tk.Tk()
window.geometry('600x400')
window.title('Tkinter variables ')

# tkinter vriable, I can connect this virable to multiple widgets by setting the 'textvariable' for each varaibles
string_var = tk.StringVar(value='Default Value')

# widgets

label_1 = ttk.Label(master=window,text='some texr',textvariable=string_var)
label_1.pack(pady=20)

entry_1 = ttk.Entry(master=window,textvariable=string_var)
entry_1.pack(pady=20)

# excercise 
exercise_var = tk.StringVar(value='test')

label_2 = ttk.Label(master=window,text='some text',textvariable=exercise_var)
label_2.pack()
entry_2 = ttk.Entry(master=window,textvariable=exercise_var)
entry_2.pack()

entry_3 = ttk.Entry(master=window,textvariable=exercise_var)
entry_3.pack()
# run
window.mainloop()