import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Input field
entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font="Arial 18", padx=20, pady=20)
        btn.grid(row=i+1, column=j, sticky="nsew")
        btn.bind("<Button-1>", on_click)

# Make the grid expand properly
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i+1, weight=1)

# Start the application
root.mainloop()
