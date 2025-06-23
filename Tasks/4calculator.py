import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            result_label.config(text="Invalid operator selected")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operator_var.set("")
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x300")
root.config(bg="#f0f8ff")

tk.Label(root, text="Calculator", font=("Segoe UI", 16, "bold"), bg="#f0f8ff").pack(pady=10)

tk.Label(root, text="Enter first number:", bg="#f0f8ff").pack()
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="#f0f8ff").pack()
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

tk.Label(root, text="Select operator (+, -, *, /, %):", bg="#f0f8ff").pack()
operator_var = tk.StringVar()
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/", "%")
operator_menu.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
result_label = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#f0f8ff")
result_label.pack()

tk.Button(root, text="Clear", command=clear).pack(pady=5)

root.mainloop()