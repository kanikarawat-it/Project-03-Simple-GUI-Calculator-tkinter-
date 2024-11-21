import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + value)

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def clear_entry():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 14), bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, command=lambda value=text: on_button_click(value) if value != '=' else calculate(), font=("Arial", 14), bd=5)
    btn.grid(row=row, column=col, ipadx=10, ipady=10)



# Special button for clearing the entry
clear_button = tk.Button(root, text="C", command=clear_entry, font=("Arial", 14), bg="red", fg="white", bd=5)
clear_button.grid(row=5, column=0, ipadx=10, ipady=10)

# Special button for the backspace operation
backspace_button = tk.Button(root, text="<-", command=lambda: entry_var.set(entry_var.get()[:-1]), font=("Arial", 14), bd=5)
backspace_button.grid(row=5, column=1, ipadx=10, ipady=10)



# Run the GUI
root.mainloop()
