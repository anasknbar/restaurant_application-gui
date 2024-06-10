import tkinter as tk
from tkinter import ttk

def disabled_fun():
  # get the content of the entry
  print(entry.get())
   # update widgets
  # widgets can be updated with config (two mwthod)
  # 1- Label.config(text='some new text')
  # 2- Label.['text'] = 'some new text'
  # >> i.e: label.config(text='new text')
  
  label['text'] = entry.get()
  
  # other events, disabled the widget after clicking th button
  entry['state'] = 'disabled'
  # button['state'] = 'disabled'
  
  # see all the widgets events
  # print(label.configure())
  # print(button_1.configure())
  
def  normal_fun():
  label['text'] = 'some text'
  entry['state'] = 'normal'
  
# window
window = tk.Tk()
window.geometry('400x400')
window.title('getting and setting widgets')

# widgets

label = ttk.Label(master=window,text='Text goes here..')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button_1 = ttk.Button(master=window,text='disabled',command=disabled_fun) 
button_1.pack()
button_2 = ttk.Button(master=window,text='abled',command=normal_fun) 
button_2.pack()
# run
window.mainloop()