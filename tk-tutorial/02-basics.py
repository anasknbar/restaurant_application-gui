import tkinter as tk
from tkinter import ttk
# create window
window = tk.Tk()
window.title('window and widgets')
window.geometry('900x500')

def btn_fun():
  pass

def hello_fun():
  print('Hello')

# creating widgets (we have tk widgets(basic and old) and ttk widgets (more advance and new))

# tk text widgets
text = tk.Text(master=window)
text.pack()

# ttk label widgets
label_1 = ttk.Label(master=window,text='this is text')
label_1.pack()

# ttk entry
entry_int = tk.IntVar()
entry = ttk.Entry(master=window,textvariable=entry_int)
entry.pack()

# excercise label
label_2 = ttk.Label(master=window,text='my label')
label_2.pack()

# ttk button
button_1 = ttk.Button(master=window,text='click me', command=btn_fun)
button_1.pack(pady=20)

# excercise button
button_2 = ttk.Button(master=window,text='Hi',command=hello_fun)
button_2.pack()




# run
window.mainloop() # update the gui, and check for events (click,mouse move ..etc)