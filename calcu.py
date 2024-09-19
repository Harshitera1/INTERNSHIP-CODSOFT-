import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_op.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation!")

        label_result.config(text=f"Result: {result}")
    
    except ValueError as e:
        messagebox.showerror("Input Error", f"Error: {e}")

root = tk.Tk()
root.title("Simple Calculator")
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_op = tk.Label(root, text="Enter operation (+, -, *, /):")
label_op.grid(row=2, column=0, padx=10, pady=10)

entry_op = tk.Entry(root)
entry_op.grid(row=2, column=1, padx=10, pady=10)

btn_calculate = tk.Button(root, text="Calculate", command=calculate)
btn_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()

