# import tkinter as tk
# # from tkinter import ttk
# import ttkbootstrap as ttk

# def convert():
#   mile_input = entry_int.get()
#   km_output = mile_input * 1.62
#   output_string.set(km_output)
  
# # window

# # window = tk.Tk()
# window = ttk.Window(themename='journal') # darkly
# window.title('Demo')
# window.geometry('500x300')

# #title

# title_label = ttk.Label(master=window,text="Resturant",font='Calibri 24 bold')
# title_label.pack()

# # input field

# input_frame = ttk.Frame(master=window)
# entry_int = tk.IntVar()
# entry = ttk.Entry(master=input_frame,textvariable=entry_int)

# button = ttk.Button(
#   master=input_frame,
#   text='click' ,
#   command= convert)

# entry.pack(side='left',padx=10)
# button.pack(side='left')
# input_frame.pack(pady=20)

# # output 
# output_string = tk.StringVar()
# output_label = ttk.Label(
#   master=window,text='Output',
#   font='Calibri 24 ',
#   textvariable=output_string)
# output_label.pack()
# window.mainloop()

# --------------------------------------
# import tkinter as tk
# from tkinter import ttk

# def main():
#     # Step 1: Create the main application window
#     root = tk.Tk()
#     root.title("Dropdown Menu Example")
#     root.geometry("300x200")

#     # Step 2: Create a StringVar to store the selected option
#     selected_option = tk.StringVar()

#     # Step 3: Define the options for the dropdown menu
#     options = ["Option 1", "Option 2", "Option 3", "Option 4"]

#     # Step 4: Create the ttk.Combobox widget
#     dropdown = ttk.Combobox(root, textvariable=selected_option)
#     dropdown['values'] = options  # Set the options for the Combobox
#     dropdown.current(0)  # Set the default value
#     dropdown.pack(pady=20)  # Use pack geometry manager to add it to the window

#     # Step 5: Create a button to display the selected option
#     def show_selected():
#         print(f"Selected option: {selected_option.get()}")

#     show_button = ttk.Button(root, text="Show Selected", command=show_selected)
#     show_button.pack(pady=10)

#     # Run the application
#     root.mainloop()

# if __name__ == "__main__":
#     main()
 # --------------------------------------
 
import tkinter as tk
from tkinter import ttk

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Widgets Next to Each Other")
    root.geometry("300x200")

    # Create a frame to hold the widgets
    frame = ttk.Frame(root, padding="10")
    frame.pack(fill='both', expand=True)

    # Create the label and entry widgets
    label = ttk.Label(frame, text="Label:")
    entry = ttk.Entry(frame)

    # Arrange the widgets using the grid manager
    label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
