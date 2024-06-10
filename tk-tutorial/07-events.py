import tkinter as tk
from tkinter import ttk

def get_pos(event):
  print(f"x {event.x} y: {event.y}")
  
def mouse_wheel(event):
 
  print("Mousewheel")
# window
window = tk.Tk()
window.title("Events Binding")
window.geometry("600x500")

# widgets
text = tk.Text(window)
text.pack(pady=5) 

entry = ttk.Entry(window)
entry.pack(pady=5)

button = ttk.Button(window,text="A button")
button.pack()

# events format (for more event search about them)

# window.bind('<modifer-type-detail>',function)
# window.bind('<Alt-KeyPress-a>',lambda event :print(event))
# button.bind('<Alt-KeyPress-b>',lambda event :print(event))

# by default, tkinter pass an event argument to the called function 'get_pos'
# text.bind('<Motion>',get_pos) 

# text.bind('<KeyPress>',lambda event: print(f"char {event.char} was pressed"))

# entry.bind('<FocusIn>',lambda event:print('enter your name'))

# exercise
# print 'Mousewheel' when the user hold down shift and uses the mousewheel while the text is selected
text.bind("<Shift-MouseWheel>",lambda event: mouse_wheel(event))

# run
window.mainloop()