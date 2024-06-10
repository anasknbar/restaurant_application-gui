import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Buttons')
window.geometry('500x500')

# button 
button_str = tk.StringVar(value='default')
button = ttk.Button(window,text='regular button',textvariable=button_str)
button.pack()

# checkbox
check_var = tk.BooleanVar()
check = ttk.Checkbutton(
  window,
  text='extra cheese',
  variable=check_var,
  command=lambda: print(check_var.get()))
# we use StringVar/IntVar/BooleanVar to know if the checkbox is checked or not
# you can customise the returned value using onvalue/offvalue
check.pack()


# radio buttons
radio_var = tk.StringVar() # I can link this variable to many radio button

radio_1 = ttk.Radiobutton(
  window,
  text='Radiobutton 1',
  value=1,
  variable=radio_var,
  command=lambda: print(radio_var.get()))
radio_1.pack()

radio_2 = ttk.Radiobutton(
  window,
  text='Radiobutton 2',
  value=2,
  variable=radio_var,
  command=lambda: print(radio_var.get()))
radio_2.pack()

# ------exercise-------:
def action():
  print(check_bool.get())
  
  check_bool.set(False)  
  
exercise = ttk.Label(
  window,
  text='Exercise',
  )
exercise.pack(pady=10)

check_bool = tk.BooleanVar()
exercise_checkbutton = ttk.Checkbutton(
  window,
  text="exercise checkbutton",
  variable=check_bool,
  command=lambda: print(radio_var.get())
  )

radio_var = tk.StringVar()
exercise_radiobutton_1 = ttk.Radiobutton(
  window,
  text="exercise radiobutton_1",
  value='A',
  variable=radio_var,
  command= action
  )
  

exercise_radiobutton_2 = ttk.Radiobutton(
  window,
  text="exercise radiobutton_2",
  value="B",
  variable=radio_var,
  command= action

  )

exercise_checkbutton.pack()
exercise_radiobutton_1.pack()
exercise_radiobutton_2.pack()
# run
window.mainloop()