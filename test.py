import tkinter as tk  

class MyCalculator:
    def __init__(self):
        
        self.root = tk.Tk()
        
        self.root.geometry("300x300")
        self.root.title("My Calculator")
        
        self.label = tk.Label(self.root, text="Hello DIP02", font=('Arial', 10))
        self.label.pack()
        
        self.button = tk.Button(self.root, text="AC", height=4, width=8)
        self.button.place(x=20, y=50)
        
        self.button = tk.Button(self.root, text="+/-", height=4, width=8)
        self.button.place(x=85, y=50)
        
        self.button = tk.Button(self.root, text="%", height=4, width=8)
        self.button.place(x=150, y=50)
        
        self.button = tk.Button(self.root, text="/", height=4, width=8)
        self.button.place(x=215, y=50)
        
        
        self.button = tk.Button(self.root, text="7", height=4, width=8)
        self.button.place(x=20, y=120)
        
        self.button = tk.Button(self.root, text="8", height=4, width=8)
        self.button.place(x=85, y=120)
        
        self.button = tk.Button(self.root, text="9", height=4, width=8)
        self.button.place(x=150, y=120)
        
        self.button = tk.Button(self.root, text="x", height=4, width=8)
        self.button.place(x=215, y=120)
        
        
        self.button = tk.Button(self.root, text="4", height=4, width=8)
        self.button.place(x=20, y=190)
        
        self.button = tk.Button(self.root, text="5", height=4, width=8)
        self.button.place(x=85, y=190)
        
        self.button = tk.Button(self.root, text="6", height=4, width=8)
        self.button.place(x=150, y=190)
        
        self.button = tk.Button(self.root, text="-", height=4, width=8)
        self.button.place(x=215, y=190)
        
        
        self.button = tk.Button(self.root, text="1", height=4, width=8)
        self.button.place(x=20, y=260)
        
        self.button = tk.Button(self.root, text="2", height=4, width=8)
        self.button.place(x=85, y=260)
        
        self.button = tk.Button(self.root, text="3", height=4, width=8)
        self.button.place(x=150, y=260)
        
        self.button = tk.Button(self.root, text="+", height=4, width=8)
        self.button.place(x=215, y=260)
        
        
        self.button = tk.Button(self.root, text="0", height=4, width=18)
        self.button.place(x=20, y=330)
        
        self.button = tk.Button(self.root, text=".", height=4, width=8)
        self.button.place(x=150, y=330)
        
        self.button = tk.Button(self.root, text="=", height=4, width=8)
        self.button.place(x=215, y=330)
        
        
        self.root.mainloop()

MyCalculator()