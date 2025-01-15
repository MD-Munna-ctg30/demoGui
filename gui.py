import tkinter as tk
from tkinter import ttk


# Function to handle button clicks
def button_click(value):
    current = input_text.get()
    if value == "C":
        input_text.set("")
    elif value == "=":
        try:
            result = eval(current)
            input_text.set(result)
        except Exception:
            input_text.set("Error")
    else:
        input_text.set(current + value)


# Create main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")
root.resizable(0, 0)
# Colors
bg_color = "#2c3e50"
button_color = "#5dade2"
equal_button_color = "#f39c12"
text_color = "#ffffff"

# Frame for the display
frame_display = tk.Frame(root, bg=bg_color)
frame_display.pack(pady=20, fill="both")

# Input display
input_text = tk.StringVar()
input_field = tk.Entry(frame_display,
                       textvariable=input_text,
                       font=("Arial", 24),
                       justify="right",
                       bd=10,
                       relief="flat",
                       bg=bg_color,
                       fg=text_color)
input_field.pack(fill="both", pady=10, padx=10)

# Frame for buttons
frame_buttons = tk.Frame(root, bg=bg_color)
frame_buttons.pack(fill="both")

# Buttons layout
buttons = [["7", "8", "9", "/"], ["4", "5", "6", "*"], ["1", "2", "3", "-"],
           ["C", "0", ".", "+"], ["", "", "=", ""]]











# Adding buttons
for row_index, row in enumerate(buttons):
    for col_index, char in enumerate(row):
        if char:  # Skip empty spaces
            button = tk.Button(frame_buttons,
                               text=char,
                               command=lambda value=char: button_click(value),
                               bg=button_color,
                               fg=text_color,
                               font=("Arial", 16, "bold"),
                               relief="flat",
                               bd=5)
            button.grid(row=row_index,
                        column=col_index,
                        sticky="nsew",
                        padx=5,
                        pady=5)

# Equal button customization
equal_button = tk.Button(frame_buttons,
                         text="=",
                         command=lambda: button_click("="),
                         bg=equal_button_color,
                         fg=text_color,
                         font=("Arial", 16, "bold"),
                         relief="flat",
                         bd=5)
equal_button.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

# Configure row and column weights
for i in range(5):
    frame_buttons.rowconfigure(i, weight=1)
for i in range(4):
    frame_buttons.columnconfigure(i, weight=1)

# Run the application
root.mainloop()
