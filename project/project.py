import tkinter as tk
from tkinter import ttk,messagebox

pizza_prices = {"Small": 5, "Medium": 7, "Large": 10}
burger_prices = {"Classic": 5, "Big": 7}

def calculate_order_price():
    total_order = extra_cheese_int.get() + extra_ketchup_int.get() + (soft_drink_int.get()*2)
    
    # Calculate pizza price
    pizza_price = pizza_prices.get(pizza_selected_option.get(), 0)
    total_order += (pizza_price * pizza_quantity_int.get())
    
    # Calculate burger price
    burger_price = burger_prices.get(burger_selected_option.get(), 0)
    total_order += (burger_price * burger_quantity_int.get()) 
    return total_order

def place_order():
    total_order = calculate_order_price()
    
    response = messagebox.askquestion("Order", f"Your Total Price is {total_order}. Do you want to proceed?")
    if response == 'yes':
        messagebox.showinfo("Information", "Thank you for choosing our restaurant :)")
    else:
        messagebox.showinfo("Information", "See you later")
        
    pizza_quantity_int.set(0)
    pizza_selected_option.set('')
    burger_quantity_int.set(0)
    burger_selected_option.set('')
    
    
  

window = tk.Tk()
window.title('Slice Heaven')
window.geometry('1000x500')


style = ttk.Style()
style.configure("Title.TLabel", background="lightblue", foreground="darkblue", padding=10)


top_title_1 = ttk.Label(master=window, text='Discover And Get Great Food', font=('Calibri', 24, 'bold'), style="Title.TLabel")
top_title_1.pack()


separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x', padx=10, pady=10)
## pizza section
pizza = ttk.Label(window,text="Pizza",font='Calibri 20 bold').pack(pady=10) 
# 1- Quantity:
pizza_quantity_frame = ttk.Frame(window)

pizza_quantity_int = tk.IntVar()
pizza_quantity_label = ttk.Label(pizza_quantity_frame,text="Quantity: ")

pizza_quantity_entry = ttk.Entry(pizza_quantity_frame,textvariable=pizza_quantity_int)


pizza_quantity_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
pizza_quantity_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

pizza_quantity_frame.pack()



# 2- Size: 
pizza_size_frame = ttk.Frame(window)
pizza_size_label = ttk.Label(pizza_size_frame,text="Size: ")
pizza_size_label.grid(row=0, column=0, padx=25, pady=5, sticky='w')

pizza_selected_option = tk.StringVar()
pizza_options = ["Small", "Medium", "Large"]

pizza_dropdown = ttk.Combobox(pizza_size_frame, textvariable=pizza_selected_option)
pizza_dropdown['values'] = pizza_options   # Set the options for the Combobox
pizza_dropdown.current(0)  # Set the default value
pizza_dropdown  # Use pack geometry manager to add it to the window

pizza_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky='e')

pizza_size_frame.pack()

## burger section 
pizza = ttk.Label(window,text="Burger",font='Calibri 20 bold').pack(pady=10) 

# 1- Quantity:
burger_quantity_frame = ttk.Frame(window)

burger_quantity_int = tk.IntVar()
burger_quantity_label = ttk.Label(burger_quantity_frame,text="Quantity: ")

burger_quantity_entry = ttk.Entry(burger_quantity_frame,textvariable=burger_quantity_int)


burger_quantity_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
burger_quantity_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

burger_quantity_frame.pack()

# 2- Size: 
burger_size_frame = ttk.Frame(window)
burger_size_label = ttk.Label(burger_size_frame,text="Size: ")
burger_size_label.grid(row=0, column=0, padx=25, pady=5, sticky='w')

burger_selected_option = tk.StringVar()
burger_options = ["Classic","Big"]

burger_dropdown = ttk.Combobox(burger_size_frame, textvariable=burger_selected_option)
burger_dropdown['values'] = burger_options   # Set the options for the Combobox
burger_dropdown.current(0)  # Set the default value
burger_dropdown  # Use pack geometry manager to add it to the window

burger_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky='e')

burger_size_frame.pack()

## common widgets
 
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x', padx=10, pady=10)

# 3- Soft Drinks, common between the piza and burger: 
soft_drink_frame = ttk.Frame(window)
soft_drink_label = ttk.Label(soft_drink_frame,text="Soft Drinks")
soft_drink_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
soft_drink_int = tk.IntVar()
soft_drink_entry = ttk.Entry(soft_drink_frame,textvariable=soft_drink_int)
soft_drink_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

soft_drink_frame.pack()

# 4- extra cheese and katchup
extra_cheese_int = tk.IntVar()
extra_cheese = ttk.Checkbutton(
  window,
  text="Extra Cheese",
  onvalue=1,
  offvalue= 0,
  variable=extra_cheese_int,

  ).pack()

extra_ketchup_int = tk.IntVar()
extra_ketchup = ttk.Checkbutton(
  window,
  text="Extra Ketchup",
  variable=extra_ketchup_int,
  onvalue=1,
  offvalue= 0,
  ).pack()
# 4- Dine in or Take Away?
radio_str = tk.StringVar()
dine_in_radio = ttk.Radiobutton(
  window,
  text="Dine In",
  variable=radio_str,
  value='in',
  command=lambda: print(radio_str.get()))

take_away_radio = ttk.Radiobutton(
  window,
  text="Take Away",
  variable=radio_str,
  value='out',
  command=lambda: print(radio_str.get()))

dine_in_radio.pack()
take_away_radio.pack()

order_button = ttk.Button(window,text="Order",command=place_order).pack()


window.mainloop()