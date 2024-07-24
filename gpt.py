import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get().replace('÷', '/').replace('×', '*')))
            screen.delete(0, tk.END)
            screen.insert(tk.END, result)
        except Exception:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "AC":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.geometry("320x500")
root.title("Calculator")

# Entry widget for the display screen
screen = tk.Entry(root, font="lucida 30 bold", bd=0, relief=tk.FLAT, justify='right', bg="#4D4D4D", fg="white")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame for buttons
button_frame = tk.Frame(root, bg="#4D4D4D")
button_frame.pack(expand=True, fill='both')

# Colors
bg_color = "#4D4D4D"  # dark gray for background
button_color = "#FF9500"  # orange for operation buttons
num_color = "#666666"  # gray for number buttons
dark_grey = "#222222"  # dark grey for specific buttons
text_color = "#FFFFFF"  # white for text

# Buttons layout
buttons = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Create buttons with the specified colors
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        if button_text in ["AC", "+/-", "%"]:
            button = tk.Button(button_frame, text=button_text, font="lucida 18 bold", bg=dark_grey, fg=text_color, relief=tk.FLAT, border=0)
        elif button_text in ["÷", "×", "-", "+", "="]:
            button = tk.Button(button_frame, text=button_text, font="lucida 18 bold", bg=button_color, fg=text_color, relief=tk.FLAT, border=0)
        else:
            button = tk.Button(button_frame, text=button_text, font="lucida 18 bold", bg=num_color, fg=text_color, relief=tk.FLAT, border=0)

        # Configure grid for the buttons
        if button_text == "0":
            button.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
        elif button_text == ".":
            button.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)
        elif button_text == "=":
            button.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)
        else:
            button.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
        
        button.bind("<Button-1>", button_click)

# Adjust column and row weights
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

# Set background color of the main window
root.configure(bg=bg_color)

root.mainloop()
